---
schema_version: 1
id: messari-market-data
name: Messari Asset & Market Data API
provider: Messari
url_base: https://api.messari.io
docs_url: https://docs.messari.io/
source_tier: FORMAL
purpose:
  - token-price
  - market-cap
  - trading-volume
  - asset-metrics
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
  - coinmarketcap-market-data
  - defillama-market
status: active
added_in: v54
notes_url:
---

## What this source provides

Messari's Asset & Market Data endpoint provides price, trading volume, and market capitalisation plus quantitative metrics for a large asset universe (stated 40,000+ assets), accessible programmatically. The numeric market-data surface is the part relevant to this venue class; it returns data, not commentary.

## Source tier rationale

FORMAL for the market-data API: a named firm (Messari) with a documented, versioned API used as records-of-record by enterprise consumers, aggregating exchange/chain data via its own methodology — not a direct verified-contract read, so not ON-CHAIN. Note: Messari's research/Intelligence product (analyst reports, opinion) is EXPERT and out of scope for this entry; only the quantitative market-data API is classified FORMAL here.

## When to use it

Use as a corroborating FORMAL source for token price, market cap, and volume feeding the F-FIN-007 NAV-per-share proxy and F-FIN-001 corroboration, particularly when CoinGecko and CoinMarketCap disagree and a third reference is useful to resolve or to flag an Investigate (I). Within the 1h freshness window.

## When NOT to use it

Do not cite Messari research/Intelligence analyst opinion under this entry — that is EXPERT and needs a separate citation. Do not use over an on-chain NAV read for F-FIN-007. Do not rely on it as a primary if the asset is not in its covered universe. Not a source for fee, utilisation, or liquidity-depth fields.

## Authentication and rate limits

The market-data API requires an API key the operator provisions and stores as an env var (e.g. MESSARI_API_KEY); tier/pricing details were not on the docs landing page and must be confirmed at registration. On unavailability, fall back to coingecko-market-data or coinmarketcap-market-data per tool-recovery.

Access probe: HTTP 200 on 2026-06-19 (docs.messari.io)

## Cross-references

coingecko-market-data, coinmarketcap-market-data, and defillama-market are the overlapping/fallback peers. A future expert-messari-research entry would cover the EXPERT-tier analyst product separately.

## Notes

Coverage overlaps the other aggregators; its registry value is as a third reference for I-flag disambiguation rather than an independent primary, and the FORMAL/EXPERT split (data API vs research) must be kept clean at citation time. Reclassify to active when: (1) a Messari API key is provisioned, the tier/limits confirmed, and the env-var location recorded, (2) the market-data endpoints are confirmed reachable from the VaultDiligence runtime, and (3) the operator confirms it adds disambiguation value beyond CoinGecko plus CoinMarketCap (else reject as redundant).
