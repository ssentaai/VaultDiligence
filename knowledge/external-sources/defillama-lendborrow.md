---
schema_version: 1
id: defillama-lendborrow
name: DefiLlama Yields / Lend-Borrow API
provider: DefiLlama
url_base: https://yields.llama.fi
docs_url: https://api-docs.defillama.com/
source_tier: FORMAL
purpose:
  - cross-venue-lending-pool-data
  - borrow-supply-utilisation-aggregation
  - third-party-leverage-sweep
auth: rate-limited-anonymous
access_mode: fetch
freshness_typical: hourly
freshness_max_trusted: 4h
covers_chains:
  - ALL
covers_field_ids:
  - F-FIN-085
  - F-LIQ-048
fallback_sources:
  - morpho-blue-api
  - aave-protocol-data
  - direct-rpc-read
status: active
added_in: v54
notes_url:
---

## What this source provides

DefiLlama's yields service aggregates lending-market pool data across protocols (Aave, Morpho, Euler, Spark, Compound, others) and chains. The free /pools endpoint returns per-pool TVL, supply APY, metadata; the lend-borrow endpoints (yields/poolsBorrow, yields/chartLendBorrow) return per-pool borrow/supply totals and utilisation.

## Source tier rationale

FORMAL, not ON-CHAIN. The yields dataset is a cross-protocol aggregation with normalised metrics and methodology choices (pool inclusion, APY computation) layered over on-chain state — the aggregation is what makes it FORMAL. Clears FORMAL on attributable maintainer, open-source community (adapters in the open DefiLlama repo), stable documented public API. The per-venue confirming reads (morpho-blue-api, aave-protocol-data, direct-rpc-read) supersede it for any sizing-driving figure. Not EXPERT.

## When to use it

Cross-venue breadth source for F-FIN-085: sweep for every lending pool holding the vault token across protocols and chains in one query, then confirm material positions on each venue's own primary (morpho-blue-api, aave-protocol-data) or on-chain. Secondary corroboration for F-LIQ-048 host-pool utilisation across venues. Its role is to ensure the third-party-leverage register is complete, not to be the terminal figure.

## When NOT to use it

Not the terminal source for a position size/utilisation that will drive a cap/sizing decision — hourly cadence and aggregation make it a discovery layer, not a precision layer; confirm on the venue primary or on-chain (flag I on divergence). The deeper borrow-side endpoints (poolsBorrow, chartLendBorrow) are gated behind DefiLlama's paid Pro API; the free tier covers pool discovery and supply-side data. Not for incident data (the separate defillama-hacks-db entry). Not for the asset's quality.

## Authentication and rate limits

Free API (api.llama.fi / yields.llama.fi) needs no key and api-docs.defillama.com returned HTTP 200 to anonymous WebFetch (2026-06-19); /pools and /chart are anonymous. Borrow-side endpoints (yields/poolsBorrow, yields/chartLendBorrow) are on the Pro tier (pro-api.llama.fi/{API_KEY}) and require a paid key the operator sets as env var / settings.json entry — document where before first use. Anonymous use is rate-limited; on 429, back off per tool-recovery.

Access probe: HTTP 200 on 2026-06-19 (api-docs.defillama.com; free /pools and /chart anonymous; borrow-side yields/poolsBorrow and yields/chartLendBorrow confirmed gated behind paid Pro API at pro-api.llama.fi/{API_KEY})

## Cross-references

morpho-blue-api / aave-protocol-data — the per-venue primaries DefiLlama's sweep hands off to for confirming reads. direct-rpc-read — ON-CHAIN superseding source for any confirmed position. defillama-hacks-db — the separately registered DefiLlama incident database (distinct surface, do not conflate). Field F-FIN-085 — DefiLlama's breadth is the safeguard against an incomplete leverage register.

## Notes

DefiLlama's distinctive value here is completeness: F-FIN-085 fails quietly if a leverage venue is simply not on the analyst's radar, and a cross-venue aggregator is the cheapest defence against that omission. The trade-off is precision — hourly, aggregated, borrow-side detail behind the Pro key — so it discovers, the venue primary or chain confirms. Same-tier disagreement between DefiLlama and a venue primary (both FORMAL) on a position size is an I (Investigate), resolved by the on-chain read. Reclassify to active when: (1) the free-vs-Pro endpoint boundary has been confirmed so agents do not assume borrow-side data is available without the Pro key; (2) VaultDiligence has used DefiLlama as the cross-venue discovery step for an F-FIN-085 register on at least one pack and confirmed material positions on each venue primary, with A6 confirming the handoff; (3) a DefiLlama pool figure has been reconciled against the venue primary / on-chain read for at least one position to characterise the divergence rate.
