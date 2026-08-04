# F-CTR-025

**Field ID**: F-CTR-025
**Category**: Smart Contract
**Sub-Category**: Source Availability
**Field Name**: Open-Source Status & Public Duration
**What to Collect / Question to Answer**: Are all contract components publicly source-available, for how long have they been public, and under what licence — including whether any component controlling funds or accounting remains closed?
**Data Type**: Structured: { all_components_public: bool, public_since_date, license, closed_components_list }
**Vault Types**: ALL
**Collection Tier**: T2
**Pillar(s)**: P7
**Primary Source**: On-chain: explorer source-verification status at each deployed address plus the public repository's first-commit/publish date; enumerate any deployed address whose source is unverified
**Fallback Source**: Public code repository history and licence file, cross-checked against the operator's documentation of which components are open versus closed
**Evidence Pathway**: Inspection-validatable: confirm each deployed contract is source-verified on the explorer, read the repository's publication date and licence file, and list any fund-controlling component that is not publicly available.
**Institutional Standard**: All components, especially any controlling funds or accounting, are source-available under a stated licence and have been public long enough to attract sustained adversarial review; any closed component is named as unverifiable risk.
**Status**: Gap with action
**If Not Found — Gap Action**: If components are closed or public duration is unstated, classify G2 and require the operator to publish the source or name the licence and publication date; treat any closed fund-controlling component as unverifiable risk and state it explicitly.
**Source / Precedent**: Resolv, Mar 2026: the off-chain signing path that authorised the $80M unbacked mint ($34M net loss) sat outside the publicly reviewable surface, so longer public exposure of the open components never subjected the actual attack path to adversarial review.
**Criterion ID(s)**: 7.4, RF02
