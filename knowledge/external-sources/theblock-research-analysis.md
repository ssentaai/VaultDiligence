---
schema_version: 1
id: theblock-research-analysis
name: The Block Research (The Block Pro)
provider: The Block
url_base: https://www.theblock.co
docs_url: https://www.theblock.pro
source_tier: EXPERT
purpose:
  - incident-corroboration
  - protocol-and-market-analysis
  - named-analyst-research-reports
auth: other
access_mode: pointer-gated
freshness_typical: daily
freshness_max_trusted: 30d
covers_chains:
  - ALL
covers_field_ids:
  - F-RIS-001
  - F-RIS-002
  - F-RIS-004
  - F-RIS-005
  - F-ENT-020
fallback_sources:
  - a research-advisory source
  - informal-crypto-press
  - rekt-news
status: candidate
added_in: v54
notes_url:
---

## What this source provides

The Block runs a named research arm, The Block Pro / The Block Research, staffed by identified analysts (e.g. Steven Zheng, VP of Research; Eden Au, Director of Research) producing analytical reports and proprietary datasets and charts. VaultDiligence consumes its analytical reports as corroboration for incident facts and for protocol and investment-manager mapping. The free newsroom (theblock.co) is a separate INFORMAL surface covered by informal-crypto-press.

## Source tier rationale

EXPERT, not FORMAL. The Block Research is a named firm with attributable analysts producing opinion and analysis, matching the EXPERT definition; it does not publish versioned methodology or records-of-record and is not open-source, so it does not clear the two-of-four FORMAL test. Its proprietary data dashboards are an aggregation product, which would be FORMAL only if a documented methodology were published; absent that, the analysis output stays EXPERT with an E(P) ceiling for factual claims.

## When to use it

Use as named-firm corroboration for F-RIS-001/002/004/005 incident facts and as a corroborating name source for the investment manager behind a vault (F-ENT-020) when a The Block Research report on the specific protocol exists. Cite the specific report, its named author, and the retrieval date, and pair the incident corroboration with a FORMAL or ON-CHAIN primary.

## When NOT to use it

Never as the standalone primary for an incident dollar figure, root cause, or for the registered legal name of an investment manager; those require Rekt.news / DeFiHackLabs / Chainalysis and the regulator register or GLEIF respectively. Not for state=E on factual claims (EXPERT ceilings at E(P)). Not for the free newsroom, which is INFORMAL and cited via informal-crypto-press.

## Authentication and rate limits

The newsroom theblock.co returned HTTP 403 to anonymous WebFetch on 2026-06-19; the research product theblock.pro returned HTTP 200 but is subscription-gated with pricing from 2500 USD annually. Programmatic and full-report access requires an operator-held subscription credential; this is an operator-side decision, not a VaultDiligence configuration question. No free API is documented.

Access probe: newsroom theblock.co HTTP 403 to anonymous on 2026-06-19; research product theblock.pro HTTP 200 on 2026-06-19 (301 from theblockresearch.com) but subscription-gated, pricing from 2500 USD annually

## Cross-references

a research-advisory source is the closest peer EXPERT research arm and a fallback. informal-crypto-press covers The Block's free newsroom and the wider press at INFORMAL tier. rekt-news / defihacklabs are the incident primaries this source corroborates.

## Notes

Distinguish the paid research arm (EXPERT) from the free newsroom (INFORMAL) when citing tier; only the research arm earns this entry. A The Block Research claim contradicted by an on-chain read is superseded by the on-chain read. Reclassify to active when: (1) VaultDiligence has cited a specific The Block Research report (named author, date) as corroboration on at least one pack and A6 confirmed it held against a FORMAL or ON-CHAIN primary; (2) a stable subscription-credentialed retrieval path to theblock.pro is confirmed and documented in operator settings; (3) the EXPERT-tier E(P) ceiling has been applied correctly on at least one incident field so the report is never silently treated as a standalone primary.

Ratification (2026-06-19): access_mode=pointer-gated; status=candidate. Newsroom theblock.co HTTP 403 anonymous; research product theblock.pro 200 (2026-06-19) — use theblock.pro.
