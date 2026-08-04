---
schema_version: 1
id: defillama-tvl-yield
name: DefiLlama TVL & Yields API
provider: DefiLlama
url_base: https://api.llama.fi
docs_url: https://api-docs.defillama.com/
source_tier: FORMAL
purpose:
  - tvl
  - yield-aggregation
  - protocol-metadata
  - dex-liquidity-depth
auth: rate-limited-anonymous
access_mode: fetch
freshness_typical: hourly
freshness_max_trusted: 4h
covers_chains:
  - ALL
covers_field_ids:
  - F-FIN-001
  - F-FIN-002
  - F-FIN-010
  - F-FIN-061
  - F-FIN-063
fallback_sources:
  - dune-custom-queries
  - direct-rpc-read
  - coingecko-protocol
status: active
added_in: v54
notes_url:
---

## What this source provides

DefiLlama exposes a free REST API (api.llama.fi) covering current and historical protocol TVL (/protocols, /protocol/{p}, /tvl/{p}), chain TVL (/v2/chains, /v2/historicalChainTvl), pool-level yields/APY (/pools, /chart/{pool}), stablecoin circulation (/stablecoins), and fees/revenue (/overview/fees). A paid Pro tier (pro-api.llama.fi) adds further endpoints. Update cadence is roughly hourly for TVL and pool data.

## Source tier rationale

FORMAL, not ON-CHAIN. DefiLlama aggregates on-chain state across protocols and applies adapter-level methodology choices (what counts as TVL, double-count handling), so the aggregation layer — not the reader's compute — is the source of truth. It satisfies FORMAL on at least three counts: open-source adapters and methodology on GitHub, an attributable maintainer (DefiLlama team), and versioned public API documentation. For an exact on-chain figure, escalate to direct-rpc-read.

## When to use it

Primary FORMAL source for vault TVL (F-FIN-001) and 7-day TVL change (F-FIN-002) at assessment; for native/organic yield baselining (F-FIN-010) when combined with incentive data; and as corroboration for external-borrow totals (F-FIN-061) and exit-pool depth (F-FIN-063). Prefer it inside the 4h freshness window for headline TVL and yield numbers across all chains and vault types.

## When NOT to use it

Do not cite DefiLlama as the authoritative figure where an exact on-chain read is required (use direct-rpc-read): TVL adapters can lag, double-count, or misclassify leveraged-strategy assets, and TVL is not AUM for leveraged vaults (per F-FIN-001 gap note). Do not use it as the sole source for precise per-market external-leverage positions (F-FIN-061) — read the lending markets directly; DefiLlama is corroboration only. Do not rely on /pools APY predictions as evidence.

## Authentication and rate limits

Free API at api.llama.fi requires no authentication but is rate-limited for anonymous use; on 429 back off and retry per the tool-recovery skill. Pro endpoints require a paid key at pro-api.llama.fi/{KEY}; never place a key in api.llama.fi URLs. If used via curl, the operator must add api.llama.fi to the settings.json allow-list at Step 5.

Access probe: HTTP 200 on 2026-06-19 (api-docs.defillama.com, free tier api.llama.fi documented no-auth)

## Cross-references

dune-custom-queries (fallback for bespoke TVL/leverage queries DefiLlama does not break out); direct-rpc-read (higher tier for exact figures); coingecko-protocol (fallback for protocol/price metadata). Field definitions F-FIN-001/002/010 already name DefiLlama as primary source.

## Notes

Widely used incumbent aggregator; the registry should not add a redundant TVL aggregator on top of this one. Status candidate pending operator ratification. Reclassify to active when: (1) a VaultDiligence pack has cited DefiLlama as primary for F-FIN-001/002 and A6 verification confirmed the figure against a direct-rpc-read or block-explorer cross-check; (2) the operator confirms api.llama.fi is on the settings.json curl allow-list; (3) the 4h freshness_max_trusted has been validated as appropriate for the vault types in active use (tighten for fast-moving leveraged vaults if needed).
