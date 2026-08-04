---
schema_version: 1
id: aave-protocol-data
name: Aave Protocol Data (Docs + Subgraph/API)
provider: Aave Labs / Aave DAO
url_base: https://aave.com/docs
docs_url: https://aave.com/docs/developers/smart-contracts/pool-data-provider
source_tier: FORMAL
purpose:
  - host-pool-utilisation-and-liquidity
  - third-party-leverage-position-reads
  - liquidation-parameter-lookup
auth: rate-limited-anonymous
access_mode: fetch
freshness_typical: minute
freshness_max_trusted: 1h
covers_chains:
  - ethereum
  - arbitrum
  - optimism
  - base
covers_field_ids:
  - F-LIQ-048
  - F-FIN-085
fallback_sources:
  - defillama-lendborrow
  - direct-rpc-read
  - morpho-blue-api
status: active
added_in: v54
notes_url:
---

## What this source provides

Aave developer documentation and a GraphQL/subgraph data layer (plus on-chain AaveProtocolDataProvider/UiPoolDataProvider helpers) exposing per-reserve state: total supplied, total borrowed (variable/stable), available liquidity, utilisation rate, liquidation threshold and LTV, liquidation bonus, and per-user positions.

## Source tier rationale

FORMAL, not ON-CHAIN. Reserve state derives from the Aave Pool contracts, but the documented data layer/subgraph indexes and normalises it off-chain (derived utilisation, USD figures) — the methodology layer. Clears FORMAL on attributable maintainer (Aave Labs/Aave DAO), open-source protocol, versioned public documentation, open-source data layer. The direct verified-contract read via AaveProtocolDataProvider/UiPoolDataProvider over RPC is the superseding ON-CHAIN source. Not EXPERT.

## When to use it

Primary FORMAL source for F-LIQ-048 when an Aave pool is the host pool (current utilisation, available liquidity, the utilisation level at which withdrawals cease to clear — full utilisation freezes all depositors), and for F-FIN-085 when the vault token is borrowed against on Aave (enumerate positions, read liquidation threshold). Host-pool primary for VT-1/VT-6/VT-7 vaults embedded in Aave. Short field TTL, so freshness_max_trusted is 1h.

## When NOT to use it

Not the terminal source for a withdrawal-freeze/cap finding without reconciling against on-chain reserve state — F-LIQ-048 is inspection-validatable on-chain and the Kelp DAO contagion precedent (18 Apr 2026, host-pool utilisation reaching full with 5.4B USD withdrawn in hours) is exactly where a stale figure would mislead. Not for non-Aave venues. Not for the underlying asset's quality. Not for governance/parameter-change history.

## Authentication and rate limits

Public, no key for docs and public data layer. Docs site HTTP 200 to anonymous WebFetch (2026-06-19). The hosted subgraph/API may apply anonymous rate limits and some subgraph access has moved to keyed gateways; on 429/403, back off per tool-recovery and fall through to the on-chain AaveProtocolDataProvider read or defillama-lendborrow. Document any required gateway key path before first use. No paid credential required for the docs surface.

Access probe: HTTP 200 on 2026-06-19 (docs site; Markets Data, Parameters, and Liquidations sections readable; GraphQL/React data layer documented)

## Cross-references

defillama-lendborrow — cross-venue aggregator fallback covering the same fields across Aave/Morpho/Euler/Spark at once. direct-rpc-read — ON-CHAIN superseding source (AaveProtocolDataProvider/UiPoolDataProvider). morpho-blue-api — Morpho-venue counterpart for the same F-FIN-085/F-LIQ-048 fields. Field F-LIQ-048 — the Kelp DAO/Aave contagion precedent is the host-pool-freeze scenario this source sizes; cross-ref SC6.

## Notes

Aave is the canonical host-pool case for F-LIQ-048: the field's own precedent is an Aave freeze, so Aave reserve state is the most diligence-relevant utilisation read. As with all indexed layers, reconcile any cap/sizing-driving figure against the on-chain data provider, and record read time, since utilisation can move to full within hours under stress. Subgraph access arrangements have shifted toward keyed gateways across the ecosystem, so confirm the live access path at retrieval time. Reclassify to active when: (1) an Aave utilisation/liquidity read has been reconciled against the on-chain AaveProtocolDataProvider for at least one reserve; (2) VaultDiligence has cited an Aave host-pool utilisation read for F-LIQ-048 (or a leverage position for F-FIN-085) on at least one pack and A6 confirmed it; (3) the live subgraph/API access path (anonymous vs keyed gateway) has been confirmed and documented.
