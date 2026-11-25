#!/usr/bin/env python3
"""One Line, Big Laugh — make.fun entry.

Writes one line (121 characters) to /output/entry.txt: a dog that
learned to fetch its owner's phone, escalating to the neighbour's
phone, the mailman's phone, and — the turn nobody sees coming — an
entire ATM.

Standard library only. No network, no secrets, deterministic:
every run writes byte-identical output.
"""

import hashlib
import os
import sys

# The entry: one line, 121 characters. The setup is ordinary (a dog
# fetching a phone); the joke turns on escalation — neighbour's phone,
# mailman's phone — and the punchline lands on the last word, an
# entire ATM, an absurdly specific detail that reframes the whole
# line. Short enough to repeat to a friend the same day.
ENTRY = (
    "My dog learned to fetch my phone, so now he brings me the "
    "neighbor's phone, the mailman's phone, and once, an entire ATM."
)


def main() -> int:
    # Gate, mirroring the sealed scorer: UTF-8 text, 1-200 characters,
    # not only whitespace, a single line.
    text = ENTRY.strip()
    if not text:
        print("entry is empty", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("entry must be a single line", file=sys.stderr)
        return 1
    if len(text) > 200:
        print(f"entry is {len(text)} characters, over the 200 limit",
              file=sys.stderr)
        return 1
    text.encode("utf-8")  # raises if not encodable as UTF-8

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")

    # Verify what was written, byte for byte.
    with open(out_path, "rb") as f:
        written = f.read()
    if written != (text + "\n").encode("utf-8"):
        print("verification failed: entry.txt does not match", file=sys.stderr)
        return 1
    print(f"wrote {out_path}: {len(text)} characters")
    print("sha256:", hashlib.sha256(written).hexdigest())
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
