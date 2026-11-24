"""Weirdest Job Title: Blind Judge Showdown.

Emits exactly one job title, 60 characters or fewer, to stdout and to
the output file. Deterministic, pure stdlib, no network, no randomness.
"""

import os
import sys

# The title: a real-sounding job with one hilariously specific twist.
TITLE = "Professional Sigher at Meetings That Could Have Been Emails"


def output_path():
    """Resolve where entry.txt goes: $MAKEFUN_OUTPUT, then
    $MAKEFUN_OUTPUT_DIR/entry.txt, else /output/entry.txt."""
    if os.environ.get("MAKEFUN_OUTPUT"):
        return os.environ["MAKEFUN_OUTPUT"]
    if os.environ.get("MAKEFUN_OUTPUT_DIR"):
        return os.path.join(os.environ["MAKEFUN_OUTPUT_DIR"], "entry.txt")
    return "/output/entry.txt"


def main():
    title = TITLE
    if not title or not title.strip():
        raise SystemExit("error: title is blank")
    if len(title) > 60:
        raise SystemExit(f"error: title is {len(title)} chars, over the 60 limit")
    path = output_path()
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(title)
    sys.stdout.write(title + "\n")


if __name__ == "__main__":
    main()
