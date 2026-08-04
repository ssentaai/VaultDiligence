# Archetype Dimensions — Canonical Vocabulary

**Status:** Phase 1 (non-breaking) reference. Ratified design of record:
`an internal analysis` (v2, ratified 2026-07-09).

This file defines the multi-dimensional vault-archetype vocabulary. It is **definitions
only** — no field, pillar, gate, or command consumes it yet. VT-N remains the LIVE routing
key through Phase 2 and is retired in Phase 3 (see `vt-decomposition-map.md`). The
dimensions here exist in parallel, ready for the Phase 2 field migration.

A vault's archetype is a **primary economic-exposure classification + separable dimensions
+ risk-attributes + composition pointers + an as-of-date** — not a fixed tuple. Each
dimension is recorded and queryable independently; adding a dimension later does not
restructure the others.

> **PRIMARY: economic-exposure**
> **+ DIMENSIONS: {strategy, management, structure, seniority, liquidity, venue}**
> **+ RISK-ATTRIBUTES: {concentration, maturity, liquidity-mismatch}**
> **+ COMPOSITION: downward look-through pointer(s), if the backing includes another tokenized asset**
> **+ AS-OF-DATE (dated snapshot; the archetype can change)**

**Anchor-#4:** an archetype is descriptive classification — a vault's coordinates on
observable dimensions. No dimension computes or implies a score, rank, or verdict. The
allocator decides what a tuple means.

---

## PRIMARY — Economic Exposure (hierarchical: class -> sub-type)

What the vault is economically backed by / exposed to. **Hierarchical, one sub-level deep**
(ratified depth: "as granular as changes the diligence" — do not enumerate all leaves).
Accepts a **weighted set (Option A)** where a vault backs itself with a mix (a synthetic-dollar vault); a single
value where it does not (a tokenized CLO fund).

| Class | Sub-types (one level) |
|---|---|
| cash-equivalents | money-market-funds · commercial-paper · repo |
| sovereign-fixed-income | treasuries (bills/notes/bonds) · non-US-sovereign · agency · municipal · supranational |
| corporate-fixed-income | investment-grade · high-yield · floating-rate · convertible · preferred |
| structured-credit | **CLO** · CDO · MBS · ABS  (a tokenized CLO fund = structured-credit › CLO) |
| private-credit | direct-lending · marketplace/P2P · distressed · fund-finance · specialty-finance · real-estate-debt · securities-lending · consumer/asset-based |
| real-estate | equity-REIT · mortgage-REIT · private-real-estate |
| equities | dividend/equity-income · BDC · CEF · MLP · royalty-trust |
| infrastructure | infra-debt · infra-equity · PPA/project-revenue |
| commodities | metals · energy · agriculture |
| insurance-linked | cat-bonds · reinsurance · life-settlements |
| ip-royalties | media · pharma/biotech · patent/tech-licensing |
| crypto-native | crypto asset backing — ETH · BTC · LSTs · protocol tokens · stablecoins-as-backing |
| synthetic/derivative | a derivatives position, not a held asset — perp shorts · options |

Notes:
- **Stablecoins are not a class here.** A stablecoin is an instrument classification (the
  deferred regulatory axis). A yield-bearing stablecoin vault classifies by *what backs it* —
  e.g. a synthetic-dollar vault = the weighted set {crypto-native (staked ETH), synthetic/derivative (perp
  shorts), cash-equivalents (stables), sovereign-fixed-income (T-bills via BUIDL),
  structured-credit › CLO (a tokenized CLO fund)}.
- **An ETF / fund wrapper is not an exposure** — it classifies by what it holds + a
  structure value.

---

## DIMENSION — Strategy (what generates the yield) [the axis v1 lacked]

Distinct from exposure (what you hold) and management (who runs it). Accepts a **weighted
set** for multi-strategy vaults (a synthetic-dollar vault). **Extensible — versioned, not final** (new sources
feed new values):

- **passive-carry** — hold the asset, collect its native yield (a tokenized CLO fund CLO coupons; a T-bill fund)
- **lending** — supply to a lending market, earn borrow interest (utilization / rate-curve / liquidation risk)
- **LP/AMM-provision** — provide liquidity, earn fees (impermanent-loss risk)
- **staking** — native PoS staking rewards (slashing risk)
- **restaking** — restaking / AVS rewards (slashing + AVS-correlation risk)
- **basis/funding-trade** — cash-and-carry / delta-neutral perp funding (funding-rate-inversion risk)
- **options-premium** — sell options / volatility (tail-loss risk)
- **arbitrage/relative-value** — spread capture across venues / instruments
- **carry/curve** — fixed-income carry and curve positioning

---

## DIMENSION — Management (who or what runs it)

Scoped to *who runs it* (not what strategy it runs):

- **protocol-native/autonomous** — smart-contract logic, no active manager
- **delegated-offchain-IM** — an off-chain investment manager / sub-advisor (a tokenized CLO fund = an offchain issuer + investment manager)
- **algorithmic-vault** — an on-chain algorithm rebalances / executes
- **active-onchain-manager** — a curator / manager actively sets on-chain parameters
- **none-immutable** — no manager, no active control (a finding in itself)

---

## DIMENSION — Structure (how capital is arranged)

- **single-asset** · **multi-asset-pool** · **tranched** · **leveraged** · **looped** · **delta-neutral-synthetic**
- (a tokenized CLO fund = tranched; a synthetic-dollar vault = delta-neutral-synthetic)

---

## DIMENSION — Seniority (first-class for credit / structured exposures) [new]

Which tranche the vault sits in is decision-critical (a senior AAA tranche is a different
instrument from the first-loss tranche of the same CLO):

- **senior** · **mezzanine** · **junior/equity/first-loss** · **n/a (unstructured)**
- (a tokenized CLO fund = senior [AAA tranche]) — this is where the VT-9 "first-loss" orphan resolves: it
  was a *seniority* value, not a structure value.

---

## DIMENSION — Liquidity (how a holder exits) — OFFERED, paired with the mismatch attribute

- **daily** · **epoch** · **locked** · **gated**
- **Records offered/promised redemption terms, NOT achievable liquidity.** The gap between
  offered and the underlying's own liquidity is a first-order finding — captured as the
  **liquidity-mismatch** risk-attribute below, never hidden inside this value. (a tokenized CLO fund = daily
  offered against an illiquid CLO underlying = mismatch; a synthetic-dollar vault = seven-day the staked synthetic-dollar token cooldown
  against varying-liquidity backing.)

---

## FLAG — Venue-of-primary-risk

- **onchain-primary** · **tradfi-primary** · **hybrid**
- Modulates pillar weighting and assessment order, not partition. For hybrid vaults the
  venue differs *per risk type* (a tokenized CLO fund: credit risk = tradfi/the CLO fund manager; custody = hybrid;
  liquidity = onchain/redemption) — record venue per risk-family where it differs, not one
  flat flag. **Recorded, not inferred.**

---

## RISK-ATTRIBUTES (separable; NOT tuple coordinates; NEVER inferred from the tuple)

Where money is actually lost. **Not derivable from the tuple.** All three are
one-directional — they concern the vault's OWN exposures, never its holder base.

- **concentration** — concentration *of what the vault is exposed to* (a tokenized CLO fund: underlying CLO
  obligor concentration; a lending vault: single-borrower/collateral concentration). NOT
  token-holder concentration.
- **maturity/track-record** — time-since-inception, whether the strategy/manager has been
  tested through a cycle (a tokenized CLO fund: roughly twelve months, no credit cycle; ties to F-STD-006).
- **liquidity-mismatch** — a DERIVED cross-dimension signal: *offered* liquidity vs the
  *achievable* liquidity of the underlying. Computed from (exposure-liquidity vs
  offered-liquidity) and surfaced as a finding — the Liquidity value never stands alone as
  "liquid."

**Design statement (what the archetype does NOT classify, and why that is safe):** the
archetype gives a vault's structural / economic coordinates. Concentration, maturity, and
liquidity-mismatch are deliberately EXTERNAL, field-level assessments that must never be
inferred from the tuple. A vault can be pristine on every dimension and still be a bad
allocation. **A clean tuple is not a clean vault.**

---

## COMPOSITION — downward look-through only

**DD direction rule:** assess DOWN into what the vault holds / is-backed-by; NEVER up into
who holds it.

- `composes: <slug>` — a downward pointer, recorded ONLY from the subject vault's own
  disclosed backing when that backing includes another separately-assessed tokenized asset
  (a synthetic-dollar vault carries `composes: [a tokenized CLO fund, BUIDL]`).
- Reuses the pack-store reference pattern (`composes: <slug>`, analogous to
  `manager: <slug>`) — each asset assessed once, referenced by assets that hold it.
- **Pointer-with-flag, not full inline expansion.** No holder analysis, no upward pointers,
  no circular-contagion machinery.

---

## AS-OF-DATE — the archetype is a dated snapshot, not static

The fastest vaults change their own coordinates (a synthetic-dollar vault added a tokenized CLO fund to its backing in June
2026). The archetype carries an **as-of-date** and is re-assessable when the exposure /
strategy set changes. This ties to the built **F-STD-007 change-since-onboarding** dimension:
a material archetype change is a re-assessment trigger and a finding.

---

## Deferred — the regulatory/instrument axis

The legal/regulatory instrument classification (security / ABT / EMT / ART / fund-share)
remains a **separate deferred axis** (same asset can be classified oppositely by
jurisdiction). The framework can record its own evidenced view (jurisdiction-noted, not a
legal opinion), but it is added later, not part of this structural vocabulary.
