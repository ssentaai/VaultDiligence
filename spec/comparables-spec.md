# Comparables Table — Specification

## Universal Rule

Every vault investigation returns exactly five comparables plus one TradFi anchor.
No exceptions. No vault is assessed in isolation.

The comparable set is not determined by vault type.
It is determined by: what else is competing for the same dollar allocation?

Ask: if this allocator did not choose this vault, what would they choose instead?
Those are the comparables. Structure similarity is secondary.
Yield tier, risk profile, and allocator audience are primary.

## How the Agent Selects Comparables

Step 1: Identify the yield tier of the subject vault (net APY, share price basis).
Step 2: Identify the allocator audience (institutional, DeFi-native, both).
Step 3: Identify the underlying exposure (stablecoin yield, BTC yield, ETH yield,
        credit yield, T-bill yield, basis yield).
Step 4: Select five vaults that an allocator choosing the subject vault
        would simultaneously evaluate. Must include:
        - At least one vault with a different structure but same yield tier
        - At least one vault with a lower yield and lower risk profile
        - At least one vault from a different vault type competing for the same mandate
Step 5: Select one TradFi anchor. The most direct traditional finance equivalent.
        Always sourced from a confirmed public data source (FRED, fund factsheet,
        Bloomberg, exchange listing).

Always check knowledge/research/ for ingested research on comparable vaults
before going to the web. Prior investigation work carries forward.

## Rules

Factual side-by-side. Same fields for every vault. Every cell sourced and dated.
No judgment column. No advantage assessment. No conclusions.
Always include one TradFi anchor row.
If a field cannot be sourced for a comparable: state G2 or G3.
The allocator reads the table and draws their own conclusions.

---

## Standard Field Set (all vault types)

| Field | Format | Source | Notes |
|-------|--------|--------|-------|
| Vault / Product name | Text | Protocol website | |
| Vault type | VT-X | VaultDiligence classification | |
| Primary collateral / underlying | Text | Protocol docs | |
| TVL ($M) | Currency | DefiLlama / RWA.xyz | State date |
| Net APY to depositor | % | Vaults.fyi (share price basis) | Not gross. Not emissions-inflated. |
| Redemption timeline | T+N text | Protocol docs / operator disclosure | Standard, not stressed |
| Legal structure | Text | GLEIF / company registry | Entity type + jurisdiction |
| Primary audit firm(s) | Text | Solodit / protocol GitHub | Tier-1 named. Count not sufficient. |
| Bug bounty ($M) | Currency | Immunefi | Active programmes only |
| Custody model | Text | Protocol docs | On-chain / qualified custodian / prime broker |
| Source / date | URL + date | Per cell | State when data retrieved |

---

## Reference Comparable Sets by Dollar Mandate

These are starting points. The agent confirms current TVL and APY
from T1 sources before including any comparable. A comparable that
has wound down, been exploited, or changed structure materially
must be noted with that context, not silently excluded.

Confirmed live vaults only. No theoretical comparables.

### Dollar mandate: Stablecoin yield, institutional grade (~4-6% net APY)
Competing set: Ondo USDY, BlackRock BUIDL, a tokenized institutional credit fund,
a Centrifuge-tokenized CLO fund, Franklin OnChain US Government Money Fund.
TradFi anchor: 3M T-bill (FRED DGS3MO) or iShares Treasury Bond ETF.

### Dollar mandate: Stablecoin yield, DeFi-native (~5-9% net APY)
Competing set: Morpho/Steakhouse Prime USDC, Euler USDC, Aave USDC,
Morpho/Gauntlet USDC, Compound USDC.
TradFi anchor: 3M T-bill (FRED DGS3MO).

### Dollar mandate: Enhanced stablecoin yield (~7-12% net APY)
Competing set: a synthetic-dollar vault, a preferred-equity-backed vault, Maple Finance syrupUSDC,
Usual USD0++, Resolv USR (note exploit history if included).
TradFi anchor: Prime brokerage repo rate or 1Y Treasury.

### Dollar mandate: BTC yield
Competing set: Lombard LBTC, Corn BTCN, Solv BTC, Babylon BTC staking,
a preferred-equity-backed vault (a listed preferred instrument exposure).
TradFi anchor: BTC repo rate or the listed preferred instrument held directly.

### Dollar mandate: ETH yield / liquid staking
Competing set: Lido stETH, Rocket Pool rETH, EigenLayer restaking,
Pendle PT-stETH, Ether.fi eETH.
TradFi anchor: ETH staking yield vs risk-free spread.

### Dollar mandate: Institutional credit / private credit onchain
Competing set: Maple Finance syrupUSDC, Centrifuge senior tranches,
Goldfinch, Clearpool, TrueFi.
TradFi anchor: Investment grade corporate bond ETF (LQD) or CLO ETF (a tokenized CLO fund).

## Standard Comparable Sets by Vault Type

### VT-8 (TradFi-Primary / Onchain-Wrapped)

# Worked example: a preferred-equity-backed vault
Competing for the same dollar allocation. An allocator choosing a VT-8 vault
is simultaneously evaluating all of these. Group by yield tier.

| ID | Product | Vault type | Why competing for same dollar |
|----|---------|-----------|-------------------------------|
| S  | {vault-name} | VT-8 | Subject vault |
| | **SAME YIELD TIER (~6-10% net APY)** | | |
| C1 | a synthetic-dollar vault | VT-2 | Largest yield stablecoin. BTC/ETH delta-neutral vs a listed preferred instrument. Same APY range. Direct competitor for crypto-native allocator. |
| C2 | Usual USD0++ | VT-3 | RWA-backed yield stablecoin. T-bill underlying vs a listed preferred instrument. Competing for same stablecoin yield mandate. |
| C3 | Maple Finance syrupUSDC | VT-3 | Institutional credit yield. Unsecured vs secured contrast. Competing for same 8-10% yield target. |
| C4 | Morpho/Steakhouse Prime USDC | VT-1 | DeFi lending yield. On-chain vs TradFi-primary contrast. Same APY range. Competing for same USDC yield allocation. |
| | **LOWER YIELD TIER (~4-5% net APY)** | | |
| C5 | Ondo USDY | VT-3a | Tokenised T-bill. Same institutional audience. Lower yield, lower complexity. Conservative alternative. |
| C6 | BlackRock BUIDL | VT-3a | Tokenised MMF. Institutional anchor. Lowest risk in the comparison set. |
| | **BTC YIELD ALTERNATIVES** | | |
| C7 | Lombard LBTC | VT-5 | BTC restaking yield. Same BTC exposure as a listed preferred instrument but different mechanism. For allocator wanting BTC yield without equity wrapper. |
| | **TRADFI ANCHOR** | | |
| TF1 | the issuer's listed preferred instrument (direct) | N/A | The underlying instrument held directly. Removes the onchain wrapper. Shows what a preferred-equity-backed vault adds and what it costs. Source: [issuer site] |
| TF2 | 3-month T-bill | N/A | Risk-free rate baseline. Net APY premium over risk-free in bps. Source: FRED DGS3MO |

### VT-3a (a tokenized CLO fund and similar)
| ID | Product | Why included |
|----|---------|-------------|
| S | Subject vault | |
| C1 | Ondo USDY | Tokenised T-bills. Same institutional audience. Higher liquidity. |
| C2 | BlackRock BUIDL | Tokenised MMF. Institutional-grade benchmark. |
| C3 | a related Centrifuge-tokenized treasury fund | Same issuer family. Different underlying (gilts vs CLOs). |
| C4 | Maple Finance | Institutional credit. Undercollateralised vs overcollateralised contrast. |
| TF | a tokenized CLO fund ETF (NYSE listed) | TradFi anchor. Same CLO strategy, traditional wrapper. Daily liquidity. |

### VT-1 (Morpho lending vaults)
| ID | Product | Why included |
|----|---------|-------------|
| S | Subject vault | |
| C1 | Morpho/Gauntlet USDC | Benchmark Morpho vault. Same vault type. |
| C2 | Euler USDC | Alternative DeFi lending. Different architecture. |
| C3 | Aave USDC | Battle-tested protocol. Lower yield, lower risk. |
| C4 | a synthetic-dollar issuer the staked synthetic-dollar token | Yield stablecoin alternative. Different risk profile. |
| TF | 3-month T-bill | TradFi anchor. Risk-free rate baseline. Source: FRED DGS3MO. |

### VT-2 (Delta-neutral)
| ID | Product | Why included |
|----|---------|-------------|
| S | Subject vault | |
| C1 | a synthetic-dollar vault | Benchmark delta-neutral. Largest by TVL. |
| C2 | Gauntlet Basis Alpha | Institutional-grade basis strategy. |
| C3 | Resolv USR (pre-exploit) | Historical comparable. Exploit context required. |
| TF | Prime brokerage repo | TradFi anchor. BTC repo rate. |

---

## Differentiation Matrix

Remove the current "Subject advantage? Y/N/Partial" column. Replace with:

| Dimension | Subject vault | [Comparable C1] | [Comparable C2] | Source / date |
|-----------|---------------|-----------------|-----------------|---------------|
| Court-enforceable principal claim | [value] | [value] | [value] | [source] |
| Custody: qualified / SIPC / on-chain | [value] | [value] | [value] | [source] |
| Redemption: $10M standard timeline | [value] | [value] | [value] | [source] |
| Net APY (share price basis, no emissions) | [value] | [value] | [value] | [source] |
| Yield obligation: contractual / discretionary | [value] | [value] | [value] | [source] |
| Regulatory path for US institutional LP | [value] | [value] | [value] | [source] |
| Live performance track record (months) | [value] | [value] | [value] | [source] |
| All-in fee load (bps) | [value] | [value] | [value] | [source] |

The allocator reads the matrix and draws conclusions. No advantage column.
No VaultDiligence judgment on which vault is better.
