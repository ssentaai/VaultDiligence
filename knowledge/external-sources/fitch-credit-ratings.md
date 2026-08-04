---
schema_version: 1
id: fitch-credit-ratings
name: Fitch Ratings
provider: Fitch Ratings, Inc. (Hearst)
url_base: https://www.fitchratings.com
docs_url: https://www.fitchratings.com/products/rating-definitions
source_tier: FORMAL
purpose:
  - credit-rating-pointer
  - fund-rating
  - structured-finance-rating
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
  - sp-global-credit-ratings
  - kbra-credit-ratings
status: candidate
added_in: v54
notes_url:
---

## What this source provides

Fitch Ratings publishes issuer, fund, and structured-finance credit ratings, rating actions, and rating-definition documentation. For VaultDiligence the relevant surface is whether a vault's underlying fund or tokenised asset carries a Fitch rating, the symbol, scale, and date.

## Source tier rationale

FORMAL by first-matching rule: Fitch is a regulator-recognised NRSRO satisfying multiple FORMAL criteria — published versioned rating definitions and methodologies, attributable corporate maintainer, and records-of-record output. Not ON-CHAIN; outranks EXPERT as the output is a regulated record.

## When to use it

Use as a credit-rating pointer for F-RAT-006 on VT-3/VT-4/VT-8 vaults whose underlying carries a Fitch rating, and as the third independent agency cross-check when Moody's and S&P diverge on the same instrument; corroborates F-COL-010 rating distribution. Cite symbol, scale, action date.

## When NOT to use it

Do not use for on-chain/contract fields. Do not treat a Fitch fund rating as interchangeable with S&P's f-scale without noting the scale difference. Absence of a Fitch rating is G3, not a finding.

## Authentication and rate limits

The site rejected the anonymous fetch entirely on 2026-06-19; rating detail and research are behind free-registration plus subscription tiers. Anonymous programmatic retrieval is unreliable. Cite an operator-disclosed Fitch report or a held entitlement; otherwise G2 naming Fitch as the gated holder.

Access probe: Fetch blocked to anonymous client on 2026-06-19 (WebFetch returned 'unable to fetch from www.fitchratings.com' — site rejects the anonymous client)

## Cross-references

Mutual fallback with moodys-credit-ratings, sp-global-credit-ratings, kbra-credit-ratings. Same-tier conflict among agencies on one instrument is flagged I (Investigate), never resolved silently.

## Notes

Fitch is the weakest-probed of the four credit agencies here (fully blocked to anonymous fetch), so retrieval will most often run through operator disclosure rather than direct fetch. Reclassify to active when: (1) an authenticated or operator-entitlement retrieval path is confirmed and the anonymous block is documented as expected, (2) Fitch has been cited on a pack as the rating pointer and survived A6 verification, (3) its fund/structured-finance scales are documented for agents so citations state the correct scale.

Ratification (2026-06-19): access_mode=pointer-paid; status=candidate. Paid NRSRO subscription; analyst obtains. Probe: fetch blocked to anonymous 2026-06-19.
