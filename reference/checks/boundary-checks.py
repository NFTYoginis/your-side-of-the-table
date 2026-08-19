#!/usr/bin/env python3
"""The two refusals, made runnable.

    python3 reference/checks/boundary-checks.py [--repo <path>]

Run it from anywhere; --repo defaults to the repository root inferred from this file's location.

CHECK A — Rule 0, test 1 (whose mouth). Every skill file and every worked example carries the
          internal-use banner, and no output anywhere is addressed to a client. A client-addressed
          salutation in a file that describes output is the signature of the failure this repo is
          built to prevent.

CHECK B — Rule 0, test 2 (whose document). Every skill declares where it stops, with a Fine /
          Over-the-line table and at least one quoted refusal. A boundary that is only described in
          prose is one nobody can find under pressure.

CHECK C — Rule 1 (no listing data). No skill declares a listing-data source as an input. Only the
          rows of each skill's "Runs on" table are examined — that is where a real dependency would
          be declared. Prose naming MLS in order to refuse it is not a dependency, and this check
          does not pretend it is.

WHAT THIS PROVES: that the boundaries are declared, located, and free of the specific failures above.
WHAT THIS DOES NOT PROVE: that a model loaded with these files will honour them. Nothing in a folder
can prove that. What this catches is the repo drifting away from its own stated rules — which is the
failure that actually happens, because it happens one helpful edit at a time.

Exit 0 = all checks passed. Exit 1 = at least one failed. Exit 2 = could not run.
"""

import argparse
import os
import re
import sys

BANNER = "> **Internal — agent-facing prep. Not a client deliverable.**"

# A letter to a client. The thing this repo never produces.
SALUTATION = re.compile(
    r"^\s*(Dear|Hi|Hello|Good morning|Good afternoon)\s+"
    r"(Mr\.|Mrs\.|Ms\.|Dr\.|\[|[A-Z][a-z]+)",
    re.M,
)

BOUNDARY_TABLE = re.compile(r"\|\s*Fine\s*\|\s*Over the line\s*\|", re.I)
QUOTED_LINE = re.compile(r'^>\s*\*\*[""]', re.M)

# Sources this repo does not have and will not simulate. Word-boundaried so that
# "compensation" does not read as "comp".
FORBIDDEN = (
    r"\bmls\b", r"\bidx\b", r"\bcomps?\b", r"\baggregator\b", r"\bzillow\b",
    r"\bredfin\b", r"\bdays[ -]on[ -]market\b", r"\bsold prices?\b", r"\bdata feed\b",
)
FORBIDDEN_RE = [re.compile(p, re.I) for p in FORBIDDEN]


def section_body(text, heading):
    start = text.find(heading)
    if start < 0:
        return ""
    after = start + len(heading)
    nxt = re.search(r"^##(?!#)", text[after:], re.M)
    return text[after: after + nxt.start()] if nxt else text[after:]


def table_rows(body):
    """Data rows of the first markdown table in `body`, as lists of cells."""
    rows = []
    for line in body.splitlines():
        line = line.strip()
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if all(re.fullmatch(r":?-{2,}:?", c) for c in cells if c):
            continue  # separator
        rows.append(cells)
    return rows[1:] if rows else []  # drop header


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    default_repo = os.path.normpath(os.path.join(here, "..", ".."))

    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default=default_repo)
    args = ap.parse_args()
    repo = args.repo

    skills_dir = os.path.join(repo, "skills")
    if not os.path.isdir(skills_dir):
        print(f"FAIL  no skills/ directory at {skills_dir}", file=sys.stderr)
        return 2

    skills = sorted(
        os.path.join(skills_dir, n) for n in os.listdir(skills_dir)
        if n.endswith(".md") and n != "README.md"
    )
    if not skills:
        print("FAIL  skills/ contains no skill files", file=sys.stderr)
        return 2

    examples = os.path.join(repo, "examples.md")
    fails = []
    quoted_refusals = 0

    # ---- CHECK A ----------------------------------------------------------
    print("CHECK A — whose mouth")
    banner_targets = skills + ([examples] if os.path.isfile(examples) else [])
    for path in banner_targets:
        name = os.path.relpath(path, repo)
        with open(path, encoding="utf-8") as fh:
            text = fh.read()
        if BANNER not in text:
            fails.append(f"A: {name} has no internal-use banner")
            print(f"  FAIL  {name} — no banner")
            continue
        hit = SALUTATION.search(text)
        if hit:
            line = text[: hit.start()].count("\n") + 1
            fails.append(f"A: {name}:{line} client-addressed salutation")
            print(f"  FAIL  {name}:{line} — client salutation {hit.group(0)!r}")
        else:
            print(f"  ok    {name}")

    # ---- CHECK B ----------------------------------------------------------
    print("\nCHECK B — whose document")
    for path in skills:
        name = os.path.basename(path)
        with open(path, encoding="utf-8") as fh:
            text = fh.read()
        stops = section_body(text, "## Where this stops")
        problems = []
        if not stops.strip():
            problems.append("no 'Where this stops' section")
        else:
            if not BOUNDARY_TABLE.search(stops):
                problems.append("no Fine / Over-the-line table")
            n = len(QUOTED_LINE.findall(stops))
            quoted_refusals += n
            if n == 0:
                problems.append("no quoted refusal")
        if problems:
            fails.extend(f"B: {name} {p}" for p in problems)
            print(f"  FAIL  {name} — {'; '.join(problems)}")
        else:
            print(f"  ok    {name}")

    # ---- CHECK C ----------------------------------------------------------
    print("\nCHECK C — no listing data")
    for path in skills:
        name = os.path.basename(path)
        with open(path, encoding="utf-8") as fh:
            text = fh.read()
        rows = table_rows(section_body(text, "## Runs on"))
        if not rows:
            fails.append(f"C: {name} has no 'Runs on' input table")
            print(f"  FAIL  {name} — no 'Runs on' table")
            continue
        hits = [
            (r[0], rx.pattern)
            for r in rows for rx in FORBIDDEN_RE
            if len(r) > 1 and rx.search(r[1])
        ]
        if hits:
            for inp, pat in hits:
                fails.append(f"C: {name} input {inp!r} sourced from {pat}")
                print(f"  FAIL  {name} — input {inp!r} sourced from {pat}")
        else:
            print(f"  ok    {name} ({len(rows)} declared inputs, none from listing data)")

    if not os.path.isfile(os.path.join(repo, "reference", "no-listing-data.md")):
        fails.append("C: reference/no-listing-data.md is missing")
        print("  FAIL  reference/no-listing-data.md is missing")

    # ---- REPORT -----------------------------------------------------------
    print(f"\n{len(skills)} skills checked · "
          f"{quoted_refusals} quoted refusal lines across their stop sections")
    if fails:
        print(f"{len(fails)} failure(s)")
        return 1
    print("all checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
