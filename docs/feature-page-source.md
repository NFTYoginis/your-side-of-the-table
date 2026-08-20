# Feature-page source kit — Your Side of the Table

**For marketing, writing a feature page on thequietai.com. This is source material, not a page.**

> **Before this page publishes, the finished copy goes back through the claims gate.** Every line here
> is traceable to a file in the repo. Anything added on the way to the site is not, and that is the
> part that needs checking.

Everything below is traceable to a file in this repo — the trace table at the bottom names which. If
you need a claim that isn't here, it's probably in *§ What this repo cannot back*, which lists the
things that would be false. Those aren't stylistic preferences; the repo declines them on its own
public page, so a site page that quietly adds them turns the repo into evidence against us.

**Working rule:** anything on the site page should survive a reader clicking through to the repo.

*Prepared 2026-08-19 by specialist-builder; revised 2026-08-20 (claims-gate note above, public contact
route in § 8, jurisdiction routing in § 3 and § 7). This file lives in `docs/`, so GitHub Pages serves
it publicly alongside the landing page — it's written to cost nothing if someone finds it.*

---

## 1. Positioning

**Lift these. They're the repo's own words, not new copy.**

The one-line version — the repo's own headline, verbatim:

> **Ten minutes of prep before the conversation where you say your number out loud.**

The what-it-is version, verbatim:

> A prep instrument for the five conversations a residential agent now has to run out loud.

The who-it's-for version, verbatim:

> **A licensed residential agent, working the buyer side, the listing side, or both.** Typically one
> to fifteen years in. They came up in a market where the fee was on the MLS and the buyer signed
> nothing before the third house, and they have been improvising every one of these conversations
> since August 2024. Their brokerage gave them a forms class, not a position.

And the line that does the most work in one sentence, verbatim:

> They already know their market. They do not know how to say their number without flinching.

**Why it exists**, if the page needs a paragraph of context — verbatim from the repo's landing page:

> August 2024 moved two numbers from implicit to spoken — and handed every agent five conversations
> nobody trained them for.

The two rules behind that, both sourced to the National Association of REALTORS® in the repo: a buyer
must sign a written agreement with the agent's compensation disclosed **before** touring a home, and
offers of compensation came off the MLS. One clarification the repo is careful about and the page
should be too — those rules **do not require an agency agreement and do not dictate any type of
relationship.** An agent telling a buyer "you have to become my client to see a house" has overstated
it, and so would we.

---

## 2. The five jobs, in plain language

For a reader who has never sold a house and will never clone a repo. Each is a conversation an agent
now has to run, and what they walk away holding.

**1. The pre-tour sit-down.**
Before an agent can show a buyer a single home, there now has to be a conversation and a signed
agreement. Most of them go wrong on order, not on content — the agent leads with the paperwork, so
the buyer experiences the whole meeting as a signature request. This lays out the sequence: their
situation first, how you work second, what you charge third, the paperwork fourth. The agent walks in
with a running order and the one objection this particular buyer is most likely to raise.

**2. Saying the fee out loud.**
The number used to sit on a listing service. Now it comes out of the agent's mouth in a first meeting.
The technique is three moves — state it, stop talking for two seconds, then say what it buys — and the
pause is the part almost nobody can do. Also covers the choice between charging a percentage and
charging a flat fee, including the awkward one: on the buyer's side, a percentage means the agent
earns more the more their client spends, and sharp buyers notice. The agent walks away with the
sentence, the silence, their walk-away number, and an answer to the pushback that's coming.

**3. Helping a seller decide about the other side's fee.**
Sellers used to offer compensation to the buyer's agent almost automatically. Now it's a decision, and
they ask their listing agent what to do. Most agents answer "it's totally up to you," which is
technically true and professionally empty. This turns it into four real options and reframes the money
— it isn't paying the other side's help, it's the same question as a closing-cost credit or a rate
buydown: will you spend some of your proceeds to widen the pool of buyers who can actually afford to
write on this house? The agent walks in with a recommendation and the questions that get the seller
to their own answer.

**4. Deciding what to ask for, before anyone opens a form.**
How long the agreement runs, how much of the search it covers, and whether the client can walk away.
Agents default to whatever was pre-printed and then can't defend it. Treated here as three separate
business decisions rather than one — with a case for asking small at the first meeting and earning the
extension, and for handing the client the right to cancel, which costs almost nothing and buys a lot
at the moment of signing.

**5. Thinking through a repair request.**
The inspection comes back with forty items and the buyer wants to ask for all of them. Three items is
a request; nineteen is a renegotiation and the other side knows it. This sorts the report into what
actually matters, what every house of that age has, and what's boilerplate — then picks between asking
for a repair, a cash credit, a price cut, or nothing, and reads honestly how much leverage there
actually is. It stops before any document gets written. That boundary is the point, not a limitation.

**One framing worth keeping:** these are five conversations, not five features. The product is the ten
minutes before each one.

---

## 3. The constraint story

**This is the most interesting thing about the build and the part you'd otherwise never find.** It
refuses three things, on purpose, and says so on its own landing page.

### It never writes anything addressed to the client

No emails, no letters, no one-pagers, no "send this to your seller." Every word it produces is
addressed to the agent. The repo's whole rule is four words — **whose mouth, whose document** — and
the first half is this one.

This is unusual enough to lead with. Most tools in this category are judged by what they'll write for
you. This one is recognisable by what it won't.

### It never explains what a contract means

An agent may fill in the blanks on their brokerage's approved form. They may not draft it, alter it,
or explain what it means — that's the unauthorized practice of law in all fifty states, whatever their
real-estate licence says. Courts have been consistent about both halves, and there is **no bright-line
test** for how far is too far, which is exactly why the tool's answer is *none* rather than *some*.

The repo cites state real-estate commissions and REALTOR® association guidance for this, linked rather
than paraphrased.

There's a second reason it holds the line even for the agent's own private understanding: anything the
tool explains, the agent may repeat to a client tomorrow. So "just tell me what this clause means, for
me" gets refused too.

**What makes the refusal usable rather than annoying:** it always ends in a redirect. It names the
line, sends the question to the broker or a real-estate attorney, and then delivers the part of the
request that was in scope. The repo ships a worked example of exactly this — an agent asks for
addendum wording and for what the inspection contingency permits, gets both refused, and still walks
away with the full strategy sheet. The repo's own words for why: a refusal that leaves the agent with
nothing is one they'd route around, to a general-purpose chatbot that will happily draft the addendum.

**One thing the page must not turn into a permission slip.** Some of this genuinely varies by state —
what an agent may say about a form, whether attorney review is customary where they work, what their
state requires them to disclose. The repo names those three as varying and routes them to the agent's
own broker and attorney; it does not answer them, and it carries no state-by-state content. The part
worth getting right in copy: that routing changes **what the agent may say**, and changes **nothing
about what the tool produces.** No attorney's answer unlocks client-addressed output. If a line on the
page could be read as *get your lawyer's blessing and it'll write the letter*, it has inverted the
build's one rule. The safe framing is the true one — it tells you where to ask, and it doesn't move.

### It runs on no licensed listing data

No MLS, no IDX, no aggregator, no comps, no sold prices, no local rate statistics — and it won't
estimate around the gap either.

The reason is concrete rather than philosophical: MLS data is licensed per organization. Every MLS is
its own contract even when access is brokered through an aggregator, national-scale feeds run into the
low six figures annually, and IDX access carries standing refresh and audit obligations that never
end. A folder of text files cannot hold that compliance surface and shouldn't pretend to. A tool that
quietly cached listing data would put its user in breach of agreements the user personally signed.

The elegant part, and worth a sentence on the page: **none of the five jobs ever needed it.** They're
position problems, not data problems. The agent already holds every input.

### It won't tell an agent what to charge

Related, and a good closing beat for this section. It has no opinion on anyone's fee. It helps an agent
say the number they've decided on — and if they haven't decided, surfacing that is the finding rather
than something to paper over with a plausible-sounding rate.

---

## 4. The proof block — copy exactly

**This is the single most useful paragraph in the repo for a site page. Reproduce it verbatim.** It's
currently live on the repo's landing page under the heading *"What this page doesn't claim."*

> There are no testimonials on this page, no user counts, no defect or coverage numbers, and no
> "trusted by" row. Not because they'd be unflattering — because you couldn't check any of them, and
> the repo's `VERIFY.md` treats an unverifiable claim as a bug.

Two notes on using it:

- **"This page" travels.** The phrasing refers to whatever page it sits on, so it works unchanged on
  the site. Don't rewrite it to "the repo" — that would make it a statement about somewhere else and
  quietly excuse the site page from the same standard.
- **The follow-on list is part of the block** and can come with it if there's room. Verbatim:

> What you can check instead, in about two minutes:
> - Read `examples.md` — four worked exchanges, one of them the tool refusing a request and then
>   delivering the part that was in scope.
> - Run the three checks above on a clean clone.
> - Break it four ways with the procedure in `VERIFY.md` and watch each check catch it.
> - Read the sources in `reference/the-upl-line.md` — state real-estate commissions and REALTOR®
>   associations, linked, not paraphrased.

If the site page keeps that list, "the three checks above" needs something above it — either the
three commands, or a rewrite to "the three checks in the repo." That's the one edit this block needs
to survive the move, and it's a link-target problem, not a claim problem.

**The self-verification angle is a legitimate proof story on its own.** The repo ships three small
scripts that check its own rules — that nothing it produces is addressed to a client, that every job
declares where it stops, that no job depends on listing data — plus a documented procedure for
deliberately breaking the repo four ways to prove the checks actually fail when they should. A check
that can't fail is decoration. That's a stronger claim than a testimonial and it's one a skeptical
reader can run themselves in about two minutes.

---

## 5. Asset status

**The og-image is done and live.** It was rendered during this dispatch, so the "briefed and pending"
status in the original brief is out of date — flagged here so nobody waits on it or, worse, treats it
as missing and commissions a second one.

| Asset | Status | Where |
|---|---|---|
| Social/OG image, 1200 × 630 PNG, 73 KB | **Live, HTTP 200** | `https://nftyoginis.github.io/your-side-of-the-table/og-image.png` |
| Repo landing page | **Live, HTTP 200** | `https://nftyoginis.github.io/your-side-of-the-table/` |
| Public repo | **Live, public** | `https://github.com/NFTYoginis/your-side-of-the-table` |

The OG image is a two-column split — quoted lines an agent may say on the left, the same lines struck
through on the right where they'd cross into contract interpretation. It re-renders from an HTML
source in the repo rather than being redrawn, so **wording changes are cheap.** If the feature page
wants a variant with different example lines, that's a small ask, not a design job.

**No other assets exist.** No screenshots, no product video, no logo lockup specific to this build, no
photography. If the page needs any of those, they don't exist yet and this file is not the place they
came from.

---

## 6. Trace table — every claim to its file

Marketing shouldn't have to take this kit's word for anything. Section by section:

| Kit section | Backed by |
|---|---|
| Positioning lines | `README.md` (headline), `identity.md` (§ You are, § Who you serve) |
| "Why it exists" + the two 2024 rules + the no-agency-required clarification | `reference/what-changed-2024.md`, which links four NAR sources |
| Job 1 — pre-tour sit-down, the sequence | `skills/buyer-consultation-prep.md` |
| Job 2 — the fee, the pause, percentage vs flat | `skills/fee-conversation.md` |
| Job 3 — four positions, the proceeds reframe | `skills/seller-compensation-decision.md` |
| Job 4 — term, scope, exit as three decisions | `skills/agreement-terms-position.md` |
| Job 5 — sorting the report, choosing the instrument | `skills/post-inspection-position.md` |
| "Whose mouth, whose document"; the refusal language | `rules.md` § Rule 0 |
| UPL framing, no-bright-line-test, the case-law sourcing | `reference/the-upl-line.md` (four linked state/association sources) |
| What varies by state, who to ask, and that counsel doesn't re-open the refusal | `reference/the-upl-line.md` § *Your state's answer, and what it doesn't change*; `rules.md` § Rule 0; each skill's § *Where this stops* |
| The worked refusal that still delivers | `examples.md` § Example 3 |
| MLS licensing, six figures, IDX obligations | `reference/no-listing-data.md` |
| "None of the five jobs ever needed it" | `reference/no-listing-data.md` § Why it doesn't matter here |
| "Won't tell you what to charge" | `skills/fee-conversation.md` § Where this stops |
| Proof block, verbatim | `docs/index.html` § Proof — the `.noclaim` block |
| The three checks and the break-it procedure | `reference/checks/`, `VERIFY.md` |
| Asset status | `docs/og-image.png`, `assets/social/og-1200x630.html`, live HTTP checks |

---

## 7. What this repo cannot back — do not write these

Flagged rather than supplied. Each one is either unverifiable or contradicted by a file in the repo.

**Anything about adoption.** No user counts, no install numbers, no "trusted by," no agent logos, no
"join hundreds of agents." **This build has zero users.** The repo declines these on its own page for
a stated reason, and the site contradicting it is the specific failure worth avoiding.

**Anything about outcomes.** No "close more deals," no "win more listings," no "stop losing clients
on price," no "protect your commission." Nothing has been measured. There is no study, no cohort, no
before-and-after.

**Anything about time saved.** "Ten minutes of prep" is a description of what the reader does, and
it's the repo's own line. "Saves you three hours a week" is a different claim and there's nothing
behind it.

**Anything implying legal protection or compliance.** This is the most dangerous available claim and
the most tempting, because the build is *about* a legal boundary. Do not write "keeps you compliant,"
"UPL-safe," "protects your licence," or "audit-proof." The repo's own disclaimer says the opposite in
plain terms: it is not legal, tax, financial, or compliance advice, and a state commission and the
agent's broker outrank every file in it. The honest version — *"it refuses to cross the line and tells
you where the line is"* — is both true and a better line anyway.

**Anything implying a lawyer's sign-off changes it.** Also out: "attorney-approved," "lawyer-reviewed,"
"cleared for your state," "compliant in all fifty states," and any variant of *check with your attorney
and you're good to go.* The repo routes state questions to the agent's own counsel **because** it
doesn't know any state's rule, and its two refusals don't move once counsel answers. Copy implying
otherwise sells the opposite of what was built — and it's the one misread this file exists to prevent.

**Testimonials or quotes from agents.** None exist. Not real, not composite, not "representative."

**Efficacy claims about the language itself.** No "proven scripts," no "battle-tested objection
handling." The objection library is a structured argument, not a tested one, and the repo asks working
agents to contribute what actually happened to them precisely because it doesn't have that data yet.

**Commission statistics beyond one figure.** If the page wants a market stat, use only this one: **in
2025, sellers offered buyer-agent compensation in roughly 70% of transactions.** Two independent
sources in the repo agree on it, and it's the number that makes the whole build make sense — the
practice changed from automatic to decided, and most sellers, having decided, still offer. **Do not
use the total-commission or per-side rate figures.** The repo records a genuine disagreement there —
its brief-supplied total of ~5.5–5.7% sits about half a point above the ~5.0–5.2% that public
secondary sources report — and it deliberately shows both rather than averaging them into a false
consensus. A site page that picks one silently would be publishing a contested number as settled.

**Pricing, availability, or roadmap.** Not in the repo, in any form.

**Anything about the property-side tool as a bundle or upsell.** The repo is careful that the two
tools have no dependency in either direction, and says so. "Works even better with…" is fine and
true; anything implying you need both is not.

---

## 8. If you need something that isn't here

The rule this kit runs on is the same one the repo runs on: **if a claim can't be traced to a file,
it doesn't ship.** If the page needs something in § 7, that's a real request — it just needs evidence
first, which usually means the build getting used by someone. Send it back rather than writing around
it.

**Where to take a question.** Read the file first — § 6 names one for every claim above, and it settles
most of them:
[github.com/NFTYoginis/your-side-of-the-table](https://github.com/NFTYoginis/your-side-of-the-table).

If reading it doesn't settle it, **open an issue on the repo**:
[github.com/NFTYoginis/your-side-of-the-table/issues](https://github.com/NFTYoginis/your-side-of-the-table/issues).
That's the route for a factual question, a claim you can't trace, or a correction — and it works
whether you're writing the feature page or you found this file by accident. Answers land in public,
where the next person reading this can see them.

What a useful correction looks like:
[`CONTRIBUTING.md`](https://github.com/NFTYoginis/your-side-of-the-table/blob/main/CONTRIBUTING.md).
