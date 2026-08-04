# F-STR-001

**Field ID**: F-STR-001
**Category**: Strategy Risk
**Sub-Category**: Lending — Rate Model
**Field Name**: Interest-Rate-Model Curve Shape & Reactivity
**What to Collect / Question to Answer**: For each lending market the vault supplies, what interest-rate model governs the borrow rate, and what are its parameters — base rate, the kink / optimal-utilisation point, the pre-kink slope, the post-kink (jump) slope, or, for an adaptive model, the target utilisation and adjustment speed? State whether the curve is reactive enough that, at the utilisation level a supplier run would produce, the borrow rate rises steeply enough to attract repayment / new supply rather than leaving the market pinned near 100% utilisation. Source: the IRM contract read on-chain and the protocol's rate-model documentation.
**Data Type**: Structured (IRM contract address + type; base rate; kink/optimal-utilisation; slope1; slope2/jump; adaptive target + speed where applicable)
**Vault Types**: Strategy = lending
**Collection Tier**: T1
**Pillar(s)**: P9 (propose; operator confirms — secondary P4)
**Primary Source**: On-chain read of the market's IRM contract (e.g. Morpho `AdaptiveCurveIRM`, Aave `DefaultReserveInterestRateStrategy`, Compound `JumpRateModel`) + protocol rate-model docs
**Fallback Source**: Protocol risk dashboard reporting the configured rate curve per market
**Evidence Pathway**: Inspection-validatable — read the IRM parameters from the market's rate-strategy contract and reconstruct the borrow-rate-vs-utilisation curve; the kink and jump slope determine whether a utilisation spike is self-correcting or self-reinforcing.
**Institutional Standard**: What a well-run vault evidences: the IRM type and every curve parameter are disclosed and on-chain-readable per market, so the borrow-rate response at stress utilisation can be reconstructed and the self-correction (or absence of it) is observable rather than assumed.
**Status**: Gap with action
**If Not Found — Gap Action**: Read the IRM contract and record the curve parameters (E). If the parameters are readable but the model is undocumented, state the reconstructed curve and mark the model-intent narrative E(P). If the market uses an unverifiable or off-chain rate source, classify G2 and name the market and the rate authority. N/A only if the vault supplies no interest-bearing lending market (state why).
**Source / Precedent**: Morpho Blue variable-rate market model, `docs.morpho.org/learn/concepts/market/` (AdaptiveCurveIRM targets a utilisation point and adjusts the rate over time); Aave/Compound jump-rate ("kink") model. Mechanism anchor: during the USDC depeg (Mar 2023) utilisation on major lending pools spiked and jump-rate borrow costs rose sharply — the curve shape governs whether that pressure clears or freezes the market.
**Criterion ID(s)**: propose 9.1 / 9.4 (leave for ratification)
