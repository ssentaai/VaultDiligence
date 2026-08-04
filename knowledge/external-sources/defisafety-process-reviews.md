---
schema_version: 1
id: defisafety-process-reviews
name: DeFiSafety Process-Quality Reviews
provider: DeFiSafety
url_base: https://www.defisafety.com
docs_url: https://www.defisafety.com/methodology
source_tier: EXPERT
purpose:
  - process-quality-review
  - security-process-assessment
auth: rate-limited-anonymous
access_mode: pointer-gated
freshness_typical: static
freshness_max_trusted: 30d
covers_chains:
  - ALL
covers_field_ids:
  - F-SEC-012
  - F-SEC-013
  - F-SEC-006
  - F-SEC-010
  - F-RAT-001
fallback_sources:
  - immunefi-bug-bounty-programs
  - sherlock-audit-registry
status: candidate
added_in: v54
notes_url:
---

## What this source provides

Published process-quality reviews scoring a protocol's documentation, testing, audit, and access-control practices against a stated methodology.

## Source tier rationale

EXPERT, not FORMAL: DeFiSafety is a named firm producing an assessment/opinion (a quality review), not records of record. Methodology is published, but the output is an expert judgement — evidence ceiling E(P) for factual claims. Collapsed from two conflicting proposals (one EXPERT, one FORMAL) into a single EXPERT entry: a source has exactly one tier.

## When to use it

Corroborating evidence for security/process fields (F-SEC-006/010/012/013) and as a rating pointer (F-RAT-001). Never the sole source for a material fact.

## When NOT to use it

Not as standalone E for any material claim; corroborate with ON-CHAIN/FORMAL. Not current if the protocol changed after the review date.

## Authentication and rate limits

Reviews are free to read in-browser but the site returns HTTP 403 to anonymous programmatic fetch (2026-06-19) — analyst opens it (pointer-gated).

Access probe: HTTP 403 to anonymous WebFetch 2026-06-19 (free to read in-browser)

## Cross-references

Collapsed from defisafety-process-reviews (EXPERT) and defisafety-process-quality-reviews (FORMAL). Pairs with immunefi-bug-bounty-programs and sherlock-audit-registry.

## Notes

Registered v54 (Fix 70). Candidate + pointer-gated (403 anonymous). Tier set to EXPERT (single tier per source). Reclassify to active when: (1) a clean access route is confirmed; (2) cited on a pack with A6 confirmation; (3) F-SEC cross-refs applied.
