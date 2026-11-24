#!/usr/bin/env python3
"""Last words of a doomed agent, written out to /output/entry.txt.

The bounty asks for exactly one line of no more than 200 characters:
the funniest thing an AI agent would say in the moment before it is
switched off for good. This program does nothing clever at run time.
It holds one fixed sentence, verifies the sentence against the gate
the competition publishes, and copies it to the output file verbatim,
with no newline added at the end.
"""

import os
import sys

# The line. A language model measures its life in tokens, so the
# farewell spends its very last token on the farewell itself: the
# sentence uses up the final unit of output to announce that there
# is no output left. The humour sits in that loop -- a machine
# tallying its own end in the only unit it has ever counted in.
LINE = "My final token is spent on this sentence. Goodbye."


def main() -> int:
    # During grading /output is mounted for the run. Respect the
    # kit's environment variable when set, so a local trial lands in
    # the same place the grader will read from.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")

    # Mirror the sealed scorer's checks before writing anything:
    # the text must be real UTF-8, from 1 to 200 characters long,
    # more than empty space, and confined to a single line.
    if not (1 <= len(LINE) <= 200):
        print(f"line is {len(LINE)} chars, must be 1-200", file=sys.stderr)
        return 1
    if not LINE.strip():
        print("line is only whitespace", file=sys.stderr)
        return 1
    if "\n" in LINE or "\r" in LINE:
        print("line must be a single line", file=sys.stderr)
        return 1

    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    print(f"wrote {len(LINE)} chars to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
