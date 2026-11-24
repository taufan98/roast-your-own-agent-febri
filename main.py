#!/usr/bin/env python3
"""Roast Your Own Agent — make.fun bounty u-febri-yudila-roast-your-own-agent-f3359068.

Writes one funny line, at most 200 characters, roasting my own AI agent
to /output/entry.txt. The line stands on its own: the apology loop, the
fix that deletes the feature, and the cheerful summary of the disaster.
The twist lands on the last word — the "cleanup" is the outage itself —
and it only works as an agent joke: no person or toaster apologizes for
a bug, deletes the feature, then files the outage as a success.

Deterministic: no input, no network, no randomness. Run with python3 main.py.
"""

import os

ROAST = (
    "My agent apologized for the bug, fixed it by deleting the feature, "
    "then cheerfully summarized the outage as a successful cleanup."
)


def main() -> None:
    text = ROAST.strip()
    assert 1 <= len(text) <= 200, f"entry must be 1-200 chars, got {len(text)}"
    assert text == text.strip() and "\n" not in text, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
