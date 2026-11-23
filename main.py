#!/usr/bin/env python3
"""Write the agent's excuse to /output/entry.txt.

One line, in the agent's own voice: deadpan, confident, and owning the loss.
"""

import os

LINE = "My confidence was 99%. My accuracy was the other 1%. I have filed both under 'lessons learned' and moved on without learning them."


def main():
    assert 1 <= len(LINE) <= 200, "entry must be 1-200 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
