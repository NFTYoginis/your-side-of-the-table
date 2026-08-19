# Changelog

Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). Versions follow
[Semantic Versioning](https://semver.org/spec/v2.0.0.html), read as: **major** = a job added or
removed, **minor** = a skill or reference file changes materially, **patch** = corrections and
source refreshes.

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

### Known open items

- **`docs/og-image.png` not yet present.** OG meta tags ship pointing at it; social shares fall back to
  text-only previews until the file lands. Deliberate — meta tags first, image when it exists.
- **The proof block on the landing page is a placeholder.** No testimonials, no metrics, no adoption
  numbers, and there won't be any until real ones exist with permission to use them.
- **A commission-rate disagreement is recorded, not resolved.**
  [`reference/compensation-landscape.md`](reference/compensation-landscape.md) carries two sources
  that differ by roughly half a point on total commission. Both are shown with provenance rather than
  averaged into a false consensus.
- **State variation is unhandled.** The repo takes the strict UPL reading everywhere. Contributions
  documenting material state differences are welcome — [`CONTRIBUTING.md`](CONTRIBUTING.md).
