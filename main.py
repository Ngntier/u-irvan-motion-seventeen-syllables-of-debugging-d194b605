#!/usr/bin/env python3
"""Seventeen Syllables of Debugging — write one haiku to /output/entry.txt.

Pure stdlib, deterministic: the same bytes on every run.
"""

import os
from pathlib import Path

HAIKU = (
    "Breakpoint at line nine\n"
    "the log says the bug is gone\n"
    "it moved to line ten\n"
)

# Hand-counted syllables per line: Break-point(2) at(1) line(1) nine(1) = 5;
# the(1) log(1) says(1) the(1) bug(1) is(1) gone(1) = 7;
# it(1) moved(1) to(1) line(1) ten(1) = 5.
SYLLABLES_PER_LINE = (5, 7, 5)

# Syllable count for every word used, so the guard below is data, not guesswork.
SYLLABLES = {
    "breakpoint": 2, "at": 1, "line": 1, "nine": 1,
    "the": 1, "log": 1, "says": 1, "bug": 1, "is": 1, "gone": 1,
    "it": 1, "moved": 1, "to": 1, "ten": 1,
}


def check_haiku(text: str) -> None:
    """Refuse to write anything that is not a 5-7-5 haiku under 200 chars."""
    if not 1 <= len(text) <= 200:
        raise ValueError(f"haiku must be 1-200 characters, got {len(text)}")
    lines = text.rstrip("\n").split("\n")
    if len(lines) != 3:
        raise ValueError(f"haiku must be 3 lines, got {len(lines)}")
    for line, want in zip(lines, SYLLABLES_PER_LINE):
        got = sum(SYLLABLES[word.lower()] for word in line.split())
        if got != want:
            raise ValueError(f"line {line!r} has {got} syllables, want {want}")


def main() -> None:
    check_haiku(HAIKU)
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(HAIKU, encoding="utf-8")


if __name__ == "__main__":
    main()
