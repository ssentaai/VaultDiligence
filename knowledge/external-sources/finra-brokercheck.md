---
schema_version: 1
id: finra-brokercheck
name: FINRA BrokerCheck
provider: FINRA (Financial Industry Regulatory Authority)
url_base: https://brokercheck.finra.org
docs_url: https://brokercheck.finra.org
source_tier: FORMAL
purpose:
  - broker-dealer-regulatory-standing
  - prime-broker-disciplinary-history
  - registration-status-verification
auth: rate-limited-anonymous
access_mode: fetch
freshness_typical: daily
freshness_max_trusted: 30d
covers_chains:
  - ALL
covers_field_ids:
  - F-CUS-001
  - F-CUS-004
fallback_sources:
  - sec-edgar-filings
  - sipc-member-list
status: active
added_in: v54
notes_url:
---

## What this source provides

Public FINRA lookup for US broker-dealers and registered representatives. Returns per firm/individual: registration status, CRD number, employment history, licensing, and disclosed regulatory actions, complaints, and disciplinary events. Used to confirm a named prime broker's registration and enumerate its disciplinary history.

## Source tier rationale

FORMAL. Operated by FINRA, a named SEC-overseen SRO, surfacing records of record (registration filings and disclosed regulatory events). Clears FORMAL on attributable regulator-affiliated maintainer and records of record. Not ON-CHAIN (no chain involvement); not EXPERT (records, not opinion).

## When to use it

Primary FORMAL source for confirming a prime broker's registration and disciplinary standing (F-CUS-001, F-CUS-004) for VT-3/VT-4/VT-8 vaults with a US prime broker. Cite the specific firm CRD page and retrieval date; prefer over operator disclosure for regulatory-standing claims.

## When NOT to use it

Not for non-US brokers (covers only FINRA-registered firms). Not for SIPC coverage limits (use the SIPC list and the brokerage agreement). Not for custody-agreement terms such as rehypothecation, which are document-review fields (F-CUS-002, F-ENT-042) no lookup can answer.

## Authentication and rate limits

Public, no API key. Web UI anonymous and rate-limited; an undocumented JSON API exists at api.brokercheck.finra.org that may throttle bursts. Treat scrapes as best-effort and fall back to the rendered firm page. No operator credential required.

Access probe: HTTP 200 on 2026-06-19 (homepage, anonymous WebFetch)

## Cross-references

sec-edgar-filings (broker-dealer FOCUS/X-17A-5 financial filings); sipc-member-list (companion membership lookup); fields F-CUS-002 and F-ENT-042 (document-review fields BrokerCheck cannot answer).

## Notes

US-registered broker-dealers only; international prime brokers are a G2 against the home regulator. Disclosure events are self-reported and regulator-filed, so absence of a disclosure is weaker evidence than presence. Reclassify to active when: (1) VaultDiligence has cited a specific BrokerCheck firm page as primary source on at least one pack and A6 confirmed it held; (2) a stable retrieval path (rendered firm page or documented API route) returns consistent results across two queries; (3) the freshness_max_trusted window is validated against an observed firm-record update.
