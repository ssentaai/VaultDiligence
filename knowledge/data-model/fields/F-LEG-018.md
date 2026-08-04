# F-LEG-018

**Field ID**: F-LEG-018
**Category**: Legal
**Sub-Category**: Cross-Chain Claim Seniority
**Field Name**: Cross-Chain Holder-Claims Seniority & Loss-Bearing Hierarchy
**What to Collect / Question to Answer**: Do bridged representations of the vault token carry an equal principal claim to the canonical-chain token, and if a bridge incident impairs one chain's representation is that loss socialised across all holders or borne only by holders on the affected chain? What does the documentation state about claims seniority across chains?
**Data Type**: Text
**Vault Types**: Strategy in {staking,restaking} OR Structure in {leveraged,looped} OR (Structure=multi-asset-pool AND Management=algorithmic AND Exposure=crypto-native)  (derived from VT-N; original "Vault Types" value: VT-5, VT-7, VT-6)
**Collection Tier**: T3
**Pillar(s)**: P1
**Primary Source**: Operator legal terms / token deployment documentation stating cross-chain claim symmetry and loss-allocation rule per chain
**Fallback Source**: Bridge / messaging-layer contract configuration read on each chain to determine which chain bears an impairment, cross-referenced with redemption terms
**Evidence Pathway**: Inspection-validatable: read the canonical and bridged token contracts plus the bridge/lockbox contract on each chain to confirm whether bridged supply is fully collateralised by locked canonical supply and which holders absorb a shortfall on a bridge failure.
**Institutional Standard**: Documentation states cross-chain symmetry explicitly: bridged representations carry an equal principal claim and a bridge incident is socialised across all holders rather than borne solely by holders on the affected chain, with the loss-bearing hierarchy named per chain.
**Status**: Gap with action
**If Not Found — Gap Action**: Request the operator state in writing, per chain, whether bridged tokens carry equal claim seniority and how a bridge-incident loss is allocated; undisclosed or ambiguous cross-chain claims seniority is a critical condition the allocator must price as a worse loss-given-default than headline TVL implies. Classify G2 if terms exist but are unpublished, G3 if no such allocation rule exists.
**Source / Precedent**: Aave §1.9 framework requirement: 'Cross-chain symmetry is stated explicitly: whether bridged representations carry equal claim... or whether a bridge incident is borne by holders on the affected chain rather than socialised... Undisclosed or ambiguous claims seniority... is a critical condition.' F-FIN-050 covers single-chain first-loss only; cross-chain seniority was an unfilled gap.
**Criterion ID(s)**: 1.3
