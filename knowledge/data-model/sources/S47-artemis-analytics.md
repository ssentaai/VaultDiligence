---
source_id: S47
name: Artemis Analytics
tier: T2
type: Institutional crypto data platform — time-series and fundamentals
url: https://app.artemisanalytics.com
api: https://api.artemisanalytics.com
sheets_syntax: =ART("{token}","{metric}")
---

# S47 — Artemis Analytics

## What It Is

Institutional-grade crypto analytics platform. Trusted by McKinsey,
T. Rowe Price, VanEck, Visa, Circle, Sequoia, Grayscale, Tether.
Team from Ribbit Capital, Venmo, BlackRock.
Founded 2022. Backed by Haun Ventures, Variant, Modular Capital.
Covers 12,000+ tokens across 50+ blockchains.

## What It Covers

TVL time-series (90-day, 1-year trends)
Protocol revenue and fee trends
DeFi utilisation rates over time
Active addresses and transaction volume
Stablecoin flows and market share
Developer activity metrics
Cross-chain flow data
Bad debt history for lending protocols
Yield sustainability metrics (revenue vs APY paid)

## What It Does NOT Cover

Redemption waterfall structure (counterparty-level T+N).
Legal structure and custody architecture.
Smart contract privileged roles.
Audit scope and findings.
These require VaultDiligence investigation criteria, not Artemis data.

## Evidence Tier

T2: Requires subscription. Not freely accessible.
If Artemis data is unavailable: classify field as G2.
State: "Time-series data available via Artemis Analytics (S47).
Subscription required. Point-in-time snapshot used instead."

For point-in-time fields where Artemis provides time-series context:
  Label: TS (time-series) vs PT (point-in-time) in field registry.
  PT fields confirmed from T1 APIs. TS context from Artemis where available.

## How to Cite

Value: [metric value]
Source: Artemis Analytics, api.artemisanalytics.com/[endpoint]
Retrieved: [YYYY-MM-DD]
Period: [e.g. 90-day trend, 12-month trend]
Evidence state: E (if subscription active) / G2 (if not accessible)

## Artemis Sheets Syntax (for analyst workflow)

=ART("MORPHO","TVL")           — Morpho TVL latest
=ART("MORPHO","REV")           — Morpho protocol revenue
=ART("AAVE","BAD_DEBT")        — Aave bad debt history
=ART("STEAK_USDC","UTIL")      — Steakhouse USDC utilisation rate

## Key Use Cases for VaultDiligence

VT-1 DeFi Lending:
  Utilisation rate trend: is this vault approaching Nash equilibrium?
  Revenue vs APY: is yield sustainable or subsidised?
  Bad debt history: named incidents, amounts, resolution.

VT-5 Liquid Staking:
  Slashing event history for validators in the staking pool.
  APR trend. Withdrawal queue depth over time.

VT-3a Tokenised Funds:
  Protocol-level TVL trend (fund manager credibility signal).

Comparables table:
  Time-series TVL for all comparable vaults (not just point-in-time).
  Revenue trend for protocol sustainability assessment.

## Relationship to VaultDiligence

Artemis provides the time-series context that T1 APIs cannot.
VaultDiligence investigation criteria require a primary source for every field.
Artemis is a T2 source: valuable context, not primary evidence.
Primary on-chain evidence (Morpho API, Etherscan) takes precedence
when Artemis time-series and T1 point-in-time conflict.
