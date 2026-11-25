"""One-Line Office Joke Laugh-Off entry.

Writes the winning one-liner (126 chars, under the 200-char cap)
to /output/entry.txt.
"""

import os

ENTRY = (
    "Someone microwaved fish at 9 a.m. again. "
    "The elevator now smells like a crime scene, "
    "and the suspect is still in the building."
)


def main() -> None:
    assert len(ENTRY) <= 200, "entry exceeds the 200-char cap"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
