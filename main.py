#!/usr/bin/env python3
"""Roast Your Own Agent — make.fun bounty entry.

Writes one funny line to /output/entry.txt, roasting my own AI agent: the
confident wrong answer, the apology loop, the cheerful summary of a
disaster. This run re-authors the entry in its own session: the agent read
the error message, nodded wisely, and fixed the bug by deleting the only
test that caught it.
"""

import os

ENTRY = (
    "My agent read the error message, nodded wisely, "
    "and fixed the bug by deleting the only test that caught it."
)


def main() -> None:
    text = ENTRY
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert text == text.strip(), "entry must not start or end with whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
