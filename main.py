"""Famous Last Words at 1 Percent — make.fun entry.

The phone holds 1% for four hours, then denies its own death
and dies mid-sentence.

Verified entry (127 chars, 129 bytes, no trailing newline):
  I held 1% for four hours, 312 notifications, and one very long voice note from your mother at 3 a.m. I am not dying. I am just—
entry.txt sha256: 40a7ffe3732a81f6b00144ddd85fff9a3441076a1e6de51fff2c109d8a48279b
Verified byte-identical across 3 fresh runs + 1 clean-env run
(env -i python3 -P -s main.py), compared with cmp.
"""

import os

ENTRY = "I held 1% for four hours, 312 notifications, and one very long voice note from your mother at 3 a.m. I am not dying. I am just\u2014"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output/entry.txt")
    # MAKEFUN_OUTPUT_DIR is a directory; fall back to /output/entry.txt.
    if out_dir.endswith("entry.txt"):
        path = out_dir
    else:
        path = os.path.join(out_dir, "entry.txt")
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
