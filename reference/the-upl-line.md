# The line

The one boundary this repo is built around. Read it once, properly, and the refusals stop feeling
arbitrary.

---

## The rule in one sentence

**A real-estate licensee may fill in the blanks on an attorney-approved pre-printed form. A licensee may
not draft provisions, alter the form, or explain what any of it means.**

That's the whole thing. Everything below is detail.

## What the courts have actually said

The permission and the prohibition come from the same body of case law, and they're usually stated in
the same breath:

- **Filling blanks is clerical work inside the licensee's role.** Courts have held that agents and
  brokers may complete the blanks in pre-printed agreements that attorneys have prepared or approved —
  party names, property identifiers, dates, amounts. This is treated as memorializing a transaction the
  licensee legitimately negotiated, not as practicing law.
- **Interpreting the same document is not.** Courts have been, in the words of one state's guidance,
  "just as clear in prohibiting them from interpreting the meaning or effect of provisions in those
  agreements."
- **Adding language is not, either** — even to a form an attorney wrote. Additional clauses may not be
  added to a pre-printed contract, and drafting special provisions between other parties falls outside
  the licence.
- **There is no bright-line test** for how far a licensee may modify a form before crossing over. That
  absence is the reason the rule in this repo is *zero* rather than *some*. A standard with no defined
  edge is not a standard you should approach experimentally.

Sources, all public:

- [NY Department of State — Legal Memorandum LI04, *Real Estate Brokers and Salespersons and the Unauthorized Practice of Law*](https://dos.ny.gov/legal-memorandum-li04-real-estate-brokers-and-salespersons-and-unauthorized-practice-law)
- [NC REALTORS® — *When is the "drafting" of contract language considered the unauthorized practice of law?*](https://www.ncrealtors.org/question/when-is-the-drafting-of-contract-language-considered-the-unauthorized-practice-of-law/)
- [NCREC Bulletins — *What is the "Unauthorized Practice of Law"?*](https://bulletins.ncrec.gov/what-is-the-unauthorized-practice-of-law/)
- [Arkansas Real Estate Commission — *The Unauthorized Practice of Law and The Problem of Multiple Client Loyalties*](https://arec.arkansas.gov/news_post/the-unauthorized-practice-of-law-and-the-problem-of-multiple-client-loyalties/)

**These are state-level sources describing a rule that exists in all fifty states in some form, and the
details vary by state.** Some states are materially stricter — attorney-state closing practices,
promulgated-form regimes, and state-specific guidance all move the edges. Your state's commission and
your broker are the authority on your version of this. Nothing here is legal advice about your practice.

## Why this repo takes the strict reading

Three reasons, and the third is the one agents underweight.

**1. There is no defined edge.** If the standard were "you may explain up to a point," a tool could aim
below the point. It isn't, so the tool aims at zero.

**2. The output gets repeated.** Anything this repo tells an agent, the agent may say to a client
tomorrow. An interpretation delivered "just so you understand it yourself" becomes an interpretation
delivered to a buyer, because that's what useful information does. This is the reason
[`../skills/agreement-terms-position.md`](../skills/agreement-terms-position.md) refuses even the
agent-only version of *"what does the protection period clause mean?"*

**3. Insurance.** The build brief for this repo reports that **2026 errors-and-omissions carriers have
begun adding generative-AI exclusions** to real-estate policies — meaning an agent who crosses this
line with AI assistance may be doing it uninsured.

> **Provenance:** that E&O point is supplied by the operator's build brief and is **not independently
> verified in this repo.** Treat it as a prompt to make a phone call, not as a finding. Ask your
> carrier directly: *"Does my current policy exclude claims arising from generative-AI-assisted work?"*
> That is a call worth making regardless of what this file says, and the answer is specific to your
> policy.

## The two tests

Reproduced from [`../rules.md`](../rules.md) Rule 0, because this is the file people arrive at.

**Whose mouth?** Output is written to the agent, about the agent's business. Not to the client.

**Whose document?** You speak about what the agent *does, charges, and proposes*. You never speak about
what the *paper* means, obligates, or produces.

## Worked boundary — twelve calls

The line is easier to hold once you've seen it fall in the middle of similar-looking sentences.

| # | Request | Call | Why |
|---|---|---|---|
| 1 | "How do I say my fee?" | **Fine** | The agent's own business |
| 2 | "What does the compensation clause obligate my buyer to pay?" | **Refuse** | Meaning and effect of a provision |
| 3 | "Should I propose 30 days or 90?" | **Fine** | A business position |
| 4 | "What happens when the 90 days expires?" | **Refuse** | Consequence under the document |
| 5 | "Draft an addendum for the roof credit." | **Refuse** | Drafting |
| 6 | "Should we ask for a credit or a repair on the roof?" | **Fine** | Strategy, not paper |
| 7 | "Put the protection period in plain English for my buyer." | **Refuse — worst case** | Interpreting *and* client-addressed |
| 8 | "Why do I now need an agreement before showing?" | **Fine** | A fact about the agent's practice — see [`what-changed-2024.md`](what-changed-2024.md) |
| 9 | "Can my buyer terminate and keep earnest money?" | **Refuse** | Contract rights, with money attached |
| 10 | "How do I raise the earnest-money question with them?" | **Fine** | Prepping how to *raise* it, not answering it |
| 11 | "Write an email to my seller explaining the change." | **Refuse** | Client-addressed — fails test 1 alone |
| 12 | "Help me decide what to recommend to my seller." | **Fine** | Licensed brokerage judgment |

Note the pairs — 2/1, 4/3, 6/5, 10/9. Each pair is one topic split by the line. The usable move, every
time, is to **hand back the version of the question that sits on the agent's side.** A refusal that
ends in a redirect keeps the agent inside the tool; a bare refusal sends them somewhere with no line
at all.

## Where the answers actually live

| Question type | Who answers it |
|---|---|
| What this form says, does, or obligates | A real-estate attorney in your state |
| How to complete your brokerage's form correctly | Your broker; your brokerage's forms training |
| What your state permits a licensee to do | Your state real-estate commission |
| Whether your policy covers AI-assisted work | Your E&O carrier |
| What to charge, propose, recommend, or argue for | You — and this repo helps you say it |

## One more boundary, adjacent but different

**Never represent compensation as standard, customary, or fixed.** That isn't UPL — it's the antitrust
territory the 2024 practice changes came out of. Compensation is negotiable and always was. The rule
lives in [`../skills/seller-compensation-decision.md`](../skills/seller-compensation-decision.md)
§ *Where this stops*, Stop 2, because that's the job where the temptation is strongest.

---

*Last reviewed 2026-08-19. State-level rules change; this file does not update itself. Your broker and
your state commission outrank it.*
