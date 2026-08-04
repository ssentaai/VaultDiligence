---
schema_version: 1
id: goldrush-covalent-api
name: GoldRush (Covalent) Foundational API
provider: GoldRush (Covalent)
url_base: https://api.covalenthq.com/v1
docs_url: https://goldrush.dev/docs/
source_tier: FORMAL
purpose:
  - multichain-token-balances-and-holders
  - decoded-event-logs
  - transaction-history-aggregation
auth: api-key
access_mode: fetch
freshness_typical: minute
freshness_max_trusted: 24h
covers_chains:
  - ethereum
  - base
  - arbitrum
  - optimism
  - polygon
covers_field_ids:
  - F-CTR-001
  - F-FIN-061
  - F-LIQ-040
fallback_sources:
  - etherscan-evm-explorer
  - thegraph-subgraph
  - direct-rpc-read
status: active
added_in: v54
notes_url:
---

## What this source provides

GoldRush (formerly Covalent) offers a unified multichain REST API returning structured, decoded historical data across 100+ chains: token balances by address, full token-holder lists with balances, transaction histories, and decoded log events with USD pricing. It delivers refined/decoded output rather than raw RPC, so token-holder concentration and aggregated balance queries that would require many raw reads come back as a single structured response.

## Source tier rationale

FORMAL, not ON-CHAIN. GoldRush is a named provider (Covalent) running off-chain indexing, decoding, and pricing; the response is the provider's structured representation, and the decoding/pricing layer is methodology the reader does not control. It satisfies at least two FORMAL conditions: attributable maintainer and documented versioned API. The ON-CHAIN first-matching rule fails — it is a remote aggregator API, explicitly the FORMAL case, not a direct verified-contract read.

## When to use it

Use for multichain aggregation that explorers answer poorly: token-holder concentration and redemption-currency holder distribution (supports F-LIQ-040 and corroborates F-CTR-001 holdings), and as one aggregation input for external-borrow / position exposure (F-FIN-061) where a single chain-agnostic balance pull is more efficient than per-protocol calls. Prefer within freshness_max_trusted=24h; pair with thegraph-subgraph for protocol-specific lending positions.

## When NOT to use it

Do not cite as ON-CHAIN, and do not use its USD-priced figures as authoritative valuations — the pricing layer is GoldRush's methodology, not chain state. Do not treat it as the primary source for the lending-position math in F-FIN-061/062 where a protocol-native subgraph or the protocol's own API is more precise; GoldRush is the breadth-over-depth aggregator. Decoded-event coverage depends on contract verification/decoding having succeeded on GoldRush's side.

## Authentication and rate limits

Requires an API key (free tier with rate limits; paid tiers raise them). On 429 or 5xx, back off per the tool-recovery skill and fall back to etherscan-evm-explorer (per-chain) or thegraph-subgraph (protocol positions). Note the api-reference sub-path probed 404 on 2026-06-19; the operator should confirm the exact current endpoint paths before wiring queries.

Access probe: HTTP 200 on 2026-06-19 (goldrush.dev/docs/ root; Foundational API documents token balances, transaction histories, decoded event logs, NFT assets, token holders across 100+ chains. The /docs/api-reference/overview sub-path returned 404 — the docs root resolved)

## Cross-references

thegraph-subgraph for protocol-native lending positions (deeper, narrower); etherscan-evm-explorer / blockscout-evm-explorer for single-chain explorer reads; direct-rpc-read for authoritative on-chain values; DefiLlama (separate venue) overlaps on TVL/aggregation and is the better source for protocol-level TVL.

## Notes

Proposed candidate (Shape 1) — not registered. Distinct value is one-call multichain decoded token-holder and balance data, which neither single-chain explorers nor a single subgraph provide cleanly; the 404 on the api-reference path means endpoint paths must be re-confirmed before registration. Reclassify to active when: (1) operator confirms current endpoint paths and key handling and adds the URL pattern to the settings.json allow-list; (2) a coverage test shows GoldRush token-holder output matches an independent explorer/RPC read for a sample vault token; (3) covers_field_ids cross-references are applied to the field definitions during source-add Step 5.
