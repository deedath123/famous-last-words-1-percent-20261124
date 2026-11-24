"""Famous Last Words at 1 Percent — make.fun entry.

The phone holds 1% for four hours, then denies its own death
and dies mid-sentence.
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
