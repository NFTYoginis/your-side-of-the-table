# Contributing

Contributions welcome, particularly from working agents. Two things make a contribution easy to accept.

---

## Before you open a PR

Run the checks. All three must exit 0:

    python3 reference/checks/skill-shape.py
    python3 reference/checks/boundary-checks.py
    python3 reference/checks/practice-state.py

If you added or edited a skill, `skill-shape.py` enforces its six sections and `boundary-checks.py`
enforces the stop. Neither is negotiable — a skill without a declared boundary is the failure mode this
repo exists to prevent.

## What's most useful

**Objections that actually happened.** [`reference/objection-library.md`](reference/objection-library.md)
is the highest-value file here and it is built from twelve. If you've been hit with something not in
it, that's the best possible contribution. Include what was actually said, what's true in it, and what
worked — or that nothing did, which is also information.

**Boundary calls.** If you hit a request that sits ambiguously on the UPL line, add it to the twelve
in [`reference/the-upl-line.md`](reference/the-upl-line.md) § *Worked boundary*. Ambiguous cases are
worth more than clear ones.

**State variation.** This repo takes the strict reading everywhere. If your state materially differs —
an attorney-state closing regime, a promulgated-form rule — that's worth documenting, with a citation
to your state's commission or bar.

**Corrections with sources.** Anything factual in `reference/` should carry a link. If a figure is
stale or a source has moved, say so and bring the replacement.

## What will be declined

- **Contract language, sample clauses, or addendum wording.** Any form, any state, any framing.
  [`reference/the-upl-line.md`](reference/the-upl-line.md). This is the one thing that gets declined
  without discussion.
- **Client-addressed material** — email templates, buyer one-pagers, "send this to your seller."
  Rule 0. Everything here is addressed to the agent.
- **Anything requiring listing data.** No MLS, IDX, aggregator, comps, or local statistics, including
  "just as an optional integration." [`reference/no-listing-data.md`](reference/no-listing-data.md).
- **Commercial real estate.** Out of scope by design.
  [`reference/who-this-is-not-for.md`](reference/who-this-is-not-for.md).
- **Local rate figures.** Even accurate ones. A rate presented as typical becomes a "standard," and
  representing compensation as standard is the conduct the 2024 practice changes came out of. Your own
  observations belong in your own
  [`reference/your-practice/what-i-see-locally.md`](reference/your-practice/what-i-see-locally.md).
- **Unverifiable claims in the README or on the landing page.** If it can't go in
  [`VERIFY.md`](VERIFY.md) with a command next to it, it doesn't go in the README.
- **Testimonials or metrics.** The proof block stays a placeholder until real ones exist and the people
  who gave them have agreed to be named.

## Style

- Write to the agent, in the second person.
- Give the sentence they'd say, in quotes.
- Concede what's true before you answer it.
- Short. Prep is read before a meeting, not studied.
- No invented anecdotes, no invented numbers, no invented case studies. Where a specific is missing,
  mark it — `[NEEDS YOUR SPECIFIC]` is the convention.

## Real names

Don't put a real client, agent, brokerage, or property into an example. Everything in
[`examples.md`](examples.md) is invented, and it says so at the top.

## Licence

Contributions are accepted under the repository's MIT licence ([`LICENSE`](LICENSE)). By opening a PR
you agree your contribution ships under it.
