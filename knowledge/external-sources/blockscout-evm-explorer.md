---
schema_version: 1
id: blockscout-evm-explorer
name: Blockscout Explorer API
provider: Blockscout
url_base: https://eth.blockscout.com/api
docs_url: https://docs.blockscout.com/devs/apis
source_tier: FORMAL
purpose:
  - contract-source-verification
  - open-source-explorer-fallback
  - l2-and-long-tail-chain-coverage
auth: rate-limited-anonymous
access_mode: fetch
freshness_typical: minute
freshness_max_trusted: 24h
covers_chains:
  - ethereum
  - base
  - arbitrum
  - optimism
  - gnosis
covers_field_ids:
  - F-CTR-001
  - F-CTR-002
  - F-CTR-005
  - F-CTR-006
  - F-SEC-006
  - F-ORC-002
  - F-GOV-005
fallback_sources:
  - etherscan-evm-explorer
  - direct-rpc-read
status: active
added_in: v54
notes_url:
---

## What this source provides

Blockscout is an open-source block explorer with hosted instances for many EVM chains and an Etherscan-compatible RPC API plus a newer REST/PRO API. It returns verified contract source code and ABI, contract read-method results, account and token balances, transfers, and event logs. Its Etherscan-migration compatibility layer means existing explorer query patterns work against chains where Etherscan has no instance.

## Source tier rationale

FORMAL, not ON-CHAIN. Blockscout is a hosted indexing service: the API returns Blockscout's indexed representation of chain state, not a read the reader's compute produces. It meets at least two FORMAL conditions: open source with a stable maintainer community, and a documented API surface. ON-CHAIN fails for the same reason as Etherscan — it is a remote provider, not a direct RPC / verified-contract read.

## When to use it

Use as the primary EVM-explorer source on chains where Blockscout is the canonical or only explorer instance, and as the documented fallback for etherscan-evm-explorer when Etherscan rate-limits or lacks the chain. Authoritative-grade FORMAL for the same identity/governance fields as Etherscan: contract address/standard (F-CTR-001/002), multisig and pause reads (F-CTR-005/006), role enumeration (F-SEC-006), oracle provider reads (F-ORC-002), and timelock duration (F-GOV-005).

## When NOT to use it

Do not cite as ON-CHAIN; escalate to direct-rpc-read for material values. Index coverage and uptime vary by instance (community-hosted vs Blockscout-hosted) — verify the specific chain instance is current before relying on it. Where both Etherscan and Blockscout cover a chain and a value conflicts, treat as same-tier I (Investigate) and resolve via direct-rpc-read.

## Authentication and rate limits

Public hosted instances are usable anonymously but rate-limited; the newer PRO API uses keys and the page notes old MyAccount keys no longer work with PRO routes. On rate-limit or instance downtime, fall back to etherscan-evm-explorer or a direct RPC read per the tool-recovery skill. Self-hosted instances exist for chains without a public one.

Access probe: HTTP 200 on 2026-06-19 (docs.blockscout.com/devs/apis landing page; confirms REST/RPC APIs, PRO API, Etherscan-migration compatibility, self-hosted instances)

## Cross-references

etherscan-evm-explorer is the primary explorer it backstops (and vice versa for long-tail chains); direct-rpc-read is the ON-CHAIN escalation; goldrush-covalent-api and thegraph-subgraph cover the data-aggregation and event-history surfaces Blockscout serves only thinly.

## Notes

Proposed candidate (Shape 1) — not registered. Blockscout's distinct value over Etherscan is open-source provenance and coverage of L2 / long-tail chains, making it a genuine fallback rather than a redundant aggregator. Reclassify to active when: (1) operator confirms which chain instances VaultDiligence will treat as authoritative and adds their URL patterns to the settings.json allow-list; (2) at least one pack has used Blockscout as the explorer of record on a chain Etherscan does not cover, with A6 confirming the citation; (3) covers_field_ids cross-references are applied in the field definitions during source-add Step 5.
