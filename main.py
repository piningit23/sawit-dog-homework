#!/usr/bin/env python3
"""The Dog Ate My Homework: Funniest Excuse.

Writes one line, under 200 characters, in which a dog explains why the
homework got eaten, to /output/entry.txt. Pure standard library, fully
deterministic: the same line every run.
"""

import os

EXCUSE = (
    "I only ate the answers \u2014 the questions are buried in the yard "
    "if you still need them."
)


def main() -> None:
    text = EXCUSE.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
