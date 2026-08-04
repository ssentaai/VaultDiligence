---
schema_version: 1
id: sipc-member-list
name: SIPC Member List
provider: Securities Investor Protection Corporation (SIPC)
url_base: https://www.sipc.org
docs_url: https://www.sipc.org/list-of-members
source_tier: FORMAL
purpose:
  - sipc-membership-verification
  - investor-protection-coverage-confirmation
auth: none
access_mode: pointer-gated
freshness_typical: weekly
freshness_max_trusted: 30d
covers_chains:
  - ALL
covers_field_ids:
  - F-CUS-001
  - F-CUS-005
fallback_sources:
  - finra-brokercheck
status: candidate
added_in: v54
notes_url:
---

## What this source provides

SIPC maintains the authoritative list of member broker-dealers whose customers are covered by SIPC protection (up to 500,000 USD per customer, including 250,000 USD cash, on broker failure). Used to confirm whether a named prime broker is a SIPC member, establishing the base investor-protection floor before excess-SIPC analysis.

## Source tier rationale

FORMAL. SIPC is a congressionally created non-profit and the member list is a record of record for who is and is not covered. Meets FORMAL on attributable maintainer and records of record. Not ON-CHAIN; not EXPERT (membership status, not analysis).

## When to use it

Primary for the SIPC-membership half of F-CUS-001 and the coverage floor for F-CUS-005, for VT-3/VT-4/VT-8 vaults with a US prime broker. Pair with the prime brokerage agreement and the broker's excess-SIPC disclosure for the full coverage picture.

## When NOT to use it

Not for excess-SIPC, fidelity-bond, or E&O amounts (broker disclosures, not on the list; F-CUS-005 primary). Not for the insolvency recovery process/timeline (F-CUS-006, a legal-opinion field). Not for non-US brokers; SIPC covers US-registered broker-dealers only.

## Authentication and rate limits

Public, no auth, no key. The member list is published on sipc.org; the list-of-members route returned HTTP 404 to anonymous WebFetch during probing while the homepage returned 200, so confirm the live route at retrieval time rather than hard-coding it. No operator credential required.

Access probe: Homepage HTTP 200 on 2026-06-19; list-of-members route HTTP 404 to anonymous WebFetch on 2026-06-19

## Cross-references

finra-brokercheck (companion regulatory-standing lookup for the same firm); fields F-CUS-005 and F-CUS-006 (adjacent coverage and insolvency fields this list does not answer).

## Notes

Membership confirms only that SIPC's statutory protection applies; it does not speak to solvency, segregation, or rehypothecation terms. Base SIPC coverage is small relative to institutional position sizes, so read F-CUS-005 excess coverage alongside it. Reclassify to active when: (1) the live member-list retrieval route is confirmed (the list-of-members path probed 404 anonymously and must be resolved); (2) VaultDiligence has cited the member list as primary source on at least one pack and A6 confirmed it; (3) the relationship between the published list and FINRA registration has been checked for at least one firm for consistency.

Ratification (2026-06-19): access_mode=pointer-gated; status=candidate. ROUTE: homepage 200 but member-lookup route 404 to anonymous (2026-06-19) — confirm the SIPC member-database deep route before active.
