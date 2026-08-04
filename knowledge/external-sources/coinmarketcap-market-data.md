---
schema_version: 1
id: coinmarketcap-market-data
name: CoinMarketCap API (price, market cap, volume)
provider: CoinMarketCap
url_base: https://pro-api.coinmarketcap.com
docs_url: https://coinmarketcap.com/api/
source_tier: FORMAL
purpose:
  - token-price
  - market-cap
  - trading-volume
auth: api-key
access_mode: fetch
freshness_typical: minute
freshness_max_trusted: 1h
covers_chains:
  - ALL
covers_field_ids:
  - F-FIN-007
  - F-FIN-001
fallback_sources:
  - coingecko-market-data
  - defillama-market
  - messari-market-data
status: active
added_in: v54
notes_url:
---

## What this source provides

CoinMarketCap's API delivers live price quotes, historical OHLCV, market capitalisation, trading volume, and global market metrics across a large token and exchange universe, with most endpoints refreshing on a roughly one-minute cycle. It returns numeric market data, not opinion. Access is also available via WebSocket and an MCP server.

## Source tier rationale

FORMAL, not ON-CHAIN. CoinMarketCap aggregates exchange and chain data through its own listing and pricing methodology, so the consumed figure is CMC's computed value. It clears the FORMAL bar on attributable maintainer (named firm) and a documented, versioned, records-of-record API widely used as a reference. The underlying data is not a direct verified-contract read.

## When to use it

Use as the direct fallback to CoinGecko for spot token price, market cap, and 24h volume on listed governance/vault tokens, supporting the F-FIN-007 NAV-per-share proxy and the F-FIN-001 TVL/marketcap corroboration when CoinGecko is rate-limited or disagrees. Prefer within the 1h freshness window.

## When NOT to use it

Do not use over an on-chain NAV read for F-FIN-007 — the on-chain read supersedes. Do not cite for illiquid vault tokens where the listed price is stale (flag E(P)). Same-tier conflict with CoinGecko on the same claim is an Investigate (I) flag, not a silent pick. Not a source for fee, utilisation, or liquidity-depth fields.

## Authentication and rate limits

A keyless trial tier exists for selected endpoints; the Basic (free) tier requires an API key (15,000 monthly call credits, 50 requests/minute) the operator stores as an env var (e.g. CMC_API_KEY). Higher tiers and commercial use require paid plans. On 429/credit exhaustion, fall back to coingecko-market-data per tool-recovery.

Access probe: HTTP 200 on 2026-06-19 (coinmarketcap.com/api/)

## Cross-references

coingecko-market-data is the primary same-coverage peer (this is its fallback); defillama-market and messari-market-data overlap. Shares F-FIN-007 and F-FIN-001 coverage with those entries.

## Notes

Redundant with CoinGecko on coverage — its registry value is purely as a same-tier fallback for resilience and for I-flag cross-checks, not as an independent primary; the operator may reject it if CoinGecko plus DefiLlama are deemed sufficient. Reclassify to active when: (1) a CMC API key is provisioned and the env-var location recorded, (2) the price/marketcap endpoints are confirmed reachable from the VaultDiligence runtime, and (3) the operator confirms it adds fallback value beyond coingecko-market-data (else reject to _rejected.md as redundant).
