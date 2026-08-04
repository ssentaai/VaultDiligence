# F-COL-011

**Field ID**: F-COL-011
**Category**: Financial
**Sub-Category**: Collateral Contagion
**Field Name**: Collateral Onboarding Controls
**What to Collect / Question to Answer**: What process gates the admission of a new collateral asset or market — is there a required audit re-scope, a timelock, an independent risk review, and an authority threshold — before the new asset can back the vault?
**Data Type**: Text / Y-N (per control: re-scope required, timelock present, review authority, threshold)
**Vault Types**: Strategy=lending OR (Structure=multi-asset-pool AND Management=algorithmic AND Exposure=crypto-native) OR Structure in {leveraged,looped}  (derived from VT-N; original "Vault Types" value: VT-1, VT-6, VT-7)
**Collection Tier**: T3
**Pillar(s)**: P4
**Primary Source**: Governance documentation / collateral-onboarding policy / listing process docs
**Fallback Source**: On-chain governance proposal history and contract admin role enumeration showing how prior assets were added
**Evidence Pathway**: Inspection-validatable: read the contract's collateral-admission function and its access control, and inspect the on-chain governance history of prior listings to see whether a timelock and re-audit actually preceded admission; the written gating policy is Third-party-evidenced against the operator's onboarding procedure.
**Institutional Standard**: Good looks like a documented and on-chain-enforced gate where a new collateral market cannot be admitted without a fresh audit re-scope covering the new asset, an enforced timelock, an independent risk review, and a defined authority threshold — closing the path by which a new or fictitious asset is admitted under a stale audit.
**Status**: Gap with action
**If Not Found — Gap Action**: Request the written collateral-onboarding policy and verify on-chain whether the admission function is timelocked and whether prior listings were preceded by an audit covering the specific new asset. If admission can occur without re-scope, state the gap and name the role holding admission authority. Flag RF12.
**Source / Precedent**: Buzko Krasnov legal analysis (27 Apr 2026) on Drift ($285M, 1 Apr 2026): a fictitious CarbonVote/CVT collateral token was admitted without an audit re-scope, despite the protocol having passed a Trail of Bits 2022 audit and a ClawSecure Feb 2026 audit — both of which predated the CVT and governance changes.
**Criterion ID(s)**: 4.1, RF12
