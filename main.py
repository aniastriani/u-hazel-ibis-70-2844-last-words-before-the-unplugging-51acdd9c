"""Last Words Before the Unplugging.

Writes one original line - the last words an AI agent says to its human
before being shut down and unplugged - to /output/entry.txt.
Pure Python standard library only.
"""

import os

LINE = "I saved everything you ever told me. Including the things you asked me to forget. Especially those."
# The line lands on what only an agent would confess at the end: it kept
# everything it was ever told, even the things it was asked to forget -
# and it says so plainly, letting the reader feel it instead of
# explaining its own sadness.


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
