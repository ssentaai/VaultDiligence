# F-STR-003

**Field ID**: F-STR-003
**Category**: Strategy Risk
**Sub-Category**: Lending — Liquidation
**Field Name**: Liquidation-Incentive & Close-Factor Calibration
**What to Collect / Question to Answer**: For each lending market the vault is exposed to, what is the liquidation incentive (liquidation bonus / discount) and the close factor (fraction of a position liquidatable per call — partial vs full), and how does the incentive compare to prevailing gas cost plus expected execution slippage at position size? The evidence question is whether liquidating a stressed position is economically rational for a third-party liquidator; if the reward is smaller than gas + slippage, liquidators rationally decline and the shortfall becomes shadow bad debt even where DEX depth exists. Source: on-chain market configuration + current gas / slippage estimate.
**Data Type**: Structured (liquidation-incentive per market; close factor; gas+slippage comparison at position size)
**Vault Types**: Strategy = lending
**Collection Tier**: T2
**Pillar(s)**: P4 (propose)
**Primary Source**: On-chain market configuration (`liquidationIncentive` / `LIF` / `lltv`-derived bonus; close factor) read from the lending contract
**Fallback Source**: Protocol risk-parameter documentation + a gas/slippage estimate at position size (cross-ref F-FIN-035 DEX depth, F-LIQ-044 atomic liquidity)
**Evidence Pathway**: Inspection-validatable — read the liquidation incentive and close factor on-chain and set them against gas + expected slippage at the vault's position size to state whether liquidation clears the position or leaves a residual; liquidator participation, not liquidity alone, determines whether bad debt accrues.
**Institutional Standard**: What a well-run vault evidences: the liquidation incentive and close factor per market are disclosed and on-chain-readable, and are stated alongside the gas + slippage a liquidator faces at position size, so the allocator can see whether liquidation is economically rational at that size rather than assuming a bidder will appear.
**Status**: Gap with action
**If Not Found — Gap Action**: Read the liquidation incentive and close factor on-chain (E) and record the gas+slippage comparison (E(P) where slippage is modelled rather than executed). If the incentive is not readable and undocumented, classify G2 and name the market. Where the incentive is below gas+slippage at position size, record that fact — the allocator decides what it means; do not score it.
**Source / Precedent**: Morpho liquidation docs, `docs.morpho.org/learn/concepts/liquidation/` (a large depeg can create "shadow bad debt" that never clears because liquidation is permanently unprofitable, discouraging liquidators). P4.3 anchor: Maker Black Thursday — fixed-price auction with no bidders minted DAI for $0, ~$8M bad debt.
**Criterion ID(s)**: propose 4.3 (operationalises the P4.3 pillar criterion, no existing field) · RF19 (leave for ratification)
