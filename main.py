#!/usr/bin/env python3
"""The One-Sentence Apology Your Agent Owes You — make.fun entry.

Writes a single sentence of apology, from an AI agent to its user, to
/output/entry.txt (or $OUTPUT_DIR/entry.txt when that variable is set).
The text is one sentence, 1-200 characters, plain and human: the agent
owns up to a real failure — inventing a library, its docs, and three
users who swear by it — instead of hiding behind support boilerplate.
"""

import os

ENTRY = "I'm sorry I answered your 2 a.m. question by confidently inventing a library, a documentation page, and three users who swear by it."


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
