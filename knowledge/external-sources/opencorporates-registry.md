---
schema_version: 1
id: opencorporates-registry
name: OpenCorporates Company Database
provider: OpenCorporates Ltd
url_base: https://api.opencorporates.com/v0.4
docs_url: https://api.opencorporates.com/documentation/API-Reference
source_tier: FORMAL
purpose:
  - legal-entity-lookup
  - company-registry-aggregation
  - officer-and-jurisdiction-data
auth: api-key
access_mode: fetch
freshness_typical: weekly
freshness_max_trusted: 30d
covers_chains:
  - ALL
covers_field_ids:
  - F-ENT-001
  - F-ENT-002
  - F-ENT-003
fallback_sources:
  - gleif-lei
  - uk-companies-house
status: active
added_in: v54
notes_url:
---

## What this source provides

OpenCorporates aggregates company records sourced directly from 140+ official government registries into a standardised schema: company name, company number, jurisdiction, company type, incorporation date, current status (active/dissolved), registered address, and officer/director records. The REST API (v0.4) returns JSON; bulk-data delivery is also offered. Each record cites its source registry and retrieval provenance.

## Source tier rationale

FORMAL: an attributable named maintainer (OpenCorporates Ltd) standardising records sourced from primary government registries, with documented API methodology and provenance per record. Off-chain (not ON-CHAIN) and an aggregation layer over primary registries — the aggregation is methodology, which is the defining mark of FORMAL rather than a raw primary source. For the highest-stakes claims, prefer the cited domicile registry directly over the aggregator.

## When to use it

Use for F-ENT-001 (legal entity name), F-ENT-002 (entity/company type), and F-ENT-003 (domicile/jurisdiction) — especially when the domicile registry has no convenient API and OpenCorporates has mirrored it. Strongest where it returns the underlying official-source citation that can be followed to the primary registry. Good first cross-jurisdiction lookup.

## When NOT to use it

Do not cite OpenCorporates as the terminal primary when the underlying domicile registry is directly reachable — follow the cited source and cite that for state=E (aggregator citation depth can push toward E(P)). Do not use for regulatory authorisation or enforcement status (F-ENT-004, F-PRJ-008) — it carries identity, not licensing. Coverage of certain offshore registries (some Caribbean jurisdictions) can be partial or stale; check the per-record source date.

## Authentication and rate limits

An API key (registered account) is required for programmatic access; tiered pricing applies for API and bulk use, set by the operator. The web search UI is browsable but the API is the reliable path. Operator sets the key as an env var. On rate-limit or coverage gap, fall back to gleif-lei-records or the named domicile registry.

Access probe: HTTP 200 on 2026-06-19 (opencorporates.com homepage confirmed: world's largest open legal-entity database sourced from 140+ official government registries, API and bulk products with login/pricing tiers)

## Cross-references

F-ENT-001/002/003 name company registry in domicile jurisdiction as primary with GLEIF as fallback — OpenCorporates sits between, mirroring many domicile registries. Fallbacks gleif-lei-records (LEI-holding entities) and uk-companies-house (UK entities, primary-source) cover the same identity fields. For US identity, sec-edgar-filings corroborates the filed name.

## Notes

OpenCorporates is most valuable as a cross-jurisdiction index that points to primary registries; treat it as a finder, then cite the primary it surfaces. Reclassify to active when: (1) the API key/pricing tier is provisioned and the access path documented; (2) the per-record source-citation behaviour is confirmed so agents cite the primary registry, not the aggregator, for state=E; (3) at least one pack cites OpenCorporates for F-ENT-001/002/003 and A6 confirms the citation chain resolved to a primary source.
