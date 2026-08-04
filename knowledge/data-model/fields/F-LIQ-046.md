# F-LIQ-046

**Field ID**: F-LIQ-046
**Category**: Liquidity
**Sub-Category**: Redemption Process
**Field Name**: Formal Redemption Capacity Limits — Contractual vs Target Settlement
**What to Collect / Question to Answer**: Are there formal daily or per-period redemption capacity limits, and what is the contractual settlement window versus the operator's target settlement window?
**Data Type**: Structured (capacity limit if any, contractual settlement window, target settlement window, cut-off time)
**Vault Types**: Exposure in {private-credit,structured-credit} OR Management=delegated-offchain-IM OR Structure=tranched OR Structure in {leveraged,looped} OR (Exposure in {equities,corporate-fixed-income,sovereign-fixed-income} AND venue=tradfi-primary)  (derived from VT-N; original "Vault Types" value: VT-3, VT-3a, VT-4, VT-7, VT-8)
**Collection Tier**: T2a
**Pillar(s)**: P9
**Primary Source**: Fund terms / subscription documents / protocol documentation stating capacity limits and the contractual settlement window
**Fallback Source**: Operator disclosure of any redemption cap, the contractual window, the target window, and the daily cut-off time
**Evidence Pathway**: Inspection-validatable: read the contractual settlement window and any formal capacity limit from the fund or protocol terms and compare against the operator's stated target window; the gap between contractual and target is the allocator's stress assumption.
**Institutional Standard**: Any formal daily or per-period redemption capacity limit is stated, and the contractual settlement window is recorded separately from the operator's target window, with the daily cut-off time. Where no formal capacity limit exists, that absence is stated explicitly rather than implied.
**Status**: Gap with action
**If Not Found — Gap Action**: Record whether a formal redemption capacity limit exists, the contractual settlement window, the target window, and the cut-off time. If the operator runs to a target faster than the contractual window, state both. If the contractual window is undocumented, classify G2 and name the fund document required.
**Source / Precedent**: a synthetic-dollar and CLO-fund a research advisory/LlamaRisk pack, 5 Jun 2026 (§Settlement): 'no formal daily redemption capacity limits... T+1 target (contractual three business days), 2pm ET cut-off.'
**Criterion ID(s)**: 9.3
