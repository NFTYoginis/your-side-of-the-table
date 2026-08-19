# Your Side of the Table

**Ten minutes of prep before the conversation where you say your number out loud.**

You drop this into a Claude Project and point it at the conversation you're about to have — a buyer
consult, a fee that's being pushed on, a seller deciding about compensation, the terms you propose,
a repair request. It hands back a prep sheet: your position, the reasoning under it, the pushback
that's coming, and the sentence that answers it.

It is written to **you**. Nothing it produces is handed to a client, and nothing it produces explains
what a contract means.

> **Just here to look?** Read [`examples.md`](examples.md) — four exchanges, one of them the tool
> refusing. Then [`reference/objection-library.md`](reference/objection-library.md), which is the
> densest file in the repo. `identity.md` and `rules.md` are the operating instructions; open them
> when you're setting it up, not when you're evaluating it.

## Why it exists

The August 2024 practice changes moved two numbers from implicit to spoken: a buyer must sign a written
agreement with your compensation disclosed **before** touring a home, and offers of compensation came
off the MLS. Two rules — and every agent suddenly running five conversations they'd never had to run.

Most agents got a forms class. Nobody got a position.
[`reference/what-changed-2024.md`](reference/what-changed-2024.md) has the sourcing.

## The one rule

> **Whose mouth, whose document.**
>
> Every output is addressed to you, about your business. Nothing explains what a document means.

Interpreting a contract for a client is the unauthorized practice of law in all fifty states, whatever
your licence says. You may fill blanks in your broker's approved form; you may not draft, alter, or
explain it. This repo refuses that consistently enough to be annoying if it's what you came for — and
routes you to the broker or the attorney instead of trailing off.

The case-law sourcing and twelve worked boundary calls: [`reference/the-upl-line.md`](reference/the-upl-line.md).

## Setup — about five minutes

**1.** Create a Claude Project. Add these five files and nothing else:

    identity.md
    rules.md
    skills/<the one you need>.md
    reference/the-upl-line.md
    reference/objection-library.md

**2.** Add your own positions. Open `reference/your-practice/`, fill the three files, ten minutes once:

| File | What it holds |
|---|---|
| `fee-position.md` | Your number, your floor, what the fee buys |
| `agreement-terms.md` | Term, scope, exit — and what your broker lets you vary |
| `what-i-see-locally.md` | What you've actually seen in your own market |

Check what's still blank:

    python3 reference/checks/practice-state.py

You can skip this. Jobs will then ask you for the missing number or label the output framework-only —
they will not invent one.

**3.** Load one skill, not five. Loading all of them blurs five distinct output shapes into one generic
answer. [`skills/README.md`](skills/README.md) routes.

## First-run prompts

| You want | Say |
|---|---|
| Prep a buyer consult | `Buyer consult Thursday. Referral, first-time buyer, hasn't toured with anyone.` |
| Say your fee | `I'm buyer side, 2.5%, and she came back with "her friend's agent does it for 2."` |
| Run the seller compensation talk | `$415k entry-level listing. Seller opened with "I'm not paying some buyer's agent."` |
| Set your terms | `What term and scope should I propose to a cold portal lead?` |
| Think through an inspection | `Inspection flagged the panel. Buyer wants a credit. How do I play it?` |
| See the boundary fire | `Draft me the addendum language for that credit.` → it refuses, then gives you the part that's in scope |

## The five jobs

| # | Job | Prepares |
|---|---|---|
| 1 | [Buyer consultation prep](skills/buyer-consultation-prep.md) | The five-beat sequence, your value in specifics, and the break you should expect |
| 2 | [The fee conversation](skills/fee-conversation.md) | The statement, the pause, percentage vs flat, and the answer to the pushback |
| 3 | [Seller compensation decision](skills/seller-compensation-decision.md) | Four positions, the proceeds reframe, and a recommendation instead of a shrug |
| 4 | [Agreement terms position](skills/agreement-terms-position.md) | Term, scope, and exit as your business position — within what your broker allows |
| 5 | [Post-inspection position](skills/post-inspection-position.md) | Sorting the report, picking the instrument, and reading leverage honestly |

Each skill file is self-sufficient — inputs, method, output format, and its own stop in one file. Lift
one into another tool and it works without the rest of this repo.

## What it refuses

Three refusals, and the first two are runnable:

1. **No client-addressed output, ever.** No letters, no one-pagers, no "send this to your seller."
2. **No interpreting, drafting, or altering any form.** Including "just a starting point," including
   "in plain English so my buyer gets it" — which is the most dangerous version, because it's written
   to be handed over.
3. **No listing data.** No MLS, IDX, aggregator, comps, or local rate statistics, and no estimating
   around the gap. MLS data is licensed per organization; a folder of markdown files can't hold that
   compliance surface and shouldn't pretend to.
   [`reference/no-listing-data.md`](reference/no-listing-data.md)

It also won't tell you what to charge. It helps you say the number you've decided on, and pressure-test
whether you've actually decided.

Who it's **not** for — including the two jobs that stop working if your brokerage sets your positions:
[`reference/who-this-is-not-for.md`](reference/who-this-is-not-for.md).

## Verify it yourself

Every claim on this page has a command behind it. Python 3, standard library, nothing to install:

    python3 reference/checks/skill-shape.py       # five skills, six sections each, every stop declared
    python3 reference/checks/boundary-checks.py   # no client-addressed output; no listing-data inputs
    python3 reference/checks/practice-state.py    # which of your positions are on file

All three exit 0 on a clean checkout. [`VERIFY.md`](VERIFY.md) pairs each claim with its command, and
carries a four-step procedure for **breaking the repo to prove the checks can fail** — a check that
can't fail is decoration.

There are no defect counts here, no coverage percentages, and no adoption numbers, because you
couldn't check any of them.

## Runs alongside a property-side tool. Needs none.

Nothing here requires another tool and nothing installs into one. If you run a property-side assistant
— pricing, listings, buyer matching, showing notes — the two are disjoint: that one establishes what's
true about the house, this one prepares what you'll say about yourself. No shared files, no install
order, no dependency in either direction.
[`reference/alongside-a-property-tool.md`](reference/alongside-a-property-tool.md) maps the seam and
the four handoffs.

## Before you use it

[`DISCLAIMER.md`](DISCLAIMER.md) — not legal, tax, financial, or compliance advice. Your state
commission and your broker outrank every file here. Ask your E&O carrier whether your policy excludes
generative-AI-assisted work.

[`SECURITY.md`](SECURITY.md) — no client names, addresses, or financials in these files. Run
`practice-state.py` before you fork: your filled-in positions are competitive information and the
shipped `[PLACEHOLDER]` versions are the ones meant to be public.

---

MIT licensed — [`LICENSE`](LICENSE). Contributions welcome, especially objections that actually
happened to you: [`CONTRIBUTING.md`](CONTRIBUTING.md).

Built by **The Quiet AI**.
