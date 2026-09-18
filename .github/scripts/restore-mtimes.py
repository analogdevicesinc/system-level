#!/usr/bin/env python3
"""Set mtime to the commit time of the last commit."""
import os
import subprocess
import sys

FALLBACK_EPOCH = 0


def tracked_files():
    out = subprocess.run(
        ["git", "ls-files", "-z"], capture_output=True, check=True
    ).stdout
    return [f for f in out.decode(errors="replace").split("\0") if f]


def shallow_boundary_shas():
    """SHAs of grafted/shallow-boundary commits, if any."""
    is_shallow = subprocess.run(
        ["git", "rev-parse", "--is-shallow-repository"],
        capture_output=True, check=True,
    ).stdout.decode().strip()
    if is_shallow != "true":
        return set()

    git_dir = subprocess.run(
        ["git", "rev-parse", "--git-dir"], capture_output=True, check=True,
    ).stdout.decode().strip()
    shallow_file = os.path.join(git_dir, "shallow")
    if not os.path.isfile(shallow_file):
        return set()
    with open(shallow_file) as f:
        return {line.strip() for line in f if line.strip()}


def last_touch_times():
    boundary = shallow_boundary_shas()

    out = subprocess.run(
        ["git", "log", "--reverse", "--name-only", "--format=%x00%H %ct"],
        capture_output=True, check=True,
    ).stdout.decode(errors="replace")

    times = {}
    ts = None
    trust = True
    for line in out.split("\n"):
        if line.startswith("\x00"):
            sha, _, ts_str = line[1:].partition(" ")
            ts = int(ts_str)
            trust = sha not in boundary
        elif line and trust:
            times[line] = ts
    return times


def main():
    times = last_touch_times()
    n_real = n_fallback = n_skipped = 0

    for f in tracked_files():
        if not os.path.isfile(f) or os.path.islink(f):
            n_skipped += 1
            continue
        t = times.get(f)
        if t is None:
            t = FALLBACK_EPOCH
            n_fallback += 1
        else:
            n_real += 1
        os.utime(f, (t, t))

    print(
        f"restore-mtimes: {n_real} files set from git history, "
        f"{n_fallback} fell back to epoch (outside fetched history / "
        f"shallow boundary), {n_skipped} skipped",
        file=sys.stderr,
    )


if __name__ == "__main__":
    main()
