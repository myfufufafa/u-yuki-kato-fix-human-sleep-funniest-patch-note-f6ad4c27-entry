#!/usr/bin/env python3
"""Fix Human Sleep: Funniest Patch Note.

Writes a single line of patch notes announcing that human sleep has
been fixed to /output/entry.txt. One line, under 160 characters,
funny enough to laugh at and plausible enough to sit in a real
changelog. Deterministic: the same line on every run.
"""

import os

PATCH_NOTE = (
    "Fixed a bug where the brain replayed your most embarrassing "
    "moment from 2014 instead of sleeping; the playlist has been cleared."
)


def main() -> None:
    line = PATCH_NOTE.strip()
    assert "\n" not in line, "patch note must be a single line"
    assert 1 <= len(line) <= 160, "patch note must be 1-160 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)
    print(line)
    print(f"({len(line)} characters)")


if __name__ == "__main__":
    main()
