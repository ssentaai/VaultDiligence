---
schema_version: 1
id: uk-companies-house
name: UK Companies House Public Data API
provider: Companies House (UK Government)
url_base: https://api.company-information.service.gov.uk
docs_url: https://developer.company-information.service.gov.uk/
source_tier: FORMAL
purpose:
  - uk-company-registry
  - incorporation-record
  - officer-and-filing-history
auth: api-key
access_mode: fetch
freshness_typical: realtime
freshness_max_trusted: 7d
covers_chains:
  - ALL
covers_field_ids:
  - F-ENT-001
  - F-ENT-002
  - F-ENT-003
  - F-ENT-006
fallback_sources:
  - opencorporates-registry
  - gleif-lei
status: active
added_in: v54
notes_url:
---

## What this source provides

The Companies House Public Data API returns statutory records for UK-registered companies (Companies Act 2006): registered company name, company number, company type, incorporation date, registered office address, company status (active/dissolved/liquidation), SIC codes, officers (directors/secretaries), persons with significant control, and filing history. Data is described as live and real-time; responses are JSON over REST.

## Source tier rationale

FORMAL with high confidence: the statutory UK company register operated by a named government body — records of record for UK incorporation by definition. Off-chain (not ON-CHAIN) and a documented public REST API with key-based access. As a primary statutory registry it is higher-authority than the OpenCorporates aggregation for UK entities.

## When to use it

Use as the primary source for UK-incorporated operator entities: F-ENT-001 (registered name), F-ENT-002 (company type), F-ENT-003 (jurisdiction = UK), and F-ENT-006 (incorporation date, directly from the statutory record). Prefer over OpenCorporates for UK entities because it is the primary source; reads support state=E within freshness_max_trusted.

## When NOT to use it

Applies only to UK-registered companies — not for offshore (BVI/Cayman) or non-UK entities, where the relevant domicile registry or OpenCorporates is correct. Do not use for FCA authorisation or regulatory status (F-ENT-004, F-PRJ-008) — Companies House records existence and corporate structure, not regulatory permission. Persons-with-significant-control data can lag real ownership; treat PSC as a lead, not proof of beneficial ownership.

## Authentication and rate limits

An API key (free registered application key) is required and passed via HTTP Basic auth on https://api.company-information.service.gov.uk; the operator registers an application on the developer hub and stores the key as an env var. Subject to per-key rate limiting (HTTP 429 on excess) — back off per tool-recovery and fall back to the Companies House web service or OpenCorporates.

Access probe: HTTP 200 on 2026-06-19 (developer.company-information.service.gov.uk hub confirmed: live/real-time REST API for companies under the Companies Act 2006, with an authentication section indicating key-based access)

## Cross-references

F-ENT-001/002/003/006 name the company registry in the domicile jurisdiction as primary — for UK entities this is the registry. opencorporates-registry mirrors Companies House data (use as fallback or cross-jurisdiction finder); gleif-lei-records cross-checks identity for UK entities holding an LEI. For UK regulatory status pair with fca-fs-register.

## Notes

For any UK-domiciled operator this is the authoritative primary registry and should outrank the OpenCorporates mirror for the same fields. Reclassify to active when: (1) the application API key is provisioned and the HTTP Basic access path documented; (2) the per-key rate limit is observed and recorded here; (3) at least one pack cites Companies House for F-ENT-001/002/003/006 on a UK entity and A6 confirms it.
