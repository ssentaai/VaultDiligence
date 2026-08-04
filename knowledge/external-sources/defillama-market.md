---
schema_version: 1
id: defillama-market
name: DefiLlama API (TVL, prices, yields)
provider: DefiLlama
url_base: https://api.llama.fi
docs_url: https://api-docs.defillama.com/
source_tier: FORMAL
purpose:
  - tvl
  - token-price
  - yield-aggregation
  - incentive-apy
  - dex-pool-depth
auth: rate-limited-anonymous
access_mode: fetch
freshness_typical: hourly
freshness_max_trusted: 4h
covers_chains:
  - ALL
covers_field_ids:
  - F-FIN-001
  - F-FIN-002
  - F-FIN-003
  - F-FIN-004
  - F-FIN-009
  - F-FIN-010
  - F-LIQ-011
fallback_sources:
  - coingecko-market-data
  - coinmarketcap-market-data
  - messari-market-data
status: active
added_in: v54
notes_url:
---

## What this source provides

DefiLlama exposes free REST endpoints for protocol/chain TVL (/tvl/{protocol}, /protocol/{protocol}, /v2/historicalChainTvl), current and historical token prices (/prices/current/{coins}, /prices/historical), yields and pool APY/TVL (/pools, /chart/{pool}), and reward-token incentive data. Update cadence is roughly hourly. It returns numeric market and financial aggregates, not opinion.

## Source tier rationale

FORMAL, not ON-CHAIN. DefiLlama aggregates on-chain state through its own indexing and methodology choices, so the reader's compute is not the source of truth — the aggregation layer is. It satisfies the FORMAL bar on at least three of the four tests: open-source community (github.com/DefiLlama), attributable maintainers, and versioned/documented methodology. The underlying numbers ultimately derive from chain state, but the consumed artifact is DefiLlama's computed feed.

## When to use it

Primary FORMAL source for vault/protocol TVL (F-FIN-001) and its 7d/30d/peak movement (F-FIN-002/003/004), for token-incentive APY via rewardTokens (F-FIN-009), and as the organic-yield input for F-FIN-010 when paired with revenue data. Use within the 4h freshness window; record the snapshot timestamp. Default aggregator for ALL chains.

## When NOT to use it

Do not cite for withdrawable-now liquidity (F-FIN-005) or utilisation (F-FIN-006) — those require on-chain or curator disclosure. Do not treat DefiLlama TVL as AUM for leveraged strategies. Do not use the /pools depth figure as an exit-stress simulation for F-LIQ-014/015/016 — those need a 1inch/DEX execution simulation, a different venue. Known issue: protocol-name slug mismatches can return stale or empty TVL silently; cross-check the slug.

## Authentication and rate limits

Free tier requires no authentication (base URL https://api.llama.fi). Anonymous use is rate-limited; on 429, back off per the tool-recovery skill and fall back to coingecko-market-data. A Pro API (paid) adds exclusive endpoints and higher limits; the operator decides whether to provision a key. No VaultDiligence-side key is required for the free endpoints.

Access probe: HTTP 200 on 2026-06-19 (api-docs.defillama.com; base https://api.llama.fi returned 404 on bare root, which is expected — it serves resource paths not a root index)

## Cross-references

coingecko-market-data and coinmarketcap-market-data are price/marketcap fallbacks; messari-market-data corroborates. F-FIN-001 already names DefiLlama as primary source in its field definition. For exit-stress liquidity (F-LIQ-014/015/016) defer to a dex-liquidity venue source, not this entry.

## Notes

DefiLlama overlaps heavily with the other market aggregators on TVL/price; the operator should set explicit fallback ordering at Step 5 rather than treating them as interchangeable, to avoid the one-source-per-field divergence the investigation-core rule warns about. Reclassify to active when: (1) the free endpoints used for F-FIN-001/002/003/009/010 are confirmed reachable from the VaultDiligence runtime with the slug-resolution checked against at least one live pack, (2) fallback ordering versus coingecko-market-data and coinmarketcap-market-data is recorded in the field cross-references, and (3) one pack has cited DefiLlama as primary for F-FIN-001 and A6 verification confirmed the citation held.
