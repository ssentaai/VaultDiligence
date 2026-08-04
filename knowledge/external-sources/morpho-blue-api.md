---
schema_version: 1
id: morpho-blue-api
name: Morpho API (GraphQL)
provider: Morpho Association / Morpho Labs
url_base: https://api.morpho.org/graphql
docs_url: https://docs.morpho.org/tools/offchain/api/
source_tier: FORMAL
purpose:
  - third-party-leverage-position-reads
  - host-market-utilisation-and-liquidity
  - liquidation-parameter-lookup
auth: none
access_mode: fetch
freshness_typical: minute
freshness_max_trusted: 1h
covers_chains:
  - ethereum
  - base
covers_field_ids:
  - F-FIN-085
  - F-LIQ-048
fallback_sources:
  - defillama-lendborrow
  - direct-rpc-read
status: active
added_in: v54
notes_url:
---

## What this source provides

GraphQL endpoint (api.morpho.org/graphql) serving real-time on-chain and off-chain state for Morpho Blue markets and MetaMorpho vaults. Per market returns supplyAssets, borrowAssets, collateralAssets, liquidityAssets, utilisation, LLTV (liquidation loan-to-value), oracle, and per-position data.

## Source tier rationale

FORMAL, not ON-CHAIN. Market/position state derives from the Morpho Blue contracts, but the API indexes and aggregates it off-chain (USD conversions, derived utilisation) — the methodology layer that defines FORMAL. Clears FORMAL on attributable maintainer (Morpho Association/Morpho Labs), open-source protocol, versioned public API documentation. A direct verified-contract read of a Morpho market is the superseding ON-CHAIN source; this API is the indexed convenience layer. Not EXPERT (serves state, not opinion).

## When to use it

Primary FORMAL source for F-FIN-085 when the vault token is supplied as collateral or borrowed against on Morpho markets (enumerate each market, read leveraged position size and LLTV liquidation threshold, record refresh cadence), and for F-LIQ-048 when a Morpho market is the host pool (current utilisation, available liquidity, utilisation level at which withdrawals cease to clear). Short field TTL, so freshness_max_trusted is 1h.

## When NOT to use it

Not the terminal source for a cap/sizing decision without reconciling against a direct contract read — F-FIN-085 and F-LIQ-048 are inspection-validatable on-chain and a stale/diverging API figure must not drive a sizing call (reconcile; flag I on divergence). Not for non-Morpho venues (Aave, Euler, Spark need their own sources). Not for positions on chains the API does not index. Not for the underlying asset's NAV/quality (F-FIN-085 is about second-order queue pressure independent of NAV).

## Authentication and rate limits

Public, no key for reads. Apollo Server / GraphiQL surface returned HTTP 200 to anonymous WebFetch (2026-06-19), confirming the GraphQL server is live and reachable without authentication. Anonymous use is rate-limited; on 429/5xx, back off per tool-recovery and fall back to defillama-lendborrow or the direct contract read. No operator credential required for normal-volume reads.

Access probe: HTTP 200 on 2026-06-19 (Apollo Server / GraphiQL sandbox surface responded to anonymous WebFetch; GraphQL server live, no auth). Endpoint and schema fields corroborated via WebSearch of Morpho docs (supplyAssets, borrowAssets, collateralAssets, liquidityAssets).

## Cross-references

defillama-lendborrow — cross-venue aggregator fallback covering the same F-FIN-085/F-LIQ-048 fields across many lending markets at once. direct-rpc-read — ON-CHAIN superseding source for Morpho market params and positions. Field F-FIN-085 — the Resolv 100M USD a tokenized CLO fund loop on Aave Horizon / USR depeg precedent is the exact second-order-leverage failure this API helps size on the Morpho surface.

## Notes

The diligence value is venue-specific position enumeration: F-FIN-085 demands a per-venue register, so Morpho's API is the Morpho-venue primary, Aave's is the Aave-venue primary, and DefiLlama is the cross-venue sweep that catches venues not individually wired. Because the API serves an aggregated/indexed view, any figure that will drive a sizing/cap decision should be reconciled against on-chain market state, and the register's refresh date must be recorded (a stale register is explicitly disqualified by the field's standard). Reclassify to active when: (1) a Morpho API market-state read has been reconciled against a direct Morpho Blue contract read for at least one market; (2) VaultDiligence has built an F-FIN-085 register or F-LIQ-048 host-market utilisation read citing this API on at least one pack and A6 confirmed it; (3) the anonymous rate-limit has been characterised as sufficient for a pack's enumeration volume or a higher-throughput path confirmed.
