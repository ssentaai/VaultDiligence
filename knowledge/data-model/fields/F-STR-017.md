# F-STR-017

**Field ID**: F-STR-017
**Category**: Strategy Risk
**Sub-Category**: Restaking
**Field Name**: Restaking Reward-Token Dependency & Yield Composition
**What to Collect / Question to Answer**: What is the composition and denomination of the vault's restaking yield — ETH-denominated AVS service fees vs AVS reward tokens (often illiquid protocol tokens) vs points / airdrop expectations? What share of the headline APY depends on speculative or non-cash rewards? If AVS reward emissions or the points programme cease, what is the ETH-denominated floor yield?
**Data Type**: Structured — yield breakdown `{ source, denomination, share_of_apy_pct }` + `speculative_or_non_cash_share_pct` + `eth_denominated_floor_yield`.
**Vault Types**: `Strategy = restaking`
**Collection Tier**: T2
**Pillar(s)**: P6 (Credit / yield sustainability). *(propose; operator confirms)*
**Primary Source**: On-chain reward flows into the vault (token types and amounts) + AVS reward-emission schedules; protocol disclosure of points / airdrop dependency.
**Fallback Source**: Protocol / LRT-issuer yield-composition disclosure; third-party APY breakdowns, cited with date.
**Evidence Pathway**: Inspection-validatable — read the reward tokens actually received by the vault on-chain and classify by denomination; derive the non-cash / speculative share and the ETH-denominated floor by excluding emission-and-points components.
**Institutional Standard**: The yield is decomposed by source and denomination; the share that is AVS reward tokens or points (non-cash / speculative) is stated; the ETH-denominated floor yield if emissions and points stop is recorded — so the allocator sees how much of the APY is durable ETH-native fee income versus incentive emissions.
**Status**: Gap with action
**If Not Found — Gap Action**: E if reward flows and denominations are readable on-chain and dated. E(P) if the split is known but the points / airdrop value is unquantifiable (state it as unpriced). G2 if yield composition is disclosed to the protocol but not published. G3 if the protocol does not disclose yield composition. N/A never for a restaking vault — some yield composition is always determinable.
**Source / Precedent**: Sevim & Ferreira Torres, arXiv:2604.03274 — Renzo revenue is predicted by EigenLayer TVL, LRT yield, and multichain expansion, with a 1% yield increase → ≈ 3.82% revenue increase (yield-sensitivity and the incentive to chase higher-reward, higher-risk AVSs). LRT-market points-programme dependency.
**Criterion ID(s)**: propose at ratification.
