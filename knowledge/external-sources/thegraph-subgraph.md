---
schema_version: 1
id: thegraph-subgraph
name: The Graph (Subgraph GraphQL Network)
provider: The Graph
url_base: https://gateway.thegraph.com/api
docs_url: https://thegraph.com/docs/en/
source_tier: FORMAL
purpose:
  - indexed-protocol-event-queries
  - lending-position-aggregation
  - historical-on-chain-time-series
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
  - F-FIN-061
  - F-FIN-062
  - F-LIQ-048
  - F-CTR-006
fallback_sources:
  - goldrush-covalent-api
  - etherscan-evm-explorer
  - direct-rpc-read
status: active
added_in: v54
notes_url:
---

## What this source provides

The Graph indexes smart-contract event data into subgraphs queryable by GraphQL across 60+ networks via its decentralized gateway. For diligence it answers protocol-native questions that raw explorers cannot aggregate efficiently: per-market borrow positions using a vault token as collateral (e.g. the Euler subgraph named in F-FIN-061), host lending-pool utilisation and available-liquidity time series (F-LIQ-048), and historical pause/parameter-change event series (F-CTR-006).

## Source tier rationale

FORMAL, not ON-CHAIN — this is the explicit subgraph case in source-authority. The Graph runs indexing computation off-chain over emitted events; the subgraph's mapping logic is author-defined methodology, and the gateway returns an indexer's representation of that processed data, not a read the reader's compute produces. It meets at least two FORMAL conditions: open-source community with a documented protocol, and a stable attributable network/maintainer. ON-CHAIN fails because the reader's compute is not the source of truth.

## When to use it

Use for protocol-specific aggregation explorers cannot answer in one query: total external borrow against a vault token across a lending protocol's markets (F-FIN-061, feeding the leverage multiplier F-FIN-062), host-pool utilisation and illiquidity-threshold series (F-LIQ-048, cross-ref SC6), and historical emergency-pause / parameter-change events (F-CTR-006). Prefer where a maintained subgraph for the exact protocol exists; confirm the subgraph is current and the mapping covers the entities queried.

## When NOT to use it

Do not cite as ON-CHAIN. Do not trust a subgraph whose mapping logic, indexer, or sync status is unverified — a stale or buggy subgraph silently returns wrong totals, so corroborate material borrow figures against direct-rpc-read or the protocol's own API. Do not use it for fields where no maintained subgraph exists for the protocol in question; fall back to goldrush-covalent-api or per-contract reads.

## Authentication and rate limits

Decentralized-network queries via the gateway require an API key and GRT-denominated query payment / a billing plan; rate and cost depend on the plan. On gateway error, stale-sync, or missing subgraph, fall back to goldrush-covalent-api (decoded multichain) or direct-rpc-read per the tool-recovery skill. Always check the subgraph's indexed-block head against chain head before trusting freshness.

Access probe: HTTP 200 on 2026-06-19 (thegraph.com/docs/en/ landing page; confirms subgraphs, substreams, Graph Node, GraphQL querying of indexed on-chain data across 60+ networks via decentralized network)

## Cross-references

goldrush-covalent-api for breadth where no protocol subgraph exists; etherscan-evm-explorer / blockscout-evm-explorer for single-contract reads; direct-rpc-read (ON-CHAIN) is the authoritative escalation for borrow/position values. F-FIN-061 names the Euler subgraph as a primary source, which is this venue.

## Notes

Proposed candidate (Shape 1) — not registered. Distinct value is protocol-native event aggregation (lending positions, utilisation series) that explorers and balance APIs cannot produce in one call; the per-protocol subgraph dependency means coverage is conditional on a maintained subgraph existing. Reclassify to active when: (1) operator identifies which specific subgraphs (e.g. Euler, the relevant host-pool subgraphs) VaultDiligence treats as authoritative and records their gateway IDs; (2) a query against a named subgraph is corroborated against a direct RPC read for a sample vault token; (3) covers_field_ids cross-references are applied to the field definitions during source-add Step 5.
