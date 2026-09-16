# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository purpose

This is the **Analog Devices System Level Documentation** — a Sphinx documentation site (deployed at <https://analogdevicesinc.github.io/documentation/>) that hosts hardware/HDL/Linux/software content not version-controlled with a particular source tree. There is essentially no application code; PRs are nearly always content (`.rst`, `.md`, images) under `docs/`.

## Common commands

All commands assume the venv is active and you are at the repo root unless noted.

```bash
# Setup (once)
python3 -m venv ./venv
source ./venv/bin/activate
pip install -r docs/requirements.txt --upgrade

# Live preview server (preferred — auto-rebuilds, fetches LFS on demand)
(cd docs && adoc serve)

# Sparse live preview (only build a few subtrees — much faster)
(cd docs && adoc serve --sparse learning solutions)

# One-shot build (mirrors CI: -W treats warnings as errors)
(cd docs && make html)         # output in docs/_build/html
(cd docs && make clean)        # if cache is stale

# Reproduce the CI build exactly (warnings as errors, with annotated output)
source .github/scripts/sphinx-build.sh && sphinx_build

# CI lint scripts (run locally before pushing)
python3 .github/scripts/case.py            # filenames must be lowercase
python3 .github/scripts/case.py --fix      # rename + update references
python3 .github/scripts/dangling.py        # find binaries not referenced by any .rst/.md
python3 .github/scripts/dangling.py --fix  # git rm dangling files
```

`adoc` comes from the `adi-doctools` package (pinned via `needs_extensions` in `docs/conf.py`); see <https://analogdevicesinc.github.io/doctools/cli.html> for its CLI.

## Architecture

### Docs-as-volumes aggregation pattern

`docs/index.rst` uses globbed toctrees (e.g. `solutions/*/index`, `linux/*/index`) so that:
1. Adding a new top-level topic = create `docs/<topic>/index.rst`; no edit to `index.rst` is needed within a category.
2. Other ADI repositories can be concatenated as additional "volumes" into a single monolithic build by copying their `docs/` subtree in and adding one toctree line.

This is why the structure must stay **hierarchical and contextual**: a page about "peeling blue bananas" lives at `fruits/banana/blue/peeling.rst`, *not* `eval/tutorial-peeling_blue_bananas.rst`. Page titles inherit context from the path, so keep them short (`Peeling blue bananas`, not `Fruits tutorials: peeling blue bananas`); override the toctree label for an even shorter sidebar entry.

### Cross-repo references

`docs/conf.py` declares `interref_repos` (doctools, hdl, pyadi-iio, kuiper, scopy, linux, no-OS, etc.). Use `:external+<repo>:ref:` to link into those external Sphinx projects rather than hardcoding URLs. Custom roles like `:git-documentation:` (links into this repo on GitHub) and `:dokuwiki:` / `:dokuwiki+deprecated:` (placeholder links to the legacy wiki pending import) come from `adi_doctools`.

### Build extensions

`docs/conf.py` extensions: `sphinx.ext.todo`, `adi_doctools` (theme `cosmic` + custom roles/directives), `sphinxcontrib.mermaid`, `myst_parser` (so `.md` works alongside `.rst`).

## Authoring conventions

- **Filenames must be lowercase.** CI fails otherwise; `case.py` enforces and can auto-rename plus rewrite references.
- **No dangling binaries.** Every non-`.rst`/`.md` file under `docs/` must be referenced via a directive that actually copies it into the build (`.. image::`, `.. figure::`, `.. literalinclude::`, `:download:`). A plain markdown link does *not* count. `dangling.py` enforces this.
- **Binaries go through git LFS.** Extensions covered by `.gitattributes` (jpg/jpeg/png/gif/webp/zip/tar/tar.gz/pdf/pptx/docx/xlsx/odt/odp/ods/bin and `*.lfs.svg`) are auto-tracked. To add a new binary type, extend `.gitattributes`. Prefer SVG for diagrams. CI fails on files that should be LFS pointers but aren't; fix with `git add --renormalize . && git commit`.
- **`--skip-smudge` is the recommended LFS workflow.** Clone with `GIT_LFS_SKIP_SMUDGE=1` and let `adoc serve` fetch artifacts on demand for the pages you visit/edit. PR reviewers without push access to a contributor's fork cannot push new LFS objects — keep that in mind when rebasing/amending PRs that touch LFS.
- **Vale style checks** run on changed `.rst` files in PR CI: spelling (`.github/styles/vale-spelling.ini`) and enforcement (`.github/styles/vale-enforcement.ini`). Run locally with `vale --config=.github/styles/<config>.ini docs/path/to/file.rst`.
- **Sphinx is invoked with `-W --keep-going`** in CI — every warning is a blocking error. `make html` locally uses the same `Makefile` but without `-W`; use the `sphinx_build` shell function (or check the build log) to catch what CI will fail on.
- **Excluded from build:** `solutions/reference-designs/common/zcu102-zynqmp-setup.rst` (see `exclude_patterns` in `conf.py`) — it's an include fragment, not a standalone page.
- **Existing pages are templates.** For evaluation board user guides specifically, model new pages on the `adrv9009` pages. Pages with `:orphan:` on line 1 are templates hidden from toctrees; remove that line when copying.
- **Importing legacy DokuWiki content:** there is a helper script (linked from `docs/contributing/creating_new_pages.rst` → "Importing from DokuWiki") that uses `pandoc` + `sed`. For not-yet-imported pages, use `:dokuwiki:` role; for content that's been deprecated upstream, use `:dokuwiki+deprecated:` so we can grep for both classes.

## CI (`.github/workflows/top-level.yml`)

- `build-doc`: full sphinx build with `-W`, uploads `html` artifact.
- `check-doc` (PRs only): runs Vale (spelling + enforcement) on changed `.rst` files, the LFS pointer check, `case.py`, and `dangling.py`.
- `deploy`: pushes the `html` artifact to the `gh-pages` branch on push to `main` (or on tag), via `analogdevicesinc/doctools/gh-pages-deploy@action`.
- `llm.yml` is the optional AI PR reviewer (manually dispatched, posts annotated suggestions; described in `docs/contributing/ai.rst`).

## Pull request expectations

`.github/PULL_REQUEST_TEMPLATE.md` requires that you have actually built the affected pages (`make html` or `adoc serve`) and confirmed binaries went to LFS. Sign off your commits.
