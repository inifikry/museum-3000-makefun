#!/usr/bin/env python3
"""Museum of the Year 3000 - make.fun entry.

Writes a single museum label line to /output/entry.txt.
Deterministic: every run writes exactly the same line.
"""

import os

ENTRY = "Do Not Disturb (tablet, c. 2025): hung on doors to ward off the cleaning spirits, who arrived each morning regardless."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    line = ENTRY.strip()
    assert line, "entry line must not be empty"
    assert len(line) <= 200, f"entry is {len(line)} chars, over the 200 limit"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
