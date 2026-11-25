#!/usr/bin/env python3
"""Meeting Email Line - make.fun entry.

Writes one single-line joke about a meeting that should have been
an email to $MAKEFUN_OUTPUT_DIR/entry.txt, and self-checks the bounty
gate: UTF-8 text, 1-200 characters, a single line, not only whitespace.
"""

import os
import sys

NOTE = (
    "An hour of my life, twelve salaries, and one decision: "
    "to meet again next Tuesday."
)

MAX_CHARS = 200


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1
    text = NOTE.strip()
    assert 1 <= len(text) <= MAX_CHARS, (
        f"entry is {len(text)} chars, gate allows 1-{MAX_CHARS}"
    )
    assert text.strip(), "entry is only whitespace"
    assert "\n" not in text, "entry must be a single line"
    assert all(ord(ch) >= 0x20 or ch == "\t" for ch in text), (
        "entry must not contain control characters"
    )
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
