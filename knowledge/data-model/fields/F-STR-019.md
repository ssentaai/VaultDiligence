# F-STR-019

**Field ID**: F-STR-019
**Category**: Financial
**Sub-Category**: Hedge
**Field Name**: Short-Leg (Perp) Margin Regime & Liquidation Parameters
**What to Collect / Question to Answer**: On the short perpetual leg held at the exchange: what margin mode is used (cross vs isolated / portfolio margin), what is the maintenance-margin ratio and the resulting liquidation price as a % adverse move from entry, and is the position exposed to the venue's auto-deleveraging (ADL) queue? What price move on the underlying would trigger a maintenance-margin call or forced liquidation of the short, and what is the operator's top-up / de-risk procedure and its latency? This is the *exchange-leg* margin question — distinct from on-chain collateral liquidation and from tranche-level protection.
**Data Type**: Structured (margin mode; maintenance-margin %; liquidation-trigger move %; ADL exposure: y/n; margin top-up procedure + latency)
**Vault Types**: `Strategy = basis/funding-trade`
**Collection Tier**: T3
**Pillar(s)**: P5 — operator confirms
**Primary Source**: Operator hedge-operations documentation stating per-venue margin mode, maintenance-margin ratio, and margin-management procedure; exchange contract specifications for maintenance-margin tiers
**Fallback Source**: Audit/risk-review of the hedging operation; exchange public margin-tier schedule applied to disclosed position size
**Evidence Pathway**: Inspection-validatable against exchange contract specs + operator procedure: read the venue's maintenance-margin tier for the contract and position size, compute the liquidation-trigger move, and confirm the operator's documented top-up / de-risk procedure and latency.
**Institutional Standard**: The margin mode, maintenance-margin ratio, liquidation-trigger move, and ADL exposure are documented per venue, with a stated and time-bounded margin top-up / de-risk procedure, so the adverse move that would force-liquidate the short is a known figure rather than an assumption. (Fact to record.)
**Status**: Gap with action
**If Not Found — Gap Action**: Margin regime + liquidation-trigger move documented and reconciled to exchange specs: E. Operator states margin mode but not maintenance ratio / procedure: E(P). Undocumented margin regime on the short leg: G2, name the operator hedge-operations owner as the entity that must produce it. N/A only if there is no exchange-held short leg (e.g. fully DEX-perp or options-only).
**Source / Precedent**: `F-HED-002` covers *tranche-level* zero-liquidation (can the senior/principal tranche be liquidated) — not the operational margin mechanics of the short at the venue. `F-FIN-032`/`F-FIN-033`/`F-FIN-034`/`F-FIN-035` cover *on-chain lending-protocol* collateral ratio, liquidation threshold, and liquidation depth (`getUserAccountData` / `getReserveConfigurationData`) — a different venue and mechanism from CEX perp maintenance margin. A basis trade is force-liquidated on the short in a sharp up-move if maintenance margin is breached before top-up; this is the mechanism `F-HED-005` (rebalancing) assumes is survived but does not itself parameterise.
**Criterion ID(s)**: propose new under P5 (operator assigns); adjacent to criterion 5.2, 5.5
