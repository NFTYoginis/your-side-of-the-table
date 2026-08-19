#!/usr/bin/env python3
"""Every skill file carries the same six sections, a banner, and a quoted refusal.

    python3 reference/checks/skill-shape.py [--repo <path>]

Run it from anywhere; --repo defaults to the repository root inferred from this file's location.

WHAT THIS PROVES: that each skill in skills/ is shaped like a working skill — it says when to use it,
what it runs on, how to start from nothing, how it thinks, what it produces, and where it stops. The
"Output format" check is the one that matters most: a skill named for an artifact has to specify that
artifact, or the name is a claim the file does not honour.

WHAT THIS DOES NOT PROVE: that the content under any heading is correct, useful, or safe. A skill can
pass every check here and still give bad advice. This is a shape check. It is not a review.

Exit 0 = every skill passed. Exit 1 = at least one failed. Exit 2 = could not run.
"""

import argparse
import os
import re
import sys

REQUIRED_SECTIONS = (
    "## When to use",
    "## Runs on",
    "## The two questions",
    "## Method",
    "## Output format",
    "## Where this stops",
)

BANNER = "> **Internal — agent-facing prep. Not a client deliverable.**"

# A quoted refusal or line-to-say: a blockquote whose content is bolded and quoted.
QUOTED_LINE = re.compile(r'^>\s*\*\*[""]', re.M)

# Where a question that is not the agent's gets routed.
ROUTES = ("attorney", "counsel", "broker", "lender", "commission", "carrier")


def section_body(text, heading):
    """Text under `heading` up to the next same-or-higher-level heading."""
    start = text.find(heading)
    if start < 0:
        return ""
    after = start + len(heading)
    nxt = re.search(r"^##(?!#)", text[after:], re.M)
    return text[after: after + nxt.start()] if nxt else text[after:]


def check(path):
    """Return a list of failure strings for one skill file. Empty list = passed."""
    with open(path, encoding="utf-8") as fh:
        text = fh.read()
    fails = []

    for heading in REQUIRED_SECTIONS:
        if heading not in text:
            fails.append(f"missing section: {heading}")

    if BANNER not in text:
        fails.append("missing the internal-use banner")
    elif text.index(BANNER) > 400:
        fails.append("banner is not near the top of the file")

    stops = section_body(text, "## Where this stops")
    if stops:
        if not QUOTED_LINE.search(stops):
            fails.append('"Where this stops" has no quoted refusal line')
        if not any(r in stops.lower() for r in ROUTES):
            fails.append('"Where this stops" routes nowhere (no broker/attorney/lender/commission)')

    fmt = section_body(text, "## Output format")
    if fmt and len(fmt.strip()) < 400:
        fails.append('"Output format" is too thin to be an artifact spec')

    questions = section_body(text, "## The two questions")
    if questions and not re.search(r"^\s*(1\.|\*\*1)", questions, re.M):
        fails.append('"The two questions" has no numbered questions')

    return fails


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    default_repo = os.path.normpath(os.path.join(here, "..", ".."))

    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default=default_repo)
    args = ap.parse_args()

    skills_dir = os.path.join(args.repo, "skills")
    if not os.path.isdir(skills_dir):
        print(f"FAIL  no skills/ directory at {skills_dir}", file=sys.stderr)
        return 2

    names = sorted(
        n for n in os.listdir(skills_dir)
        if n.endswith(".md") and n != "README.md"
    )
    if not names:
        print("FAIL  skills/ contains no skill files", file=sys.stderr)
        return 2

    bad = 0
    for name in names:
        fails = check(os.path.join(skills_dir, name))
        if fails:
            bad += 1
            print(f"FAIL  {name}")
            for f in fails:
                print(f"        {f}")
        else:
            print(f"ok    {name}")

    print(f"\n{len(names)} skills checked, {len(names) - bad} passed, {bad} failed")
    print(f"required sections per skill: {len(REQUIRED_SECTIONS)}")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
