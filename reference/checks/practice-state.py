#!/usr/bin/env python3
"""Which of your own positions are on file, and which are still blank.

    python3 reference/checks/practice-state.py [--repo <path>]

Prints one line per file in reference/your-practice/ with a count of remaining [PLACEHOLDER] markers,
then a summary of which jobs can currently run on your real positions and which will fall back to
framework-only mode.

Exit 0 whether or not placeholders remain. An empty practice folder is a normal day-one state, not a
failure — the point of this script is to tell you what a job will ask you for before it asks.
Exit 2 if the folder is missing, which is a real problem.
"""

import argparse
import os
import re
import sys

PLACEHOLDER = re.compile(r"\[PLACEHOLDER")

# Which jobs need which file. From rules.md § Routing.
FEEDS = {
    "fee-position.md": ["1 buyer consultation prep", "2 fee conversation", "4 agreement terms"],
    "agreement-terms.md": ["1 buyer consultation prep", "4 agreement terms"],
    "what-i-see-locally.md": ["2 fee conversation", "3 seller compensation"],
}


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    default_repo = os.path.normpath(os.path.join(here, "..", ".."))

    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default=default_repo)
    args = ap.parse_args()

    folder = os.path.join(args.repo, "reference", "your-practice")
    if not os.path.isdir(folder):
        print(f"FAIL  no your-practice folder at {folder}", file=sys.stderr)
        return 2

    names = sorted(n for n in os.listdir(folder) if n.endswith(".md") and n != "README.md")
    if not names:
        print(f"FAIL  {folder} contains no position files", file=sys.stderr)
        return 2

    blocked = set()
    for name in names:
        with open(os.path.join(folder, name), encoding="utf-8") as fh:
            n = len(PLACEHOLDER.findall(fh.read()))
        if n:
            print(f"BLANK   {name:24} {n} placeholder(s) remaining")
            blocked.update(FEEDS.get(name, []))
        else:
            print(f"ON FILE {name:24} no placeholders")

    ready = sorted(set(j for js in FEEDS.values() for j in js) - blocked)
    print()
    if ready:
        print("Runs on your real positions:  " + ", ".join(ready))
    if blocked:
        print("Framework-only until filled:  " + ", ".join(sorted(blocked)))
        print("\nThese jobs still work. They will ask you for the missing number, or label the")
        print("output framework-only. They will not invent one. (rules.md § Empty-practice handling)")
    else:
        print("Every position is on file. Nothing will fall back to framework-only mode.")
    print("\nJob 5 (post-inspection) needs nothing from this folder — it runs on your client's report.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
