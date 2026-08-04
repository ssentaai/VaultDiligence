---
schema_version: 1
id: chainalysis-crime-research
name: Chainalysis Crypto Crime Research
provider: Chainalysis
url_base: https://www.chainalysis.com
docs_url: https://www.chainalysis.com/blog/
source_tier: EXPERT
purpose:
  - aggregate-stolen-funds-analysis
  - ecosystem-incident-context
  - attack-trend-research
auth: none
access_mode: fetch
freshness_typical: weekly
freshness_max_trusted: 90d
covers_chains:
  - ALL
covers_field_ids:
  - F-RIS-001
  - F-RIS-002
fallback_sources:
  - defillama-hacks-db
  - slowmist-hacked-db
  - rekt-news-postmortems
status: active
added_in: v54
notes_url:
---

## What this source provides

Named blockchain-data firm publishing crypto-crime research, including the annual Crypto Crime Report and the Geography of Cryptocurrency Report, plus an ongoing investigations blog covering hacks, stolen funds, and laundering networks. The field definitions name 'Chainalysis public reports' as a primary/fallback for F-RIS-001 and F-RIS-002. Used for aggregate stolen-funds context and, where a specific incident is covered, corroborating amount and attribution.

## Source tier rationale

EXPERT. Chainalysis is a named firm with deep domain reputation, but its public output is analysis and aggregate research (reports and blog posts), not a queryable per-protocol record of record. Under the first-matching rule it is a named firm producing opinion/analysis = EXPERT, not FORMAL. As EXPERT it cannot be the sole source for a material fact and must corroborate a FORMAL or ON-CHAIN incident record.

## When to use it

EXPERT corroboration and context for F-RIS-001 and F-RIS-002 — e.g. corroborating the scale or attribution of a specific exploit Chainalysis has written up, or setting an incident against ecosystem-wide stolen-funds trends. Most useful for attacker attribution or laundering path, Chainalysis's distinctive strength. Cite the specific report or blog post and its publication date.

## When NOT to use it

Not as the sole or primary source for a specific exploit's date/amount/root cause — those are better answered by the FORMAL incident DBs and the PoC registry; per-incident granularity in the public blog is variable. Not for protocol-level incident presence (F-RIS-006 — that is Rekt and DeFiHackLabs). Not for non-exploit incidents (F-RIS-004, F-RIS-005). Much of the deepest data is in gated/commercial products, so public-surface coverage is partial.

## Authentication and rate limits

Public research is free, no key; blog and report landing pages returned HTTP 200 to anonymous WebFetch on 2026-06-19. Full datasets and the investigations product are commercial and gated — VaultDiligence cites only the public research surface. No operator credential required for the public blog/reports.

Access probe: chainalysis.com/blog HTTP 200 on 2026-06-19 (blog and report landing pages readable; 2026 Crypto Crime Report referenced)

## Cross-references

defillama-hacks-db / slowmist-hacked-db (FORMAL incident records Chainalysis context should corroborate); rekt-news-postmortems (adjacent EXPERT narrative source — both EXPERT, so a Chainalysis-vs-Rekt disagreement on a fact is a same-tier I (Investigate)); fields F-RIS-001/F-RIS-002 name Chainalysis public reports as a source directly.

## Notes

Comparative advantage for diligence is attribution and fund-flow tracing, not incident enumeration — reach for it on the 'where did the funds go / who did it' question rather than 'did it happen.' Because the deepest evidence sits behind commercial products, the public surface alone often supports only E(P); treat any material public-research claim as needing a FORMAL corroborator. Reclassify to active when: (1) VaultDiligence has cited a specific Chainalysis public report or blog post as EXPERT corroboration for F-RIS-001 or F-RIS-002 on at least one pack and A6 confirmed it; (2) the public-vs-gated boundary has been characterised so agents do not cite data that is actually behind the commercial product; (3) a Chainalysis attribution claim has been corroborated against a FORMAL incident record to validate the corroboration workflow.
