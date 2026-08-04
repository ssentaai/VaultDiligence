---
schema_version: 1
id: defillama-hacks-db
name: DefiLlama Hacks Database
provider: DefiLlama
url_base: https://api.llama.fi
docs_url: https://defillama.com/hacks
source_tier: FORMAL
purpose:
  - exploit-incident-record
  - amount-lost-and-technique
  - protocol-incident-lookup
auth: none
access_mode: fetch
freshness_typical: daily
freshness_max_trusted: 7d
covers_chains:
  - ALL
covers_field_ids:
  - F-RIS-001
  - F-RIS-006
  - F-RIS-002
fallback_sources:
  - defihacklabs-poc-registry
  - slowmist-hacked-db
  - rekt-news-postmortems
status: active
added_in: v54
notes_url:
---

## What this source provides

Structured hacks database served as JSON from api.llama.fi/hacks and surfaced at defillama.com/hacks. Each record carries name, date (unix), amount (USD lost), technique, classification (Protocol Logic / Infrastructure / Rugpull), targetType, chain array, bridgeHack boolean, returnedFunds, and a defillamaId linking to the protocol page. Used as a queryable first-pass record of confirmed exploits per protocol.

## Source tier rationale

FORMAL, not ON-CHAIN. The hacks database is an aggregation: amount, technique, and classification are curated and methodology-dependent, layered on top of underlying on-chain events. DefiLlama clears the FORMAL test on attributable maintainer, open-source community, and records-of-record positioning with a stable public API. The aggregation layer is the methodology, which is what makes it FORMAL rather than ON-CHAIN.

## When to use it

Primary FORMAL source for F-RIS-001 (enumerate confirmed exploits with date, USD lost, technique) and fast corroborating lookup for F-RIS-006 (does this protocol have an incident record). For an oracle-classified incident the technique/classification fields can seed F-RIS-002, then confirm root cause against a post-mortem. Cite the api.llama.fi/hacks record by protocol name and date with retrieval date.

## When NOT to use it

Not for root-cause narrative or resolution detail (technique labels only, not the forensic write-up — use Rekt/SlowMist/audit post-mortem). Not for incidents below its inclusion threshold or very recent uncurated events (absence is not proof of no incident). Not for bad-debt (F-RIS-005) or NAV anomalies (F-RIS-004) that were not exploits.

## Authentication and rate limits

Public, no key. api.llama.fi/hacks returned HTTP 200 with full JSON to anonymous WebFetch on 2026-06-19; the defillama.com/hacks HTML page returned HTTP 403 (bot gate), so prefer the API endpoint. Anonymous use is rate-limited; on 429/5xx back off per tool-recovery and fall back to defihacklabs-poc-registry or slowmist-hacked-db. No operator credential required.

Access probe: api.llama.fi/hacks HTTP 200 (full JSON array) on 2026-06-19; defillama.com/hacks HTML HTTP 403 to anonymous on 2026-06-19 (API endpoint preferred)

## Cross-references

defihacklabs-poc-registry (reproducible PoC corroborating technique/root cause); slowmist-hacked-db (independent named-firm incident DB for amount/classification cross-check); rekt-news-postmortems (narrative root-cause for incidents this DB only labels); fields F-RIS-004/F-RIS-005 (non-exploit incident fields not covered).

## Notes

Classification can disagree with other databases on amount and technique; same-tier (FORMAL vs FORMAL slowmist-hacked-db) disagreement must be flagged as I (Investigate), not silently averaged. The defillamaId link ties an exploit record back to the protocol's TVL page, useful for sizing the incident against the protocol at the time. Reclassify to active when: (1) VaultDiligence has cited a specific api.llama.fi/hacks record as primary source for F-RIS-001 on at least one pack and A6 verification confirmed the citation held; (2) the hacks-DB amount/technique has been cross-checked against slowmist-hacked-db or defihacklabs for at least one incident to characterise the disagreement rate; (3) the inclusion threshold and update lag have been bounded against a known recent incident to validate freshness_max_trusted.

Ratification (2026-06-19): access_mode=fetch; status=active. Use the api.llama.fi/hacks JSON route (HTTP 200, full array); the defillama.com/hacks HTML is 403 to anonymous (2026-06-19).
