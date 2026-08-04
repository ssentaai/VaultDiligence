---
schema_version: 1
id: coingecko-market-data
name: CoinGecko API (price, market cap, volume)
provider: CoinGecko
url_base: https://api.coingecko.com/api/v3
docs_url: https://docs.coingecko.com/
source_tier: FORMAL
purpose:
  - token-price
  - market-cap
  - trading-volume
  - nav-per-share-proxy
auth: rate-limited-anonymous
access_mode: fetch
freshness_typical: minute
freshness_max_trusted: 1h
covers_chains:
  - ALL
covers_field_ids:
  - F-FIN-007
  - F-FIN-001
  - F-FIN-002
  - F-FIN-003
fallback_sources:
  - coinmarketcap-market-data
  - defillama-market
  - messari-market-data
status: active
added_in: v54
notes_url:
---

## What this source provides

CoinGecko provides REST endpoints for current token price, market capitalisation, 24h trading volume, and short-window price changes across listed assets and many chains, plus a per-token /coins/{id} detail surface. Data refreshes on roughly a one-minute cadence. It returns numeric market data, not opinion.

## Source tier rationale

FORMAL, not ON-CHAIN. CoinGecko aggregates exchange and on-chain data through its own listing and pricing methodology, so the consumed value is CoinGecko's computed figure rather than a direct verified-contract read. It clears the FORMAL bar on attributable maintainer (named firm), documented/versioned API, and records-of-record positioning as a widely-cited reference aggregator.

## When to use it

Use for the NAV-per-share proxy on listed vault tokens (F-FIN-007, where CoinGecko is named as a source) and as a FORMAL fallback for TVL (F-FIN-001) and price-derived movement context (F-FIN-002/003). Prefer for spot token price/marketcap/volume of liquid governance or vault-share tokens within the 1h freshness window.

## When NOT to use it

Do not use the CoinGecko market price of a vault share as authoritative NAV when an on-chain convertToAssets() read is available — the on-chain read supersedes (it is higher tier). Do not cite for thinly-traded vault tokens where the listed price is stale or wick-driven; flag those as E(P). Not a source for fee, utilisation, or withdrawable-liquidity fields.

## Authentication and rate limits

The Demo (free) tier is anonymous and rate-limited with a limited endpoint set; the Pro tier needs an API key the operator would set as an env var. On rate-limit (429), back off and fall to coinmarketcap-market-data per tool-recovery. Base URL https://api.coingecko.com/api/v3 for the public/Demo tier; pro-api.coingecko.com for keyed access.

Access probe: HTTP 200 on 2026-06-19 (docs.coingecko.com, reached via 301 from www.coingecko.com/api/documentation)

## Cross-references

coinmarketcap-market-data is the direct same-coverage fallback; defillama-market and messari-market-data overlap on price/marketcap. F-FIN-007 and F-FIN-001 already name CoinGecko in their field definitions (NAV proxy and TVL fallback respectively).

## Notes

On-chain NAV reads always supersede CoinGecko for F-FIN-007 per the source-authority hierarchy; this entry is the FORMAL fallback when an on-chain read is unavailable. Reclassify to active when: (1) the Demo-tier endpoints for price/marketcap/volume are confirmed reachable from the VaultDiligence runtime, (2) the operator records whether a Pro key is provisioned and where the env var lives, and (3) one pack has used CoinGecko as the F-FIN-007 fallback and A6 confirmed it did not diverge from the on-chain NAV by more than the field's tolerance.
