---
schema_version: 1
id: dune-custom-queries
name: Dune Analytics API
provider: Dune
url_base: https://api.dune.com
docs_url: https://docs.dune.com/api-reference/overview/introduction
source_tier: FORMAL
purpose:
  - custom-onchain-queries
  - third-party-leverage-mapping
  - contagion-mapping
  - holder-distribution
auth: api-key
access_mode: fetch
freshness_typical: hourly
freshness_max_trusted: 24h
covers_chains:
  - ALL
covers_field_ids:
  - F-FIN-061
  - F-FIN-062
  - F-FIN-065
  - F-FIN-085
  - F-LIQ-048
fallback_sources:
  - direct-rpc-read
  - defillama-tvl-yield
status: active
added_in: v54
notes_url:
---

## What this source provides

Dune provides a credit-based REST API to execute SQL queries saved in its UI against indexed multi-chain blockchain data (the same datasets powering Dune dashboards) and retrieve results programmatically. Execution endpoints consume credits; metadata endpoints are free. It supports bespoke queries such as enumerating external lending-market positions in a vault token, holder distributions, and DEX-pool depth.

## Source tier rationale

FORMAL, not ON-CHAIN. Dune indexes and decodes chain data off-chain and serves it via its own query engine; the reader executes SQL against Dune's indexed tables, not against chain state directly, so the indexing/decoding layer is the source of truth. It satisfies FORMAL on at least two counts: an attributable maintainer (Dune) with versioned, documented API, and records-of-record query results that are reproducible for a given query and block range.

## When to use it

Use for fields that need bespoke on-chain aggregation no fixed API exposes: building the third-party-leverage register and refresh cadence (F-FIN-085), total external borrow against the vault token across venues (F-FIN-061) and its leverage multiplier (F-FIN-062), the contagion/cascade map of named protocols (F-FIN-065), and host-pool utilisation corroboration (F-LIQ-048). Best when a published query/dashboard already exists or can be authored and re-run reproducibly.

## When NOT to use it

Do not treat a Dune result as ON-CHAIN truth — decoding errors, stale spell/abstraction tables, and query-author mistakes are real failure modes; for the exact position figures F-FIN-061/085 and F-LIQ-048 ultimately require, cross-check with direct-rpc-read. Do not cite a community dashboard whose underlying SQL you have not inspected (the query is the methodology). Do not rely on it where freshness matters more than the indexing lag.

## Authentication and rate limits

API-key authentication is required; keys are auto-generated per team and managed in settings. Pricing is credit-based — execution endpoints consume credits, metadata endpoints are free. The operator must set the Dune API key (env var) and add api.dune.com to the settings.json allow-list at Step 5; document where the key lives. On credit exhaustion or rate limit, fall back to direct-rpc-read per the tool-recovery skill.

Access probe: HTTP 200 on 2026-06-19 (docs.dune.com api-reference)

## Cross-references

direct-rpc-read (higher tier; the authoritative read for the position/utilisation figures Dune aggregates); defillama-tvl-yield (fallback for headline TVL/leverage figures when a Dune query is unavailable). F-FIN-085 and F-LIQ-048 name on-chain reads as primary and analytics dashboards as fallback — Dune is the analytics-dashboard fallback.

## Notes

Differentiated from DefiLlama by supporting arbitrary user-authored aggregation rather than fixed endpoints — earns its own entry rather than being redundant. Status candidate pending operator ratification. Reclassify to active when: (1) the operator provisions a Dune API key and confirms it is in settings.json with documented location; (2) a canonical, query-inspected VaultDiligence Dune query exists for the third-party-leverage register (F-FIN-085) and A6 has cross-checked one result against direct-rpc-read; (3) the credit budget and 24h freshness_max_trusted are validated against the cadence F-FIN-085 requires (refresh before any cap or sizing decision).
