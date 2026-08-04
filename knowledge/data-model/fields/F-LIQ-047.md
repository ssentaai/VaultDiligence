# F-LIQ-047

**Field ID**: F-LIQ-047
**Category**: Liquidity
**Sub-Category**: Redemption Stack
**Field Name**: Observed Redemption Settlement Distribution
**What to Collect / Question to Answer**: Across observed redemptions, what is the settlement-time distribution — P90, maximum, the share settling beyond the target window, the trend over time, and the sample size?
**Data Type**: Structured (P90 days, max days, share beyond target, trend statistic, n observations)
**Vault Types**: Exposure in {private-credit,structured-credit} OR Management=delegated-offchain-IM OR Structure=tranched OR Structure in {leveraged,looped} OR (Exposure in {equities,corporate-fixed-income,sovereign-fixed-income} AND venue=tradfi-primary)  (derived from VT-N; original "Vault Types" value: VT-3, VT-3a, VT-4, VT-7, VT-8)
**Collection Tier**: T2a
**Pillar(s)**: P9
**Primary Source**: On-chain redemption-to-settlement timestamps across the observed series (request event to settlement transfer)
**Fallback Source**: Operator or third-party diligence settlement-time series with stated sample size and trend statistic
**Evidence Pathway**: Inspection-validatable: timestamp each observed redemption from request to settlement on-chain, compute the P90 and maximum, the share settling beyond the target window, a trend statistic, and the sample size; a sparse sample is itself a stated limitation.
**Institutional Standard**: The observed settlement-time distribution is reported with its P90 and maximum, the share of redemptions settling beyond the target window, a trend statistic, and the sample size. Where the sample is sparse, the small-n limitation is stated rather than presented as a settled distribution.
**Status**: Gap with action
**If Not Found — Gap Action**: Compute the P90, maximum, share-beyond-target, trend, and sample size from observed redemption settlement timestamps. If the sample is sparse, state n and flag the distribution as provisional. If settlement timestamps are not observable on-chain and not disclosed, classify G2 and name the settlement record required.
**Source / Precedent**: a synthetic-dollar and CLO-fund a research advisory/LlamaRisk pack, 5 Jun 2026 (§Settlement): 'P90 1.98d, max 3.71d; Mann-Kendall tau=0.078, p=0.554; n=30 sparse.'
**Criterion ID(s)**: 9.8, RF37
