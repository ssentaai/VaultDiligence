---
schema_version: 1
id: sp-global-credit-ratings
name: S&P Global Ratings
provider: S&P Global Inc. (S&P Global Ratings)
url_base: https://www.spglobal.com/ratings/en/
docs_url: https://www.spglobal.com/ratings/en/about/understanding-credit-ratings
source_tier: FORMAL
purpose:
  - credit-rating-pointer
  - fund-credit-quality-rating
  - underlying-portfolio-rating
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
  - moodys-credit-ratings
  - fitch-credit-ratings
  - kbra-credit-ratings
status: candidate
added_in: v54
notes_url:
---

## What this source provides

S&P Global Ratings publishes issuer and instrument credit ratings, fund credit-quality ratings (the 'f' scale, e.g. AA+f) and volatility ratings (e.g. S1+), rating actions and methodology. For VaultDiligence the relevant surface is the rating symbol, scale, and date for a vault's underlying tokenised asset or fund.

## Source tier rationale

FORMAL by first-matching rule: S&P is a regulator-recognised NRSRO meeting several FORMAL criteria at once — published versioned methodologies and rating definitions, attributable corporate maintainer, and records-of-record output. Not ON-CHAIN; outranks EXPERT because a rating is an official record, not informal opinion.

## When to use it

Use as a credit-rating pointer for F-RAT-006 on VT-3/VT-4/VT-8 vaults whose underlying fund/asset carries an S&P rating (the related tokenized treasury fund AA+f / S1+ precedent is the canonical example), and to corroborate the rating distribution in F-COL-010. Cite the exact fund-credit-quality and volatility symbols and the action date.

## When NOT to use it

Do not use for on-chain or contract-level fields. Do not equate the fund-credit-quality 'f' scale with a traditional issuer rating — they are distinct scales; state which. Do not present absence of an S&P rating as a finding (it is G3 for most onchain vaults).

## Authentication and rate limits

The ratings site returned HTTP 403 to anonymous fetch, and full rating detail / research is subscription-gated (S&P Capital IQ / RatingsDirect). Anonymous retrieval of a specific rating value is unreliable; cite an operator-disclosed S&P report or a held entitlement, otherwise classify as G2 naming S&P RatingsDirect as the gated holder.

Access probe: HTTP 403 to anonymous WebFetch on 2026-06-19 (ratings.spglobal.com / spglobal.com/ratings blocks anonymous client)

## Cross-references

Mutual fallback with moodys-credit-ratings, fitch-credit-ratings, kbra-credit-ratings. F-RAT-006 references the S&P AA+f/S1+ precedent directly. Same-tier disagreement between agencies on one instrument is flagged I (Investigate).

## Notes

The fund-credit-quality ('f') and volatility ('S') scales are S&P-specific and must not be conflated with letter issuer ratings from other agencies. Reclassify to active when: (1) a repeatable authenticated retrieval path or operator entitlement is confirmed (the anonymous 403 must be resolved), (2) S&P has been cited as the rating pointer on a pack and survived A6 verification, (3) the distinction between the f-scale, the S-scale, and issuer ratings is documented for agents so citations state the correct scale.

Ratification (2026-06-19): access_mode=pointer-paid; status=candidate. Paid NRSRO subscription; analyst obtains under own access or via DDQ. CONNECTED PARTY: S&P Global is an investor in Credora (RedStone) — weigh the rater's affiliation. Probe: HTTP 403 to anonymous 2026-06-19.
