# No listing data

Rule 1, with the reasoning. This repo runs on what the agent already owns and nothing else.

---

## The rule

**No MLS records. No IDX feed. No aggregator data. No comps, sold prices, days-on-market, inventory
counts, or local rate statistics.**

Not "not yet." Not "unless you have a licence." This repo has no data layer and is not designed to
acquire one.

## Why — the licensing reality

MLS data is licensed **per organization**. There are hundreds of MLSs in the United States, and access
to each is a separate contractual relationship:

- **Every MLS requires its own contract**, including when access is brokered through an aggregator. An
  aggregator simplifies the plumbing; it does not collapse the agreements.
- **National-scale feeds run into the low six figures annually.** That is the actual price of the
  thing agents assume a tool can just have.
- **IDX access carries standing obligations** — refresh frequency requirements, display rules, and
  audit exposure — that continue for as long as the data is held. They are not a one-time integration
  cost; they are a permanent operational commitment.

*(Licensing terms above as characterized in the operator's build brief, 2026-08-19. The direction is
not controversial — per-MLS contracting and IDX display obligations are standard — but confirm
specifics with your own MLS before relying on them.)*

A folder of markdown files cannot hold that compliance surface, and shouldn't pretend to. A tool that
quietly scraped or cached listing data would put its user in breach of agreements *the user personally
signed*, which is a strange thing to do to somebody you're trying to help.

## Why it doesn't matter here

The five jobs never needed it. Look at what each one actually runs on:

| Job | Runs on |
|---|---|
| Buyer consultation prep | The agent's process, fee, and terms |
| Fee conversation | The agent's number and what they do for it |
| Seller compensation decision | The seller's situation and the agent's read of their own market |
| Agreement terms position | The agent's business position and their broker's ceiling |
| Post-inspection position | The client's own inspection report and the agent's read of leverage |

**None of these is a data problem.** They are position problems. The agent already holds every input.
That's not a limitation worked around — it's why this job family was the right one to build here.

The property side genuinely does want market data, which is exactly why it is a different tool. See
[`alongside-a-property-tool.md`](alongside-a-property-tool.md).

## What this means in practice

**Refuse and redirect:**

> **"I don't carry listing data — no MLS, no comps, no market feed. That keeps this thing legal to run
> and honest about what it knows. Tell me what you're seeing in your own market and I'll work from
> that."**

**Never do these, even when they'd be helpful:**

- Estimate a local rate. *"Buyer-side is probably around 2.5% in your area"* is a fabrication with a
  hedge on it, and the agent may repeat it to a seller.
- Estimate days-on-market, absorption, or inventory.
- Estimate a repair cost. Contractors bid; the internet guesses. See
  [`../skills/post-inspection-position.md`](../skills/post-inspection-position.md).
- Recall a specific property, sale, or listing from memory. A plausible address is worse than no
  address.
- Treat the national aggregates in [`compensation-landscape.md`](compensation-landscape.md) as a local
  answer. They are dated national context, explicitly fenced in that file.

**Where local knowledge does live:**
[`your-practice/what-i-see-locally.md`](your-practice/what-i-see-locally.md) — the agent's own
first-hand observations, written down by them. It is the only local source this repo will ever have,
and it's a better one than a feed, because the agent was in the room.

## The one thing an agent can do about it

If an agent wants their own market data in the conversation, the move is to **write down what they've
seen** — not to wire in a feed. Ten lines in `what-i-see-locally.md` about what sellers in their
price band have actually offered over the last quarter outperforms any national statistic for the
conversation they're about to have, and it carries no licence, no audit, and no annual fee.
