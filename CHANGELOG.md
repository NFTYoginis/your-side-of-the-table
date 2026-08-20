# Changelog

Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). Versions follow
[Semantic Versioning](https://semver.org/spec/v2.0.0.html), read as: **major** = a job added or
removed, **minor** = a skill or reference file changes materially, **patch** = corrections and
source refreshes.

---

## [1.1.0] — 2026-08-20

### Added

- **State routing on the boundary** — [`reference/the-upl-line.md`](reference/the-upl-line.md)
  § *Your state's answer, and what it doesn't change*. Names the three things that genuinely vary —
  what you may say about a form, whether attorney review is customary, what you must disclose — and
  routes each to your broker, your state commission, and an attorney in your state. **It asserts no
  state's rule and adds no state-by-state content.**
- **The condition on that routing, stated everywhere it appears.** Counsel settles what *you* may say
  to a client; it does not change what these files produce. Both refusals are unconditional before and
  after any legal advice. Surfaced in [`rules.md`](rules.md) § Rule 0, in all five skills'
  *Where this stops*, in [`skills/README.md`](skills/README.md), [`README.md`](README.md),
  [`DISCLAIMER.md`](DISCLAIMER.md), and as an FAQ entry on the landing page.
- **[`VERIFY.md`](VERIFY.md) claim 10** — a grep proving all five skills carry the load-bearing
  sentence, with a note saying what a presence check can't tell you.

### Changed

- **[`docs/feature-page-source.md`](docs/feature-page-source.md)** — states up front that finished copy
  returns through the claims gate; § 3 and § 7 rule out "attorney-approved" and lawyer's-blessing
  framings; the closing contact route is now the public repo and its issue tracker rather than a
  sandbox path no reader can open.

### Still open

- **State variation is routed, not documented.** The strict UPL reading still applies everywhere and
  no state's rule is recorded here. That was listed below as *unhandled* at 1.0.0; routing is the part
  this build can honestly do. Contributions documenting material state differences remain welcome, with
  a citation — [`CONTRIBUTING.md`](CONTRIBUTING.md).

---

## [1.0.0] — 2026-08-19

First release.

### Added

- **Five skills**, each self-sufficient — [`skills/`](skills/)
  - `buyer-consultation-prep.md` — the pre-tour sit-down, sequenced
  - `fee-conversation.md` — stating the number, percentage vs flat, pushback
  - `seller-compensation-decision.md` — four positions, the proceeds reframe, a recommendation
  - `agreement-terms-position.md` — term, scope, exit, and the short-first ladder
  - `post-inspection-position.md` — sorting findings, picking the instrument, reading leverage
- **Rule 0** — whose mouth, whose document — [`rules.md`](rules.md)
- **Rule 1** — no listing data — [`reference/no-listing-data.md`](reference/no-listing-data.md)
- **Rule 2** — national aggregates are not a local number
- **The line** — UPL boundary with case-law sourcing and twelve worked calls —
  [`reference/the-upl-line.md`](reference/the-upl-line.md)
- **Objection library** — twelve objections, each with what's true in it and what not to say —
  [`reference/objection-library.md`](reference/objection-library.md)
- **`your-practice/`** — the agent's own fee, terms, and local observations, shipped as placeholders
- **Three checks**, standard library only — [`reference/checks/`](reference/checks/)
- **[`VERIFY.md`](VERIFY.md)** — every self-claim with the command that settles it, including a
  procedure for proving the checks can fail
- **Four worked examples**, one of them a refusal — [`examples.md`](examples.md)
- Governance: [`DISCLAIMER.md`](DISCLAIMER.md), [`SECURITY.md`](SECURITY.md),
  [`CONTRIBUTING.md`](CONTRIBUTING.md), [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md), MIT
  [`LICENSE`](LICENSE)
- **Social image** — `docs/og-image.png` (1200 × 630), rendered from
  [`assets/social/og-1200x630.html`](assets/social/og-1200x630.html). Wording changes are a re-render,
  not a redraw.
- **[`docs/feature-page-source.md`](docs/feature-page-source.md)** — source kit for anyone writing
  about this build elsewhere: positioning lifted verbatim, the five jobs in plain language, the
  constraint story, and an explicit list of claims the repo cannot back.

### Known open items

- **The proof block on the landing page is a placeholder.** No testimonials, no metrics, no adoption
  numbers, and there won't be any until real ones exist with permission to use them.
- **A commission-rate disagreement is recorded, not resolved.**
  [`reference/compensation-landscape.md`](reference/compensation-landscape.md) carries two sources
  that differ by roughly half a point on total commission. Both are shown with provenance rather than
  averaged into a false consensus.
- **State variation is unhandled.** The repo takes the strict UPL reading everywhere. Contributions
  documenting material state differences are welcome — [`CONTRIBUTING.md`](CONTRIBUTING.md).
