---
source_id: S51
name: Coin Metrics State of the Network
tier: T2a
type: Expert analysis — weekly data-backed DeFi research
url: https://coinmetrics.substack.com
docs: https://gitbook-docs.coinmetrics.io/
parent: Coin Metrics (owned by Talos Trading LLC)
added: 2026-04-29
---

# S51 — Coin Metrics State of the Network

## What It Is

Weekly research newsletter from Coin Metrics Senior Research team.
Data-backed analysis of onchain market structure, DeFi mechanics, and
protocol risk. Primary data from CM Network Data Pro and CM Market Data Feed.
Trusted by institutional investors and crypto-native funds.

The research team covers: vault mechanics and risk, lending market structure,
stablecoin dynamics, protocol revenue analysis, on-chain activity metrics.

## What It Covers for VaultDiligence

**Vault mechanics documentation**: the most authoritative published description
of ERC-4626 share price mechanics and curator risk dimensions. Citable in D2
and D3 as EXPERT ANALYSIS background for the vault structure explanation.

**Incident documentation**: Issue 359 (April 15 2026) documents the Resolv
USR collapse (March 2026) and a synthetic-dollar vault oracle incident (October 2025) with
primary data backing. Both are directly applicable adversarial brief inputs.

**Protocol-level data**: TVL figures, utilisation rates, and market structure
data backed by CM Network Data Pro. More methodologically rigorous than
DeFiLlama for cross-validation, but secondary to on-chain primary sources.

**ERC-4626 mechanics**: clean published description of share price/exchange
rate appreciation mechanism. Cite when explaining how vault APY is calculated.

## What It Does NOT Cover

Real-time data (weekly cadence only).
Individual vault risk assessment.
Legal and counterparty structure.
Redemption waterfall specifics.

## How to Use in a VaultDiligence Investigation

**D2 IC Memo**: cite Issue 359 for the three-risk-dimension framework
(liquidity, collateral, oracle) as the industry standard taxonomy.

**D3 Evidence File**: cite Issue 359 for the Resolv and a synthetic-dollar vault oracle incidents
when these are referenced as precedents in credit/oracle risk sections.

**Comparables table**: use Coin Metrics TVL figures as a cross-reference
against DefiLlama for the comparable vaults row. Cite both sources.

**Adversarial brief**: Issue 359 surfaces the multi-vault contagion pattern
and the single-venue oracle failure mode. Both are adversarial questions
for VT-1 and VT-5 investigations.

## Citation Format

Evidence state: E(P) — EXPERT ANALYSIS with stated methodology.
Format:
  "Coin Metrics State of the Network Issue [N] ([author], [date]).
  Source: coinmetrics.substack.com/p/[slug].
  Primary data: CM Network Data Pro."

## Source Bias

Owned by Talos Trading. Commercial interest in data products.
Research methodology is transparent and peer-reviewed in quality.
Cite as EXPERT ANALYSIS. Never as ON-CHAIN or FORMAL.
Cross-reference data points against DefiLlama and on-chain sources.

---
source_id: S52
name: Coin Metrics API
tier: T2a
type: Structured on-chain and market data API
url: https://gitbook-docs.coinmetrics.io/
api_base: https://api.coinmetrics.io/v4/
parent: Coin Metrics (owned by Talos Trading LLC)
pricing: Freemium — community tier available. Pro tier for high volume.
added: 2026-04-29
---

# S52 — Coin Metrics API

## What It Is

Structured API for on-chain network data, market data, and reference data
across crypto assets and protocols. Used by institutional funds and
crypto-native research teams. Community tier is free with rate limits.
Pro tier requires a commercial agreement.

API is structured as: reference data, network data (on-chain metrics),
market data (prices, volume, order book), and index data.

## What Is Available for Vault Investigations

**Network data (on-chain metrics)**:
  Supply metrics by asset (total supply, circulating supply, minted/burned).
  Transaction count and value transferred.
  Active address counts — useful for vault depositor activity cross-reference.

**Market data**:
  OHLCV price data by asset and exchange.
  Reference rates — volume-weighted prices across exchanges.
  Order book data — depth and bid-ask spread.
  Useful for the synthetic-dollar vault oracle incident pattern: confirm whether a price
  deviation was exchange-specific or multi-venue.

**DeFi-specific coverage**:
  As of April 2026: Coin Metrics coverage of DeFi protocol metrics
  is less comprehensive than DefiLlama for TVL and pool-level data.
  Use CM API for: asset-level on-chain metrics, price reference rates,
  and cross-venue order book validation.
  Use DefiLlama for: protocol TVL, pool APY, utilisation rates.

## How to Use in a VaultDiligence Investigation

**Oracle validation**: when investigating oracle risk, use CM reference
rates (volume-weighted across exchanges) to confirm whether a price
deviation seen on one exchange was genuine or exchange-specific.
This is the direct application of the synthetic-dollar vault October 2025 oracle incident.

**Asset supply verification**: for vault collateral assets, cross-reference
circulating supply and minted/burned metrics against protocol claims.

**Price corroboration**: use CM reference rates as a cross-check against
the on-chain oracle price feed being used by the vault. Significant
divergence between the oracle price and CM reference rate = oracle risk flag.

## Citation Format

Evidence state: E(P) for CM API data (derived/aggregated, not primary on-chain).
Format:
  "Coin Metrics API — [metric] for [asset] at [datetime].
  Source: api.coinmetrics.io/v4/[endpoint].
  Note: aggregated reference rate, not primary on-chain source."

## Access

Community tier: register at coinmetrics.io — free, rate limited.
Add API key to .env as COINMETRICS_API_KEY.
Rate limit: community tier is sufficient for investigation use (not real-time).
For validate-apis.py: add a CM reference rate endpoint check.
