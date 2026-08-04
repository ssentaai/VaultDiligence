---
schema_version: 1
id: moodys-credit-ratings
name: Moody's Ratings
provider: Moody's Corporation (Moody's Investors Service)
url_base: https://www.moodys.com
docs_url: https://ratings.moodys.com/rating-definitions
source_tier: FORMAL
purpose:
  - credit-rating-pointer
  - tokenised-asset-rating
  - underlying-fund-rating
auth: other
access_mode: pointer-paid
freshness_typical: static
freshness_max_trusted: 90d
covers_chains:
  - ALL
covers_field_ids:
  - F-RAT-006
  - F-COL-010
fallback_sources:
  - sp-global-credit-ratings
  - fitch-credit-ratings
  - kbra-credit-ratings
status: candidate
added_in: v54
notes_url:
---

## What this source provides

Moody's publishes long- and short-term credit ratings, rating actions, and credit research on issuers, funds, structured finance, and tokenised assets. For VaultDiligence the relevant surface is whether a vault's underlying tokenised asset or fund carries a Moody's rating, the rating symbol, scale, and date.

## Source tier rationale

FORMAL by first-matching rule: Moody's is a regulator-recognised NRSRO that satisfies multiple FORMAL criteria simultaneously — versioned public rating-definitions/methodologies, an attributable corporate maintainer, and records-of-record output (a rating is an official, citable record). It is not ON-CHAIN (no chain-derived data) and supersedes EXPERT because the output is a regulated record, not informal opinion.

## When to use it

Use as a credit-rating pointer for F-RAT-006 on VT-3/VT-4/VT-8 tokenised-asset and fund vaults where the underlying carries a Moody's rating, and as corroboration of the rating-distribution narrative in F-COL-010. State the exact symbol, scale, and rating date; ratings are point-in-time so cite the action date.

## When NOT to use it

Do not use for on-chain TVL, oracle, or contract-role fields. Do not infer an absence of risk from absence of a Moody's rating — most onchain vaults are unrated (note this as G3, not a finding). Do not treat the homepage marketing copy as rating evidence; the rating detail itself is gated.

## Authentication and rate limits

Homepage and rating definitions are public, but specific issuer/instrument ratings sit behind Moody's CreditView subscription or a sales/demo gate, so anonymous programmatic retrieval of a rating value is not reliable. The operator must either hold a CreditView entitlement or cite an operator-disclosed Moody's report. Treat anonymous fetches of rating detail as G2 naming Moody's CreditView as the gated holder.

Access probe: HTTP 200 on homepage 2026-06-19 (public); rating detail gated behind CreditView subscription / request-a-demo (not anonymously readable)

## Cross-references

Mutual fallback with sp-global-credit-ratings, fitch-credit-ratings, kbra-credit-ratings (same field, different agency). F-RAT-006 already names moodys.com / CreditView search as primary. Same-tier conflict between agencies on the same instrument is flagged I (Investigate), never silently resolved.

## Notes

F-RAT-006 explicitly notes a tokenized CLO fund was not rated by Moody's or S&P at assessment — absence of rating is common and is G3, not a defect. Reclassify to active when: (1) the operator confirms a CreditView entitlement or a repeatable authenticated retrieval path for rating values, (2) Moody's has been cited as the rating pointer on at least one pack and survived A6 verification, (3) the gated-vs-public boundary for the specific instrument types VaultDiligence reviews is documented so agents know when a rating is anonymously confirmable versus G2.

Ratification (2026-06-19): access_mode=pointer-paid; status=candidate. Paid NRSRO subscription; analyst obtains via own access/DDQ. Public rating actions may be free; full reports gated.
