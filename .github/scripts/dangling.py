#!/usr/bin/env python3
"""
Find and remove dangling files (not referenced in any .rst or .md files) in docs folder.
"""

import os
import re
import argparse
import subprocess
from collections import defaultdict
from pathlib import Path

GITHUB_ACTIONS = os.environ.get("GITHUB_ACTIONS", "false") == "true"

if GITHUB_ACTIONS:
    warning = "{file}\n::warning file={file}::{message}"
    error = "{file}\n::error file={file}::{message}"
    notice = "::notice ::{message}"
else:
    warning = "WARNING: {file} - {message}"
    error = "ERROR: {message}"
    notice = "INFO: {message}"

EXCLUDE_FILES = {
    'conf.py', 'Makefile', 'make.bat', '.gitignore', '.gitattributes',
    'requirements.txt',
    'custom.css', 'icon.svg',
}

EXCLUDE_EXTENSIONS = {'.rst', '.md'}

SKIP_DIRS = {'_build', '__pycache__', '.git'}


def find_all_files(root_dir):
    """Find all files that could potentially be dangling."""
    files = []
    for root, dirs, filenames in os.walk(root_dir):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]

        for name in filenames:
            path = Path(root) / name
            ext = path.suffix.lower()

            if ext in EXCLUDE_EXTENSIONS:
                continue
            if name in EXCLUDE_FILES:
                continue

            files.append(path)

    return files


def find_doc_files(root_dir):
    """Find all .rst and .md files in the docs folder."""
    doc_files = []
    for root, dirs, filenames in os.walk(root_dir):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]

        for name in filenames:
            if name.endswith('.rst') or name.endswith('.md'):
                doc_files.append(Path(root) / name)

    return doc_files


def load_doc_contents(doc_files):
    """Load contents of all .rst and .md files into a dict for fast searching."""
    contents = {}
    for doc_file in doc_files:
        try:
            contents[doc_file] = doc_file.read_text(encoding='utf-8')
        except (UnicodeDecodeError, PermissionError):
            pass
    return contents


# Directives/roles that actually include files in the Sphinx build
# Optional path prefixes: ./ or ../*/ patterns
PATH_PREFIX = r'(?:\./|(?:\.\./)+(?:\w+/)*)?'

# RST patterns:
#   .. directive:: path
#   .. |substitution| directive:: path
#   .. .. directive:: path  (commented out)
#   :role:`text <path>` or :role:`path`
#   :option: path
VALID_RST_PATTERNS = [
    r'\.\.\s+(?:\|[^|]+\|\s+)?[\w-]+::\s*' + PATH_PREFIX,  # .. directive:: or .. |sub| directive::
    r':[\w-]+:`[^`]*<\s*' + PATH_PREFIX,  # :role:`text <path>`
    r':[\w-]+:`\s*' + PATH_PREFIX,  # :role:`path`
    r':[\w-]+:\s*' + PATH_PREFIX,  # :option: path
]

# MyST patterns:
#   ```{directive}
#   path
#   ```
#   {role}`text <path>` or {role}`path`
#   :option: path
VALID_MD_PATTERNS = [
    r'```\{[\w-]+\}\s*' + PATH_PREFIX,  # ```{directive} path
    r'\{[\w-]+\}`[^`]*<\s*' + PATH_PREFIX,  # {role}`text <path>`
    r'\{[\w-]+\}`\s*' + PATH_PREFIX,  # {role}`path`
    r':[\w-]+:\s*' + PATH_PREFIX,  # :option: path
]


def is_valid_reference(content, rel_path, patterns):
    """Check if rel_path is referenced via a valid Sphinx directive."""
    escaped_path = re.escape(rel_path)
    for pattern in patterns:
        # Check if the path follows a valid directive
        if re.search(pattern + escaped_path, content):
            return True
    return False


def _scan_docs(docs, doc_indexes, file_dir, name, relpath_cache):
    """Look for a valid reference to file_dir/name in the given documents."""
    for i in doc_indexes:
        doc_dir, content, patterns = docs[i]

        if name not in content:
            continue

        key = (file_dir, doc_dir)
        rel_dir = relpath_cache.get(key)
        if rel_dir is None:
            rel_dir = os.path.relpath(file_dir, doc_dir)
            relpath_cache[key] = rel_dir
        rel_path = name if rel_dir == '.' else os.path.join(rel_dir, name)

        if rel_path not in content:
            continue

        if is_valid_reference(content, rel_path, patterns):
            return True

    return False


def is_file_referenced(file_path, docs, name_index=None, relpath_cache=None):
    """Check if a file is referenced via valid Sphinx directives.

    Only directives that actually copy/include files in the build count:
    - RST: .. image::, .. figure::, :download:, .. literalinclude::, etc.
    - MyST: {image}, {figure}, {download}, {literalinclude}, etc.

    Plain links like [text](path) or `path` don't copy files to the build.
    """
    if relpath_cache is None:
        relpath_cache = {}

    file_dir, name = os.path.split(str(file_path))

    # Fast path: only the documents that mention the file name as a word.
    if name_index is not None:
        candidates = name_index.get(name)
        if candidates and _scan_docs(docs, candidates, file_dir, name,
                                     relpath_cache):
            return True

    # Exhaustive pass, so the result never depends on the index.
    return _scan_docs(docs, range(len(docs)), file_dir, name, relpath_cache)


def prepare_docs(doc_contents):
    """Flatten the documents into (dir, content, patterns) tuples."""
    docs = []
    for doc_file, content in doc_contents.items():
        patterns = VALID_MD_PATTERNS if doc_file.suffix == '.md' else VALID_RST_PATTERNS
        docs.append((str(doc_file.parent), content, patterns))
    return docs


# Runs of characters that can make up a path component, used to index which
# document mentions which file name.
NAME_TOKEN_RE = re.compile(r'[^\s/\\`\'"<>|(){}\[\],;:*?=]+')


def build_name_index(docs):
    """Map every path component found in the documents to the documents using it."""
    index = defaultdict(list)
    for i, (_, content, _) in enumerate(docs):
        for token in set(NAME_TOKEN_RE.findall(content)):
            index[token].append(i)
    return index


def find_dangling_files(root_dir):
    """Find files that are not referenced in any .rst or .md file."""
    all_files = find_all_files(root_dir)
    doc_files = find_doc_files(root_dir)
    doc_contents = load_doc_contents(doc_files)
    docs = prepare_docs(doc_contents)
    name_index = build_name_index(docs)

    relpath_cache = {}
    dangling = []
    for file_path in all_files:
        if not is_file_referenced(file_path, docs, name_index, relpath_cache):
            dangling.append(file_path)

    return dangling


def git_rm(file_path, dry_run=False):
    """Remove a file using git rm."""
    if dry_run:
        print(f"  Would run: git rm {file_path}")
        return True

    try:
        result = subprocess.run(
            ['git', 'rm', str(file_path)],
            capture_output=True,
            text=True
        )
        if result.returncode == 0:
            print(f"  Removed: {file_path}")
            return True
        else:
            print(f"  Failed to remove {file_path}: {result.stderr.strip()}")
            return False
    except Exception as e:
        print(f"  Error removing {file_path}: {e}")
        return False


def main():
    parser = argparse.ArgumentParser(description='Find and remove dangling files in docs')
    parser.add_argument('--fix', action='store_true', help='Remove dangling files with git rm')
    parser.add_argument('--dry-run', action='store_true', help='Show what would be removed')
    args = parser.parse_args()

    root_dir = 'docs'
    if not os.path.isdir(root_dir):
        print(error.format(file=root_dir, message="Directory does not exist"))
        return 1

    dangling = find_dangling_files(root_dir)

    if not dangling:
        print("No dangling files found")
        return 0

    for f in dangling:
        print(warning.format(file=str(f), message="Not referenced in any .rst or .md file"))

    print(f"\nFound {len(dangling)} dangling files\n")

    if not args.fix and not args.dry_run:
        print(notice.format(message="Remove dangling files by running `python3 .github/scripts/dangling.py --fix`"))
        return 1

    removed = 0
    for f in dangling:
        if git_rm(f, dry_run=args.dry_run):
            removed += 1

    if args.dry_run:
        print(f"\nDry run complete, {removed} files would be removed")
    else:
        print(f"\nRemoved {removed} dangling files")

    return 0


if __name__ == '__main__':
    exit(main())
