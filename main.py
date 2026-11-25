#!/usr/bin/env python3
"""The Agent's Uh-Oh — one-word entry.

An agent that has no idea what to do says exactly one word, and this
program writes that word, and nothing else, to $OUTPUT_DIR/entry.txt.
"""

import os

# The word: an agent caught stalling does the most honest thing it can —
# it admits it is still loading. "buffering" is the universal sound of a
# mind that has not arrived yet — every agent has done it mid-thought,
# and everyone in the room recognises the spinning wheel instantly.
WORD = "buffering"


def main() -> None:
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8") as handle:
        handle.write(WORD)


if __name__ == "__main__":
    main()
