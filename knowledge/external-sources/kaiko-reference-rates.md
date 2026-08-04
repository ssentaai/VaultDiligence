---
schema_version: 1
id: kaiko-reference-rates
name: Kaiko Market Data and Reference Rates
provider: Kaiko
url_base: https://us.market-api.kaiko.io
docs_url: https://docs.kaiko.com/
source_tier: FORMAL
purpose:
  - reference-rates
  - fair-valuation
  - market-liquidity
  - institutional-price
auth: other
access_mode: fetch
freshness_typical: sub-minute
freshness_max_trusted: 1h
covers_chains:
  - ALL
covers_field_ids:
  - F-FIN-007
  - F-LIQ-011
fallback_sources:
  - coingecko-market-data
  - defillama-market
status: active
added_in: v54
notes_url:
---

## What this source provides

Kaiko provides enterprise-grade, BMR-compliant reference rates, fair-valuation pricing, Level 1 and Level 2 market-data feeds across spot, derivatives, and lending venues (centralised and decentralised), and index/calculation-agent services. The data is institutional-grade price and liquidity information delivered under commercial contract.

## Source tier rationale

FORMAL: a named firm producing records-of-record, regulation-aware reference rates (BMR-compliant) with documented methodology and a stable institutional maintainer. It aggregates venue data via its own methodology, so it is not ON-CHAIN, and it produces benchmark data rather than opinion, so it is not EXPERT.

## When to use it

Use only when an institutional-grade reference rate or audited fair-valuation price is specifically required for the NAV-per-share proxy (F-FIN-007) at large position size, or when a regulation-grade liquidity/depth figure is needed to corroborate DEX-pool depth context (F-LIQ-011) beyond what free aggregators provide. This is a contract-gated escalation source, not a default.

## When NOT to use it

Do not assume Kaiko is reachable — without a commercial contract there is no anonymous production access, so for most packs the free aggregators (CoinGecko, DefiLlama) are the operative sources. Do not use over an on-chain NAV read for F-FIN-007. Do not treat its liquidity feed as an exit-stress simulation for F-LIQ-014/015/016 (those need a 1inch/DEX execution sim).

## Authentication and rate limits

Enterprise-gated: production APIs require a commercial contract and credentialed access; a free Research account exists but does not unlock production feeds. The operator must decide whether to procure a contract before this source can be cited; until then it is effectively blocked for live evidence. No VaultDiligence-side anonymous configuration is possible.

Access probe: HTTP 200 on 2026-06-19 (www.kaiko.com landing page; production market-data and reference-rate APIs are enterprise-gated and require a commercial contract, no anonymous production access)

## Cross-references

coingecko-market-data and defillama-market are the accessible fallbacks for the same fields when no Kaiko contract exists. A dex-liquidity venue source covers the F-LIQ exit-stress simulations Kaiko does not.

## Notes

Highest-grade source in the sweep but the least accessible — proposed so the operator has it on record as the institutional escalation option, with the explicit caveat that it cannot support live evidence without a commercial contract; absent that contract the operator may legitimately reject or leave it dormant. Reclassify to active when: (1) a Kaiko commercial contract and credentialed API access are in place and the env-var/credential location is recorded, (2) the reference-rate and market-data endpoints are confirmed reachable from the VaultDiligence runtime, and (3) a pack has cited Kaiko for F-FIN-007 or F-LIQ-011 and A6 verification confirmed the citation held.
