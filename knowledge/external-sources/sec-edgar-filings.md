---
schema_version: 1
id: sec-edgar-filings
name: SEC EDGAR Full-Text and Submissions API
provider: U.S. Securities and Exchange Commission (SEC)
url_base: https://data.sec.gov
docs_url: https://www.sec.gov/search-filings/edgar-application-programming-interfaces
source_tier: FORMAL
purpose:
  - regulatory-filings
  - issuer-registration-status
  - us-securities-disclosure
auth: rate-limited-anonymous
access_mode: pointer-gated
freshness_typical: daily
freshness_max_trusted: 30d
covers_chains:
  - ALL
covers_field_ids:
  - F-PRJ-008
  - F-ENT-001
  - F-LEG-004
fallback_sources:
  - opencorporates-registry
  - fca-fs-register
status: candidate
added_in: v54
notes_url:
---

## What this source provides

EDGAR exposes registered-issuer filings for entities subject to US securities law: company submissions history (form types, filing dates, accession numbers), filer metadata (CIK, legal name, state of incorporation, SIC code), and full-text search over filing bodies. The data.sec.gov submissions endpoint returns JSON; full-text search and the document archive return filing documents. Filings are records of record for US registration and disclosure status.

## Source tier rationale

FORMAL with high confidence: EDGAR is operated by a named US federal regulator and the filings are records of record by definition. It is off-chain (not ON-CHAIN) — the reader queries the SEC's service. It satisfies regulator-affiliated records of record, attributable maintainer (SEC), and documented public API.

## When to use it

Use for F-PRJ-008 (regulatory status in the US — whether the operator or fund has SEC registrations, exemptions, or filed disclosures), F-ENT-001 (legal entity name as filed), and as corroboration for F-LEG-004 (token/security classification where an issuer has filed a registration or exemption notice such as a Form D). Authoritative for US-domiciled or US-registered issuers; cite specific accession numbers.

## When NOT to use it

Do not use for non-US entities with no US nexus — absence of an EDGAR record for an offshore fund is expected and is not evidence of any status. Do not infer enforcement action from EDGAR alone; enforcement lives in the SEC litigation/admin-proceedings databases, a different surface. Do not use for live UK/EU/Singapore status (use fca-fs-register, ESMA, or MAS).

## Authentication and rate limits

Anonymous over HTTPS; no API key. The SEC fair-access policy requires every programmatic request to send a descriptive User-Agent header identifying the caller, and rate-limits to a modest requests-per-second ceiling — exceeding it yields HTTP 403/429. The default WebFetch agent is blocked, so reads must go through curl or an agent that sets a compliant User-Agent. On block, back off per tool-recovery; fall back to the EDGAR web UI.

Access probe: HTTP 403 to anonymous WebFetch on 2026-06-19 (sec.gov docs page blocks the default fetch agent; the data.sec.gov submissions/full-text API is publicly documented and requires a descriptive User-Agent header per SEC fair-access policy)

## Cross-references

F-PRJ-008 names SEC EDGAR as primary source alongside FCA and MAS registers. fca-fs-register is the parallel UK-status source; opencorporates-registry corroborates the filed legal entity name. For enforcement-specific status, a separate SEC litigation-database entry would be the correct source (acquisition gap).

## Notes

EDGAR is the canonical US records-of-record surface and indispensable for any vault with a US nexus. The access caveat (User-Agent requirement; default fetch agent blocked) is the main operational friction and must be respected to avoid IP blocks. Reclassify to active when: (1) a curl/User-Agent-compliant access path is confirmed and the observed rate ceiling is documented here; (2) the distinct enforcement-database surface is registered or explicitly scoped out so F-PRJ-008 enforcement claims have a home; (3) at least one pack cites a specific EDGAR accession for F-PRJ-008 or F-ENT-001 and A6 confirms it.

Ratification (2026-06-19): access_mode=pointer-gated; status=candidate. Requires a declared User-Agent; use the data.sec.gov submissions / full-text-search JSON routes, not the www.sec.gov docs page (HTTP 403 to default agent 2026-06-19). ROUTE: confirm exact data.sec.gov endpoint per field.
