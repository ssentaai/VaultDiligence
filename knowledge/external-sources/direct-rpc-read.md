---
schema_version: 1
id: direct-rpc-read
name: Direct EVM/Solana RPC read
provider: Interchangeable RPC providers
url_base: (provider-dependent)
docs_url: 
source_tier: ON-CHAIN
purpose:
  - verified-contract-read
  - onchain-state-read
auth: none
access_mode: fetch
freshness_typical: realtime
freshness_max_trusted: 1h
covers_chains:
  - ethereum
  - base
  - arbitrum
  - optimism
  - polygon
  - solana
covers_field_ids:
  - F-CTR-001
  - F-CTR-002
  - F-CTR-003
  - F-CTR-004
  - F-CTR-005
  - F-SEC-006
  - F-ORC-001
  - F-ORC-002
  - F-FIN-001
  - F-FIN-085
fallback_sources:
  - etherscan-evm-explorer
  - blockscout-evm-explorer
status: active
added_in: v54
notes_url:
---

## What this source provides

Deterministic reads of verified-contract state and view methods (totalSupply, getOwners, getThreshold, getMinDelay, paused, oracle/priceFeed getters, account balances) via direct JSON-RPC, returned by any conformant node identically at a given block.

## Source tier rationale

ON-CHAIN: the value is computed deterministically from chain state and is reader-verifiable — any node returns the identical answer at the same block. The provider is transport, not methodology. This is the single transport-agnostic ON-CHAIN entry; per-provider access is an option, not a separate source.

## When to use it

Any value a verified contract exposes, and as the authoritative escalation for any value a FORMAL explorer/aggregator surfaces. Prefer for material on-chain facts (mint authority, timelock delay, multisig threshold, oracle address).

## When NOT to use it

Not for data requiring off-chain methodology (TVL aggregation, fiat pricing, holder labelling) — use the relevant FORMAL source. Not for unverified contracts (bytecode-only; flag per F-CTR-001).

## Authentication and rate limits

Interchangeable access options: Alchemy, Infura (Consensys), QuickNode, Ankr (keyed or public tiers), public chain RPC, and Solana Foundation RPC. Pick any; keyed providers raise rate limits. Tier follows the deterministic read, not the transport.

Access probe: provider-dependent; verified-contract reads are reader-verifiable at a given block

## Cross-references

Collapsed from the per-provider proposals alchemy-rpc-read, infura-rpc-read, quicknode-rpc-read, ankr-public-rpc, solana-public-rpc (these are access OPTIONS, not separate registry entries). rpc-provider-status (FORMAL) covers RPC liveness/diversity for F-CHN-008. Explorers etherscan/blockscout are FORMAL fallbacks.

## Notes

Registered v54 (Fix 70 ratification). Active. Collapse of 5 per-provider ON-CHAIN proposals into one transport-agnostic entry per operator ratification rule (b).
