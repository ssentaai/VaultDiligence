---
schema_version: 1
id: slowmist-hacked-db
name: SlowMist Hacked Database
provider: SlowMist
url_base: https://hacked.slowmist.io
docs_url: https://hacked.slowmist.io
source_tier: FORMAL
purpose:
  - exploit-incident-record
  - amount-lost-and-attack-classification
  - cross-ecosystem-incident-lookup
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
  - defillama-hacks-db
  - defihacklabs-poc-registry
  - rekt-news-postmortems
status: active
added_in: v54
notes_url:
---

## What this source provides

Blockchain-security-incident database maintained by the security firm SlowMist. At probing it recorded 2,154 incidents and a running cumulative-loss total, with per-incident fields: date, financial loss, attack classification (smart contract vulnerability, private key leakage, flash loan attack, etc.), affected project, and a short description, across Ethereum, Solana, BSC, Polygon and others. Used as a second independent named-firm incident record for cross-checking F-RIS-001.

## Source tier rationale

FORMAL. Maintained by SlowMist, a named blockchain-security firm, applying a consistent attack-classification taxonomy (versioned methodology in practice), and a record of record for catalogued incidents — satisfies at least two FORMAL criteria (attributable maintainer + records of record + consistent classification methodology). An aggregation, not a direct chain read, so FORMAL, not ON-CHAIN.

## When to use it

Primary or corroborating FORMAL source for F-RIS-001 (date, amount, attack classification) and cross-check for F-RIS-006, especially for non-EVM ecosystems (Solana, Tron) where DefiLlama's hacks coverage is thinner. For flash-loan or oracle-classified incidents, the classification seeds F-RIS-002. Cite the specific incident entry and retrieval date.

## When NOT to use it

Not for deep forensic root cause (per-incident description is brief; the forensic write-up is SlowMist's separate analysis blog or Rekt). Not as the sole amount source when it disagrees with DefiLlama — flag same-tier disagreement as I (Investigate). Not for non-exploit incidents (bad debt F-RIS-005, NAV anomalies F-RIS-004).

## Authentication and rate limits

Public, no key. Site returned HTTP 200 to anonymous WebFetch on 2026-06-19. JavaScript-assisted interface, so deep per-incident detail may load client-side; prefer the rendered incident page and transcribe values honestly. Anonymous use is best-effort and rate-limited; back off per tool-recovery on failure. No operator credential required.

Access probe: hacked.slowmist.io HTTP 200 on 2026-06-19 (incident table and cumulative-loss total readable; 2,154 incidents recorded)

## Cross-references

defillama-hacks-db (primary structured incident DB — cross-check amount and technique); defihacklabs-poc-registry (reproducible PoC where SlowMist gives only a prose description); rekt-news-postmortems (narrative analysis on the same incidents).

## Notes

Value is independence: a second named-firm catalogue, so SlowMist/DefiLlama agreement on an incident's amount strengthens an F-RIS-001 claim while disagreement is a genuine I (Investigate). Cross-ecosystem coverage (Solana, Tron, non-EVM) is a real complement to DefiLlama's EVM-weighted set. SlowMist also runs paid services, but the public Hacked database is the surface registered here. Reclassify to active when: (1) VaultDiligence has cited a specific SlowMist Hacked incident as a source for F-RIS-001 on at least one pack and A6 confirmed it; (2) its amount/classification has been cross-checked against defillama-hacks-db for at least one incident to characterise the agreement rate; (3) a reliable per-incident retrieval path (rendered page values, not just the summary table) has been confirmed against one detailed record.
