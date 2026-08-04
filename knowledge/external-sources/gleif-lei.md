---
schema_version: 1
id: gleif-lei
name: GLEIF LEI Records
provider: Global Legal Entity Identifier Foundation
url_base: https://api.gleif.org/api/v1
docs_url: https://www.gleif.org/en/lei-data/gleif-api
source_tier: FORMAL
purpose:
  - legal-entity-identifier
  - entity-verification
  - parent-relationship
auth: none
access_mode: pointer-gated
freshness_typical: daily
freshness_max_trusted: 30d
covers_chains:
  - ALL
covers_field_ids:
  - F-ENT-001
  - F-ENT-002
  - F-ENT-003
  - F-ENT-005
  - F-ENT-006
  - F-ENT-050
  - F-ENT-062
fallback_sources:
  - opencorporates-registry
  - uk-companies-house
status: candidate
added_in: v54
notes_url:
---

## What this source provides

Authoritative LEI records: legal name, registered address, jurisdiction, registration authority, entity status, and direct/ultimate parent relationships, via the public GLEIF API.

## Source tier rationale

FORMAL: regulator-affiliated foundation producing records of record. Records-of-record + attributable maintainer satisfy FORMAL.

## When to use it

Entity identity and jurisdiction confirmation (F-ENT-001/002/003/005/006), fund-admin entity (F-ENT-050), and SOC/entity attestation linkage (F-ENT-062).

## When NOT to use it

Not for operational or financial facts. LEI absence is itself a gap signal, not proof of non-existence.

## Authentication and rate limits

Public API at api.gleif.org/api/v1/lei-records (free). ROUTE-TODO: the lei-look-up app route 404'd to anonymous fetch on 2026-06-19; confirm the exact API query route before promoting to fetch/active.

Access probe: homepage HTTP 200; lookup route 404 to anonymous WebFetch 2026-06-19 — deep route unconfirmed

## Cross-references

Collapsed from three proposals (gleif-lei-index, gleif-lei-records, gleif-lei-registry) — same source. Fallbacks opencorporates-registry, uk-companies-house.

## Notes

Registered v54 (Fix 70). Candidate + pointer-gated pending route confirmation (operator ratification rule d). Reclassify to active when: (1) the api.gleif.org/api/v1/lei-records query route is confirmed reachable; (2) cited on a pack with A6 confirmation; (3) F-ENT cross-refs applied.
