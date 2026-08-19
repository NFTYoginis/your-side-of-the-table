# Running this alongside a property-side tool

**Nothing in this repo requires another tool, and nothing in it installs into one.** If you have a
property-side assistant, this file maps the seam so the two don't collide. If you don't, skip it —
nothing here is missing.

---

## The split

Two different halves of the same week, and they were never the same job:

| | **Property side** | **This repo** |
|---|---|---|
| **Subject** | The house, the buyer, the deal | The agent's own position |
| **Questions** | What's it worth? Who's it right for? How do I describe it? | What do I charge? What do I propose? What do I argue for? |
| **Inputs** | Market data, comps, property detail, buyer criteria | Your fee, your terms, your read, your client's report |
| **Output** | A listing, a price band, a fit summary, a showing note | A prep sheet you read before a conversation |
| **Who reads it** | The agent, often en route to a client document | The agent. Only ever the agent |

## Concretely, against Realtor Copilot v2

The operator's property-side tool (`NFTYoginis/your-market-realtor`) runs five jobs: **listing
descriptions, buyer–property matching, pricing and comp analysis, showing notes, and local-services
lookup.**

This repo runs five jobs: **buyer consultation prep, the fee conversation, seller compensation
decision, agreement terms position, post-inspection position.**

**Ten jobs, zero overlap.** Not adjacent-but-different — genuinely disjoint. Copilot v2 never asks what
you charge; this repo never asks what the house is worth. Neither can do the other's work, and neither
degrades if the other is absent.

## Where the two touch — four handoffs

Handoffs are conversational, not technical. Nothing is imported, exported, or shared on disk.

| Moment | Property side gives you | This repo does with it |
|---|---|---|
| **Before a listing appointment** | A price band with comp reasoning | The seller compensation decision that follows the number — job 3 |
| **Before a buyer consult** | A fit summary for the homes you'll discuss | The consult sequence and fee statement around it — jobs 1 and 2 |
| **After showings** | Showing notes with friction tags | Context for reading leverage post-inspection — job 5 |
| **Mid-negotiation** | What the property is worth | What you'll argue for and what you'll trade — job 5 |

The direction is consistently the same: **the property side establishes what's true about the house;
this repo prepares what you'll say about yourself.** A pricing memo doesn't tell you how to state your
fee, and a fee brief doesn't tell you what the house is worth.

## The non-dependency, stated properly

- **No shared files.** Neither repo reads, writes, or expects a path in the other.
- **No install order.** Either can be adopted first, or alone, indefinitely.
- **No shared data layer.** Copilot v2 keeps regional market data in its own `region/` files; this repo
  keeps the agent's own positions in [`your-practice/`](your-practice/). Different content, different
  purpose, deliberately not merged — your fee is not a property of your region.
- **No cross-references in operating instructions.** No skill file here tells you to go run something
  else in order to finish. This file is the only place the other tool is named, and it's reference,
  not instruction.

**Separate Projects is the recommended arrangement.** Loading both into one Claude Project blurs two
distinct output contracts — one produces client-bound artifacts like listing copy, the other produces
prep that is never client-bound. Keeping them apart is what keeps Rule 0 legible. If you do combine
them, the rule to carry is: **anything this repo produces stays internal, whatever the rest of the
project is doing.**

## If you don't have a property-side tool

Nothing to do. Every skill file here lists its inputs, and all of them come from you.

The one thing to know: when a job here wants a number about the house — a price, a comp, a repair cost
— it will ask you rather than estimate. That's Rule 1
([`no-listing-data.md`](no-listing-data.md)), and it's the same behavior whether or not you have
another tool running.
