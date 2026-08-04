---
schema_version: 1
id: kbra-credit-ratings
name: KBRA (Kroll Bond Rating Agency)
provider: Kroll Bond Rating Agency, LLC
url_base: https://www.kbra.com
docs_url: https://www.kbra.com/understanding-ratings
source_tier: FORMAL
purpose:
  - credit-rating-pointer
  - structured-credit-rating
  - clo-abs-rating
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
  - fitch-credit-ratings
status: candidate
added_in: v54
notes_url:
---

## What this source provides

KBRA publishes credit ratings and surveillance across ABS, CMBS, corporates, sovereigns and structured credit (including CLOs), plus publicly listed in-use and proposed methodologies and a regulatory/certifications section. For VaultDiligence the relevant surface is the rating symbol, scale, and date for a vault's underlying structured-credit or fund exposure.

## Source tier rationale

FORMAL by first-matching rule: KBRA is a regulator-recognised NRSRO meeting multiple FORMAL criteria — publicly listed versioned methodologies (in-use and proposed), an attributable corporate maintainer, and records-of-record rating output with a regulatory/certifications page. Not ON-CHAIN; outranks EXPERT as a regulated record.

## When to use it

Use as a credit-rating pointer for F-RAT-006 on VT-3/VT-3a/VT-7/VT-8 vaults with structured-credit or CLO/ABS underlyings (KBRA is strong in CLO/structured ratings where the others may not rate the same tranche), and to corroborate the per-position rating distribution in F-COL-010. Cite symbol, scale, action date.

## When NOT to use it

Do not use for on-chain/contract fields. Do not assume KBRA covers an instrument the major three rate; coverage differs by deal, so absence of a KBRA rating is not evidence against an existing Moody's/S&P/Fitch rating. Absence of any rating remains G3.

## Authentication and rate limits

Homepage, methodology lists, and rating-action alerts are publicly accessible with optional free sign-up; KBRA Premium / Credit Intelligence analytics are subscription-gated. Some research PDFs are free-but-registration-gated. Anonymous reads are the least restricted of the four credit agencies but still rate-limited; treat bulk programmatic pulls as gated and back off on throttling.

Access probe: HTTP 200 on homepage and /understanding-ratings on 2026-06-19 (public; free sign-up for alerts; KBRA Premium analytics subscription-gated)

## Cross-references

Mutual fallback with moodys-credit-ratings, sp-global-credit-ratings, fitch-credit-ratings. Particularly relevant where the underlying is a CLO/ABS tranche (see F-COL-010 CLO look-through precedent). Same-tier conflict flagged I (Investigate).

## Notes

KBRA is the most anonymously accessible credit agency probed and is strong in structured/CLO ratings directly relevant to F-COL-010's CLO-wrapper precedents. Reclassify to active when: (1) the free-vs-Premium boundary is documented so agents know which rating values are anonymously confirmable, (2) KBRA has been cited as the rating pointer on a pack and survived A6 verification, (3) its NRSRO/regulatory-certification status is confirmed from the regulatory page and recorded so the FORMAL classification is anchored to a primary source.

Ratification (2026-06-19): access_mode=pointer-paid; status=candidate. Paid NRSRO subscription; analyst obtains.
