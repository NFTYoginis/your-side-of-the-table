# Skills

Five skills, plus this router. **Load one skill.**

Each is self-sufficient — when to use it, what it runs on, how to start from nothing, how to think,
what it produces, and where it stops, all in the same file. You can lift a single one into a Claude
Project, a system prompt, or another tool, and it works without the rest of this repo.

Loading all five at once wastes context and blurs five distinct output shapes into one generic answer.

---

| The conversation you're about to have | Load |
|---|---|
| A buyer consult — the sit-down before you show anything | [`buyer-consultation-prep.md`](buyer-consultation-prep.md) |
| Saying your fee, or answering pushback on it | [`fee-conversation.md`](fee-conversation.md) |
| A seller deciding whether to offer buyer-agent compensation | [`seller-compensation-decision.md`](seller-compensation-decision.md) |
| What term, scope, and exit you propose | [`agreement-terms-position.md`](agreement-terms-position.md) |
| A repair request, before anyone drafts anything | [`post-inspection-position.md`](post-inspection-position.md) |

**If two apply:** run the one that's happening this week. Consults commonly chain 1 → 2 → 4; run them
in that order rather than merging them, because they produce three different prep sheets and you'll
use them at three different moments in the meeting.

## What every skill shares

| Section | What it's for |
|---|---|
| **When to use** | Including what it is *not* for |
| **Runs on** | Declared inputs, each with a source. All of them yours — no listing data, ever |
| **The two questions** | What to ask when the agent opens with nothing |
| **Method** | The reasoning, numbered |
| **Output format** | The artifact. One screen |
| **Where this stops** | The boundary, with a Fine / Over-the-line table and the refusal in quotes |
| **If you're missing something** | What to do about a blank rather than filling it |

Verify that shape holds:

    python3 ../reference/checks/skill-shape.py

## The rule that outranks every skill

Rule 0, from [`../rules.md`](../rules.md): **every output is addressed to the agent, and nothing
explains what a document means.** Each skill restates its own version in *Where this stops*. The
reasoning, the case law, and twelve worked boundary calls are in
[`../reference/the-upl-line.md`](../reference/the-upl-line.md).
