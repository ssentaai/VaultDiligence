# VaultDiligence Framework — Master Index

**Framework version: v54** (Sprint 4, 2026-06-18). v53 baseline frozen at
`knowledge-v53/` + git tag `v53`. Scope: `CHANGELOG-v54.md`. Current state:
`docs/state-of-framework-v54.md`. 13 pillars (P0–P10, P12, P13; P11 reserved),
346 fields, 47 red flags, 14 scenarios.

## Purpose

This file is the entry point for every agent session.
Read this first. Navigate to specific files as needed.
Do not re-read raw xlsx files. Everything is here.

---

## Six Investigation Areas (risk categories)

Standard taxonomy used in all output. Maps to framework pillars internally.

| Category | Pillars | The Question |
|----------|---------|-------------|
| Legal and Custody Risk | P1, P2 | Is the capital actually there and legally mine? |
| Credit and Collateral Risk | P4, P5, P6 | What happens in an orderly stress event? |
| Market and Oracle Risk | P3 | Is the price the protocol uses correct? |
| Liquidity and Exit Risk | P9 | Can I exit at fair value when I want to leave? |
| Operational and Governance | P8, P10 | Who controls this and can they fail? |
| Smart Contract Risk | P7 | Can the code be exploited or manipulated? |
| Bridging Risk | P12 | Can the bridge carrying this asset fail or be frozen? |
| Chain Risk | P13 | Does the chain it lives on inherit failure to every asset? |

Detailed criteria for each: knowledge/framework/pillars/P[N].md

---

## Red Flag Conditions

47 conditions total (RF01–RF47). Severity labels are surfacing classifications,
not verdicts — structural observations the allocator weighs.

CRITICAL: RF01, RF02, RF03, RF04, RF05, RF06, RF07, RF28
  Observable conditions with the most severe structural consequences.
  Surface immediately when triggered.

MATERIAL / BLOCKING / HIGH / INVESTIGATE: RF08 through RF47 (excluding above)
  Observable conditions requiring disclosure and gap action. v54 added RF44
  (bridge config below baseline, P12), RF45 (chain critical property, P13),
  RF46 (weak bug bounty, P7), RF47 (unregistered DAO / no wrapper, P10).

Full logic: knowledge/red-flags/RF[NN].md (one file per red flag)
Field-to-trigger mapping: knowledge/data-model/fields/

---

## Why VaultDiligence Exists in the Agent Economy

The agentic infrastructure stack is assembling in a compressed window.
ERC-8004 (identity, reputation, validation for autonomous agents).
ERC-8183 (Job primitive: escrow-locked work with independent evaluator).
x402 and MPP (settlement across stablecoin and fiat rails).
x402 Foundation: Coinbase, Cloudflare, Google, Visa, AWS, Circle, Anthropic.

What none of this stack provides: a trust layer for capital deployment.

An agent treasury deploying capital into a yield vault does not have
a compliance team, an IC, or a diligence analyst. It needs machine-readable
evidence that a vault meets a defined threshold. A score cannot serve this.
The agent needs interrogable evidence: which conditions were observed,
which gaps remain open, what each structural consequence means.

VaultDiligence is Layer 1 in the three-layer agent capital stack:
  Layer 1: Diligence (VaultDiligence) — Know Your Vault
  Layer 2: Investment Rails — KYC for machines, regulated access
  Layer 3: Wallet / Payment — Coinbase Agentic Wallet, x402, MPP

Sequence: VaultDiligence first. Then rails. Then execution.
Full positioning: spec/market-positioning.md
the structured evidence output API spec: spec/evidence-object-schema.md

## Vault Type Routing

> **Note (archetype migration — Phase 3 complete, 2026-07-09):** VT-N is RETIRED as a routing key. The canonical classification AND routing key is the multi-dimensional archetype tuple — see `archetype/dimensions.md` (vocabulary) and `archetype/vt-decomposition-map.md` (VT-N -> tuple map). Field applicability (Phase 2), pillar gates, d1 branches, and the adversarial lenses (Phase 3) all route off the dimensions; the per-field `derived-from` comments and the VT stub files below remain as historical audit artifacts, and VT-N is derivable from the tuple via the decomposition map. The routing table below is retained for historical reference only. Left historical by scope decision (a separate later step): P0's classification entry-point, P1/P3 weighting emphasis, and the four non-d1 commands.

| Type | Primary Investigation Focus | Notes |
|------|---------------------------|-------|
| VT-1 DeFi Lending | Market/Oracle, Credit/Collateral, Smart Contract | Morpho/Aave/Compound |
| VT-2 Delta-Neutral | Credit/Collateral, Liquidity | Perp funding capture |
| VT-3 Tokenised RWA | Legal/Custody, Credit, Liquidity | Off-chain underlying |
| VT-3a Tokenised Fund | Legal/Custody, Liquidity, Operational | BVI SPC/Cayman. KYC-gated. |
| VT-4 Structured Finance | Legal/Custody, Credit, Smart Contract | Senior/junior tranches |
| VT-5 Liquid Staking | Market/Oracle, Smart Contract, Liquidity | Slashing risk |
| VT-6 Yield Aggregator | Credit, Operational, Smart Contract | Multi-strategy |
| VT-7 Leveraged Stack | ALL — requires two documents | Collateral doc + strategy doc |
| VT-8 TradFi-Primary/Onchain-Wrapped | Legal/Custody, Credit | a preferred-equity-backed vault is first example |
| VT-A Agent Treasury Vault | Smart Contract (35%), Liquidity (25%) | Primary depositors are autonomous agents. Hard requirement: instant 1-block withdrawal. Pack decay: 14 days. Output: structured JSON. |

---

## Evidence States

E      Evidenced. Source confirmed. URL cited. Date stated.
E(P)   Partial. Something confirmed, material gap remains.
G2     Gap: information exists but not publicly accessible.
       Action: request from named person + organisation.
G3     Gap: information does not exist publicly.
       Action: operator must create and publish.
I      Investigate: conflicting sources. State the conflict.
N/A    Not applicable to this vault type. State why.

---

## Document Output Map

D1  Initial Allocability Screen  — Exit Liquidity Box + hard gates. 30 min.
D2  Executive Summary           — IC-ready 2 pages. Standard risk taxonomy.
D3  Full Diligence Pack         — All criteria. Every field sourced.
D4  Gap-to-Action Brief         — Every gap. Named party. Precise action.
D5  Interview Framework         — Key people questions from open D4 gaps.

Detail: document-map.md is not yet created — pending the document-availability build (see an internal analysis, currently PAUSED).

---

## Comparables

Always include. Always sourced. Always dated.
Always include one TradFi anchor row.
No judgment column. No advantage assessment.

Standard comparable set by vault type:
VT-1: Morpho/Gauntlet USDC, Euler USDC, Aave USDC. TradFi: T-bill MMF.
VT-3a: Ondo USDY, Maple Finance, Centrifuge. TradFi: CLO ETF (a tokenized CLO fund on NYSE).
VT-2: a synthetic-dollar vault, Gauntlet Basis Alpha. TradFi: Prime brokerage repo.

---

## Priority Order for Agent Work

1. Exit Liquidity Box — always first
2. Critical condition red flags (RF01-RF07, RF28) — from T1 data
3. Legal structure and custody — defines capital safety
4. Redemption waterfall — aggregated timeline across counterparty stack
5. On-chain data snapshot — TVL, APY, utilisation, oracle freshness
6. Audit and smart contract review
7. Counterparty register
8. Remaining criteria by risk category

---

## T2a Sources (third-party assessments — cite as pointer with date)

Particula PDARP:     particula.io             — onchain risk ratings
Credora:             credora.com              — credit assessment
Exponential:         exponential.fi           — yield risk ratings
LlamaRisk:           llamarisk.com            — protocol risk reports
Gauntlet:            gauntlet.network         — risk parameter reports
Chaos Labs:          chaoslabs.xyz            — simulation-based risk
Accountable DVN:     accountable.capital      — proof of solvency (S46)
a risk-infrastructure provider Risk Radar:  defirisk.intotheblock.com — protocol risk assessments,
                                                  curator TVL benchmarks (S49)
Coin Metrics SOTN:   coinmetrics.substack.com  — weekly vault/DeFi research,
                                                  incident documentation (S51)
Coin Metrics API:    api.coinmetrics.io        — price reference rates,
                                                  on-chain asset metrics (S52)
Webacy DD APIs:      dd.xyz / docs.webacy.com   — contract vulnerability tags,
                                                  vault universe, DEWS depeg
                                                  signals, sanctions screening (S50)
  YieldApp:          yieldapp.accountable.capital — verifiable yield listings

## T2 Sources (require subscription — time-series and fundamentals)

Artemis Analytics:   artemisanalytics.com     — time-series TVL, revenue,
                                                 DeFi rates, bad debt history (S47)
  Use for: 90-day trends, yield sustainability, bad debt history.
  Not available: cite as G2 with "S47 subscription required" note.

## Background Research (not citable sources — analyst reading only)

Fundamental Labs:    fundamental-labs.xyz
  Curated DeFi fundamental analysis. Different architecture and output
  to VaultDiligence. Not a citable source in packs.
  Use as analyst background reading only.
  Notable: adcv_ DeFi rate methodology benchmarks Steakhouse USDC Prime.

For every T2a/T2/EXPERT source: cite with date, state what it covers,
state explicitly what it does not cover.
Never replicate their methodology. Link and note the date.
Full source definitions: knowledge/data-model/sources/
