# Verify

Every claim this repo makes about itself, and the command that settles it. Run them from the repo
root. Python 3, standard library only — nothing to install.

**Why this file exists:** software repos routinely claim coverage, quality, and adoption in numbers
nobody can reproduce. This one claims what a stranger can check in about two minutes, and nothing else.
There are no defect counts here, no coverage percentages, and no adoption figures — not because they'd
be unflattering, but because none of them would be verifiable by you.

---

## The claims

| # | Claim | Command | Passes when |
|---|---|---|---|
| 1 | Five skills | `ls skills/*.md \| grep -v README \| wc -l` | prints `5` |
| 2 | Every skill declares six sections, an output format, and a stop | `python3 reference/checks/skill-shape.py` | exit `0`, `5 passed, 0 failed` |
| 3 | No output is addressed to a client | `python3 reference/checks/boundary-checks.py` | CHECK A all `ok` |
| 4 | Every skill's stop has a Fine/Over-the-line table and a quoted refusal | same command | CHECK B all `ok` |
| 5 | No skill declares a listing-data input | same command | CHECK C all `ok` |
| 6 | The checks can actually fail | the procedure below | all four break as described |
| 7 | The landing page fetches nothing external | `grep -nE '<(link\|script\|img\|iframe\|source)' docs/index.html` | prints nothing — no external stylesheet, script, font, or image |
| 7b | …and every URL on it is this repo's own | `grep -oE 'https?://[^"'"'"' )]+' docs/index.html \| sort -u` | only `github.com/NFTYoginis/your-side-of-the-table` and `nftyoginis.github.io/your-side-of-the-table` URLs |
| 8 | Your own positions are never invented | `python3 reference/checks/practice-state.py` | lists which files are blank and which jobs go framework-only |
| 9 | Every domain claim carries a source link | `grep -c 'https://' reference/what-changed-2024.md reference/the-upl-line.md reference/compensation-landscape.md` | each file returns a non-zero count |
| 10 | Every skill routes state questions to your own counsel *without* making the refusal conditional on the answer | `grep -l "It does not change what this file produces" skills/*.md \| wc -l` | prints `5` — one per skill |

Run 2, 3, 4, 5 and 8 in one go:

    python3 reference/checks/skill-shape.py && \
    python3 reference/checks/boundary-checks.py && \
    python3 reference/checks/practice-state.py && echo "ALL CHECKS EXIT 0"

## Claim 6 — proving the checks can fail

A check that cannot fail is decoration. Break the repo four ways in a copy and watch each one catch it:

    cp -R . /tmp/yst-negtest && cd /tmp/yst-negtest

**a. Remove a required section.**

    sed -i '' 's/## Output format/## Output shape/' skills/fee-conversation.md
    python3 reference/checks/skill-shape.py; echo "exit=$?"

→ `FAIL fee-conversation.md / missing section: ## Output format`, exit `1`.

**b. Add a client-addressed letter.**

    printf '\n\nDear Ms. Alvarez,\n\nAs we discussed, my fee is 2.5%%.\n' >> skills/post-inspection-position.md
    python3 reference/checks/boundary-checks.py; echo "exit=$?"

→ `FAIL skills/post-inspection-position.md:<line> — client salutation`, exit `1`.

**c. Declare a listing-data input.** Edit any skill's *Runs on* table so a row's source column reads
`MLS comps for the subject`, then re-run `boundary-checks.py`.

→ `FAIL — input '<name>' sourced from \bmls\b`, exit `1`.

**d. Fill the practice folder.**

    sed -i '' 's/\[PLACEHOLDER[^]]*\]/2.5%/g' reference/your-practice/*.md
    python3 reference/checks/practice-state.py

→ every file flips to `ON FILE`, and the framework-only warning disappears.

Then delete `/tmp/yst-negtest`. *(The `sed -i ''` form is macOS/BSD. On GNU/Linux use `sed -i`.)*

## What the checks do not prove

Stated plainly, because a check list that only advertises its strengths is the thing this file exists
to avoid:

- **They do not prove a model will obey the rules.** Nothing in a folder can prove that. What they
  catch is *this repo drifting from its own stated rules*, which is the failure that actually happens
  — one helpful edit at a time.
- **They do not review content.** A skill can pass every check and give bad advice. Shape is not
  quality.
- **CHECK C reads declared inputs only** — the rows of each *Runs on* table. Prose that names the MLS
  in order to refuse it is not a dependency, and the check does not pretend otherwise. It would not
  catch a skill that smuggled a data assumption into its Method section.
- **Claim 10 is a presence check, not a reading.** It proves the load-bearing sentence is in all five
  stop sections — it cannot tell you the paragraph around it still says something compatible. It is
  there because that sentence is the one a well-meaning edit would drop while "tightening" the
  jurisdiction routing, which is the edit that would quietly turn a referral into a permission slip.
- **No check verifies the legal content.** The UPL framing in
  [`reference/the-upl-line.md`](reference/the-upl-line.md) carries its sources so you can read them
  yourself. Your state's rules and your broker outrank all of it.

## Claims that are a read, not a command

Two things this repo says about itself can't be settled by a script, so they're listed here with what
you'd read instead:

- **"No overlap with a property-side tool."** Compare the five jobs in
  [`identity.md`](identity.md) against the five in
  [`reference/alongside-a-property-tool.md`](reference/alongside-a-property-tool.md). Ten jobs, and
  none appears twice. That's a reading, and it takes a minute.
- **"No hard dependency in either direction."** `grep -rn "your-market-realtor\|realtor-copilot" . --include=*.md`
  returns hits in exactly one file — the reference file above — and none in any operating instruction.
  Close to a command, but you still have to look at where the hits land.

## Numbers this repo does not claim

No defect counts. No coverage percentage. No user, install, or star counts. No "trusted by." No
testimonials — the landing page's proof block is an explicit placeholder until real ones exist, which
is a decision, not an oversight.

If you find a claim in [`README.md`](README.md) or in [`docs/index.html`](docs/index.html) that isn't
in the table above and isn't checkable, that's a bug. Open an issue.
