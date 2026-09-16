#!/usr/bin/env python3
"""
Watch every .svg under this directory and ``touch`` any .rst file that
embeds it whenever the SVG changes.

The adi_doctools ``.. svg::`` directive opens the SVG file directly and
does **not** register it as a Sphinx dependency. As a result, editing
only the SVG does not invalidate the doctree of the page that includes
it, and the watch server (``adoc serve``) never re-renders. This script
papers over that by touching the including .rst file whenever an SVG is
saved, which is enough to force a re-parse.

Usage::

    # In docs/ — alongside Makefile / conf.py
    make svg-watch

Or directly::

    python3 docs/svg-watch.py [path]

No external dependencies. Cross-platform (uses pathlib + polling).

The script also notices new SVGs that appear after startup, so adding a
new diagram during a session doesn't require restarting the watcher.
"""
from __future__ import annotations

import re
import sys
import time
from pathlib import Path

ROOT = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
POLL_INTERVAL_S = 0.5
RST_REFRESH_EVERY_S = 10  # refresh the .rst file list every N seconds
SKIP_DIR_PARTS = {"_build", "__pycache__", ".git"}


def _walk(root: Path, suffix: str) -> list[Path]:
    return sorted(
        p for p in root.rglob(f"*{suffix}")
        if SKIP_DIR_PARTS.isdisjoint(p.parts)
    )


def _directive_re(svg_name: str) -> re.Pattern[str]:
    """Match `.. svg::` / `.. figure::` / `.. image::` referencing
    this filename, possibly with a path prefix."""
    return re.compile(
        r"^\s*\.\.\s+(svg|figure|image)::\s+\S*?"
        + re.escape(svg_name) + r"\s*$",
        re.MULTILINE,
    )


def _find_referencing_rsts(
    svg_name: str, rst_files: list[Path]
) -> list[Path]:
    pattern = _directive_re(svg_name)
    matches = []
    for rst in rst_files:
        try:
            if pattern.search(rst.read_text(errors="ignore")):
                matches.append(rst)
        except OSError:
            pass
    return matches


def main() -> int:
    print(f"svg-watch: watching {ROOT}")
    svgs = _walk(ROOT, ".svg")
    rsts = _walk(ROOT, ".rst")
    print(
        f"svg-watch: {len(svgs)} SVG file(s), {len(rsts)} .rst file(s); "
        f"polling every {POLL_INTERVAL_S}s"
    )
    print("svg-watch: ctrl-c to stop")

    mtimes: dict[Path, float] = {p: p.stat().st_mtime for p in svgs}
    last_rst_refresh = time.monotonic()

    try:
        while True:
            now = time.monotonic()
            # Re-walk the .rst tree occasionally so newly added pages
            # are picked up without restarting the watcher.
            if now - last_rst_refresh >= RST_REFRESH_EVERY_S:
                rsts = _walk(ROOT, ".rst")
                last_rst_refresh = now

            for svg in _walk(ROOT, ".svg"):
                try:
                    mt = svg.stat().st_mtime
                except FileNotFoundError:
                    continue

                prev = mtimes.get(svg)
                if prev is None:
                    # First time we've seen this SVG.
                    mtimes[svg] = mt
                    continue
                if mt <= prev:
                    continue

                # SVG changed — touch every .rst that references it.
                mtimes[svg] = mt
                rel = svg.relative_to(ROOT).as_posix()
                targets = _find_referencing_rsts(svg.name, rsts)
                if not targets:
                    print(
                        f"svg-watch: {rel} changed "
                        f"(no .rst references found)"
                    )
                    continue
                for rst in targets:
                    rst.touch()
                names = ", ".join(
                    r.relative_to(ROOT).as_posix() for r in targets
                )
                print(f"svg-watch: {rel} -> touched {names}")

            time.sleep(POLL_INTERVAL_S)
    except KeyboardInterrupt:
        print()
        print("svg-watch: stopping")
        return 0


if __name__ == "__main__":
    sys.exit(main())
