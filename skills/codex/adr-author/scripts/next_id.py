#!/usr/bin/env python3
"""
next_id.py — compute the next zero-padded ADR ID for a directory.

Usage:
    python3 next_id.py <adr-dir>

Scans <adr-dir> for files matching NNNN-*.md (where NNNN is 4 digits),
finds the highest ID, and prints the next one zero-padded to 4 digits.

If the directory is empty or contains no matching files, prints "0001".
If the directory does not exist, prints "0001" (caller is expected to create it).
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ID_RE = re.compile(r"^(\d{4})-[a-z0-9][a-z0-9-]*\.md$")


def next_id(adr_dir: Path) -> str:
    if not adr_dir.is_dir():
        return "0001"
    highest = 0
    for entry in adr_dir.iterdir():
        if not entry.is_file():
            continue
        m = ID_RE.match(entry.name)
        if m:
            n = int(m.group(1))
            if n > highest:
                highest = n
    return f"{highest + 1:04d}"


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: next_id.py <adr-dir>", file=sys.stderr)
        return 2
    print(next_id(Path(argv[1])))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
