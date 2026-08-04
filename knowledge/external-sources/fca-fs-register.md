---
schema_version: 1
id: fca-fs-register
name: FCA Financial Services Register
provider: UK Financial Conduct Authority (FCA)
url_base: https://register.fca.org.uk
docs_url: https://www.fca.org.uk/firms/financial-services-register
source_tier: FORMAL
purpose:
  - uk-authorisation-status
  - regulated-firm-lookup
  - scam-clone-warning-check
auth: api-key
access_mode: fetch
freshness_typical: daily
freshness_max_trusted: 7d
covers_chains:
  - ALL
covers_field_ids:
  - F-PRJ-008
  - F-ENT-004
fallback_sources:
  - sec-edgar-filings
  - opencorporates-registry
status: active
added_in: v54
notes_url:
---

## What this source provides

The FS Register is the UK public record of firms, individuals, and bodies that are or have been authorised by the FCA or PRA. It returns authorisation status, permitted regulated activities, firm reference number (FRN), trading names, appointed representatives and principals, Directory Persons (SMCR), and explicit warnings for unauthorised firms, scams, and clone firms. A free FS Register API (developer portal, key required) provides the same data programmatically; a bulk Register Extract Service also exists.

## Source tier rationale

FORMAL with high confidence: operated by a named UK regulator and is a record of record for UK authorisation. Off-chain (not ON-CHAIN). Satisfies regulator-affiliated records of record, attributable maintainer (FCA), and a documented public API.

## When to use it

Use for F-PRJ-008 (UK regulatory status — whether the operator/fund is FCA/PRA-authorised, the permitted activities, and any clone/scam warning) and F-ENT-004 (regulatory license type, FRN, and issuing regulator where the FCA is the regulator). Authoritative for UK-authorised entities; the clone-firm warnings are a direct red-flag input.

## When NOT to use it

Do not read absence as a negative finding for entities that operate lawfully outside UK perimeter (e.g. an offshore fund not marketing into the UK) — not-on-register is expected, a G2/G3 gap not a contradiction. Do not use for US, EU, or Singapore status (use sec-edgar-filings, ESMA, MAS). The FCA explicitly disclaims SLAs/uptime, so do not treat the API as always-available.

## Authentication and rate limits

The public search UI at register.fca.org.uk is free and anonymous but client-rendered (HTML scrape yields a loading shell — read values via the API, not WebFetch HTML). The FS Register API is free but requires a key generated through the FCA developer portal; operator sets the key as an env var. No SLA or uptime guarantee — on outage, back off per tool-recovery and fall back to the web UI or screenshot citation.

Access probe: HTTP 200 on 2026-06-19 (fca.org.uk register overview confirmed public record of authorised firms/individuals and a free FS Register API via developer portal requiring a generated key; the register.fca.org.uk search UI is client-rendered and returned a CSS/loading shell to anonymous WebFetch)

## Cross-references

F-PRJ-008 names the FCA register (register.fca.org.uk) as a primary source. F-ENT-004 names the regulator public register (incl. FCA) as primary. sec-edgar-filings is the US parallel; opencorporates-registry corroborates the legal entity behind an FRN. A future ESMA/MAS/VARA entry would complete the multi-jurisdiction status picture.

## Notes

The clone-firm and unauthorised-firm warnings make this register valuable beyond plain authorisation lookup. Single-jurisdiction by design — pair with EDGAR and an EU/Asia register for F-PRJ-008 multi-jurisdiction coverage. Reclassify to active when: (1) the FS Register API key is provisioned and the access path documented in this entry; (2) the client-rendered-UI vs API distinction is confirmed so agents do not scrape the loading shell; (3) at least one pack cites the FCA register for F-PRJ-008 or F-ENT-004 and A6 confirms it held.
