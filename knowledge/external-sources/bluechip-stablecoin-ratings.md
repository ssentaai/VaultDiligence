---
schema_version: 1
id: bluechip-stablecoin-ratings
name: Bluechip Stablecoin Ratings
provider: Bluechip (independent stablecoin rating agency; Benjamin Levit, Garett Jones et al.)
url_base: https://bluechip.org
docs_url: https://bluechip.org/smidge
source_tier: EXPERT
purpose:
  - stablecoin-safety-rating
  - peg-mechanism-assessment
  - backing-quality-opinion
auth: none
access_mode: fetch
freshness_typical: static
freshness_max_trusted: 30d
covers_chains:
  - ALL
covers_field_ids:
  - F-RAT-006
  - F-COL-009
fallback_sources:
  - accountable-data-feeds
status: active
added_in: v54
notes_url:
---

## What this source provides

Bluechip publishes letter-grade stablecoin safety ratings (A+ through F) across economic safety, backing type (fiat/crypto/RWA), peg mechanism, and audit status, with a per-coin assessment narrative. The rating logic is its named SMIDGE framework, available as a downloadable document.

## Source tier rationale

EXPERT by first-matching rule: Bluechip is a named for-profit firm with named principals (CEO Benjamin Levit, Chief Economist Garett Jones) producing opinion/analysis ratings of stablecoins. It is not an NRSRO and its output is an analytical opinion, not a regulated record of record, so it falls to EXPERT rather than FORMAL — consistent with the index, which already pre-flags bluechip-ratings as an EXPERT candidate.

## When to use it

Use as a rating pointer for F-RAT-006 on stablecoin-backed vaults to record Bluechip's letter grade and SMIDGE assessment date, and as a named-expert corroborating view on backing quality feeding the collateral-drawdown context of F-COL-009. As EXPERT, it can support E only where the field is opinion-shaped; for factual backing claims it corroborates but downgrades to E(P) without a FORMAL/ON-CHAIN primary.

## When NOT to use it

Do not cite Bluechip as the sole source for a material factual claim about reserves or backing — that requires ON-CHAIN or FORMAL corroboration. Do not use for non-stablecoin vaults. Do not treat the SMIDGE letter grade as equivalent to an NRSRO credit rating.

## Authentication and rate limits

Fully public, no authentication, no API key; the homepage ratings table is anonymously readable. The dedicated /methodology path 404s — the SMIDGE methodology is reached via /about / a downloadable doc, so cite the SMIDGE document URL, not a generic methodology path. No rate limit observed.

Access probe: HTTP 200 on 2026-06-19 (homepage rating table publicly readable, no login); methodology landing /methodology returned 404, SMIDGE doc referenced on /about

## Cross-references

Fallback accountable-data-feeds for the underlying reserve evidence Bluechip opines over (Accountable is FORMAL PoR; Bluechip is the EXPERT opinion layer). For factual backing facts prefer issuer-direct reserves or Accountable over Bluechip. Sits alongside other EXPERT rating pointers (Credora F-RAT-002, Gauntlet F-RAT-005).

## Notes

Bluechip rates publicly and openly, which makes it the most accessible source in this venue, but its EXPERT tier caps factual claims at E(P). Reclassify to active when: (1) the SMIDGE methodology document is located at a stable URL and its version/date is recorded, (2) Bluechip has been cited as a rating pointer on at least one stablecoin pack and survived A6 verification, (3) the rule that Bluechip cannot be the sole source for a material backing fact is reflected in the covered field annotations so agents downgrade correctly.
