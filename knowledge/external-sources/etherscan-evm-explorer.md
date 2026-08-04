---
schema_version: 1
id: etherscan-evm-explorer
name: Etherscan API (V2 multichain)
provider: Etherscan
url_base: https://api.etherscan.io/v2/api
docs_url: https://docs.etherscan.io/
source_tier: FORMAL
purpose:
  - contract-source-verification
  - abi-and-bytecode-retrieval
  - privileged-role-and-governance-reads
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
  - F-CTR-002
  - F-CTR-004
  - F-CTR-005
  - F-CTR-006
  - F-CTR-010
  - F-CTR-019
  - F-SEC-006
  - F-SEC-007
  - F-GOV-005
  - F-ORC-001
  - F-ORC-002
fallback_sources:
  - blockscout-evm-explorer
  - direct-rpc-read
status: active
added_in: v54
notes_url:
---

## What this source provides

Etherscan's V2 unified API returns verified contract source code, ABI, contract creation metadata, account/token balances, transaction lists, and event logs across 60+ EVM-compatible chains from a single endpoint keyed by chainid. For governance and security fields it exposes the read functions of verified contracts (getThreshold, getOwners, getMinDelay, paused, oracle/priceFeed getters) and the verification status flag that distinguishes a verified from an unverified contract.

## Source tier rationale

FORMAL, not ON-CHAIN. Etherscan is a named firm operating a hosted indexing-and-API service: the response is Etherscan's representation of chain state, not a deterministic read the reader's own compute produces, and Etherscan can be wrong or stale where a direct RPC read cannot. It satisfies at least two FORMAL conditions: attributable maintainer (Etherscan) and well-documented versioned API surface (V2 docs). The first-matching ON-CHAIN rule fails because access is via a remote provider, not direct RPC / verified-contract read.

## When to use it

Primary FORMAL source for EVM contract identity and governance reads: token contract address and standard (F-CTR-001/002), upgrade and pause controls (F-CTR-004/006), multisig configuration (F-CTR-005), bridge contract identification (F-CTR-010/019), on-chain role enumeration and documentation status (F-SEC-006/007), timelock duration (F-GOV-005), and oracle type/provider address reads (F-ORC-001/002). Prefer within freshness_max_trusted=24h for governance reads; for any claim where exactness is load-bearing, corroborate the value with direct-rpc-read.

## When NOT to use it

Do not cite Etherscan as ON-CHAIN evidence or as the sole source for a material value that a direct RPC read could confirm — escalate to direct-rpc-read for those. Do not rely on it for chains it does not index (use blockscout-evm-explorer). Its 'verified source' label confirms verification but does not itself prove the deployed bytecode matches; treat unverified-contract results as a flag per F-CTR-001 gap action, not as absence of risk.

## Authentication and rate limits

Requires a free API key (set via ETHERSCAN_API_KEY env var / settings.json). Anonymous and free-tier access is rate-limited (commonly a few requests per second / a daily cap); on 429 or rate-limit, back off per the tool-recovery skill and fall back to blockscout-evm-explorer or a direct RPC read. The V2 endpoint is the single multichain base; legacy per-chain hostnames are deprecated.

Access probe: HTTP 200 on 2026-06-19 (docs.etherscan.io introduction page; confirms unified V2 API across 60+ EVM chains, contract/ABI/account/logs modules)

## Cross-references

blockscout-covalent-api fallback for non-Etherscan chains; direct-rpc-read (ON-CHAIN) is the authoritative escalation for any value Etherscan surfaces; goldrush-covalent-api overlaps on token balances/holders; thegraph-subgraph overlaps on event-log history. Field gap actions in F-CTR-001/004/005/006 and F-ORC-002 name Etherscan directly.

## Notes

Proposed candidate (Shape 1) — not registered. Etherscan is the de facto canonical EVM explorer with the widest verified-source coverage, which is why multiple field definitions name it as primary or fallback. Reclassify to active when: (1) operator confirms the V2 API base and key handling against .claude/settings.json allow-list; (2) Etherscan has been cited as primary on at least one pack with A6 verification confirming the citation held; (3) field definitions in covers_field_ids carry the etherscan-evm-explorer cross-reference applied during source-add Step 5.
