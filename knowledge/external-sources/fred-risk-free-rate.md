---
schema_version: 1
id: fred-risk-free-rate
name: FRED API (Federal Reserve Economic Data)
provider: Federal Reserve Bank of St. Louis
url_base: https://api.stlouisfed.org/fred
docs_url: https://fred.stlouisfed.org/docs/api/fred/
source_tier: FORMAL
purpose:
  - risk-free-rate
  - sofr
  - t-bill-yield
  - macro-benchmark
auth: api-key
access_mode: pointer-gated
freshness_typical: daily
freshness_max_trusted: 7d
covers_chains:
  - ALL
covers_field_ids:
  - F-MKT-001
  - F-MKT-002
  - F-FIN-015
fallback_sources:
  - ust-treasury-rates
status: candidate
added_in: v54
notes_url:
---

## What this source provides

FRED exposes the St. Louis Fed's economic time series via REST (series/observations?series_id=...). For VaultDiligence it supplies the daily SOFR series (series_id=SOFR) and the 3-month Treasury bill secondary-market rate (series_id=DTB3), the two risk-free benchmarks. Observations are point-in-time, dated, and revised on the publishing agency's schedule.

## Source tier rationale

FORMAL by the strongest reading of the rule: it is a regulator-affiliated, records-of-record source operated by a Federal Reserve bank, with a documented, versioned API and an attributable institutional maintainer. It is not ON-CHAIN (off-chain macro data). It is the authoritative reference for the risk-free rate, not an opinion source, so it is not EXPERT.

## When to use it

Primary source for the risk-free benchmarks F-MKT-001 (SOFR) and F-MKT-002 (3-month T-bill / DTB3), and therefore the denominator anchor for F-FIN-015 (net yield premium over risk-free, in bps). Use SOFR for floating-rate products and the T-bill for fixed-rate comparisons, per the field definitions. Record the observation date.

## When NOT to use it

Do not use for any crypto-native price, TVL, or vault metric — FRED has no coverage there. Do not cite a stale observation beyond the 7d window without downgrading to E(P); rates move and the latest observation should be re-pulled at assessment time.

## Authentication and rate limits

The REST API requires a free api_key the operator registers at the FRED site and stores as an env var (e.g. FRED_API_KEY); requests without it are rejected. The probe of the human docs page returned 403 to the anonymous fetcher, consistent with the keyed-access model. Fallback when unavailable: the US Treasury daily yield-curve page (ust-treasury-rates, proposed as a fallback slug — the F-MKT-002 field already names home.treasury.gov as fallback).

Access probe: HTTP 403 to anonymous on 2026-06-19 (fred.stlouisfed.org/docs/api/fred/ docs page; the FRED REST API itself requires a free api_key query parameter for series/observations)

## Cross-references

Fallback ust-treasury-rates (home.treasury.gov resource-center) covers the same T-bill benchmark and is named directly in F-MKT-002. F-MKT-001 already names the FRED SOFR endpoint as primary. Feeds the F-FIN-015 calculation.

## Notes

This is the only authoritative risk-free-rate source in the market-price sweep; without it F-MKT-001/002 (and the downstream F-FIN-015 premium) lose their FORMAL anchor, so it is a real acquisition priority despite the keyed access. Reclassify to active when: (1) a free FRED_API_KEY is provisioned and the env-var location is recorded, (2) the SOFR and DTB3 series_ids are confirmed returning current observations from the VaultDiligence runtime, and (3) the ust-treasury-rates fallback is registered or explicitly noted so F-MKT-002 is not single-sourced.

Ratification (2026-06-19): access_mode=pointer-gated; status=candidate. FRED REST API needs a free API key; becomes access_mode=fetch once keyed. Probe: docs HTTP 403 anonymous 2026-06-19.
