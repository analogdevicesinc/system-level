#!/usr/bin/env python3
"""Reject disallowed reStructuredText directives and options."""

import argparse
import os
import re
from pathlib import Path

GITHUB_ACTIONS = os.environ.get("GITHUB_ACTIONS", "false") == "true"

RULES = (
    (re.compile(r"^\s*\.\.\s+glossary::\s*$"), "Glossary definitions are global and prone to redefinition collision, and its usage has been disallowed; use a standard list instead."),
    (re.compile(r"^\s*:scale:\s*"), "Due to build optimization, the ':scale:' option is not allowed for images/figures; use width or nothing instead."),
)


def report(path, line, message):
    if GITHUB_ACTIONS:
        print(f"::error file={path},line={line}::{message}")
    else:
        print(f"{path}:{line}: ERROR: {message}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", nargs="*", type=Path, help="RST files to check")
    args = parser.parse_args()

    files = args.files or Path("docs").rglob("*.rst")
    failures = 0
    for path in files:
        if path.suffix != ".rst" or not path.is_file():
            continue
        for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            for pattern, message in RULES:
                if pattern.match(line):
                    report(path, line_number, message)
                    failures += 1

    return bool(failures)


if __name__ == "__main__":
    raise SystemExit(main())
