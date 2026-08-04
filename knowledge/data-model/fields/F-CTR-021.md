# F-CTR-021

**Field ID**: F-CTR-021
**Category**: Smart Contract
**Sub-Category**: Deployment Integrity
**Field Name**: Deployed-vs-Audited Bytecode Diff
**What to Collect / Question to Answer**: Has a byte-level diff been performed between the contracts currently live at the vault's on-chain addresses and the exact release the auditor reviewed, and is the diff null or are every divergence and its rationale enumerated?
**Data Type**: Enum: Identical / Divergent-enumerated / Divergent-unexplained / Not performed; plus diff artifact URL and divergence list
**Vault Types**: ALL
**Collection Tier**: T1
**Pillar(s)**: P7
**Primary Source**: On-chain: fetch runtime bytecode at the deployed proxy/implementation addresses via eth_getCode, compile the audited release at the stated commit, and compare the two byte arrays (metadata hash excluded)
**Fallback Source**: Operator-supplied bytecode-diff attestation naming the audit release and deployment address, or the auditor's deployment-verification note
**Evidence Pathway**: Inspection-validatable: re-compile the audited commit and diff its runtime bytecode against eth_getCode output at each live contract address, accepting only a null diff or one with every divergence enumerated and explained.
**Institutional Standard**: Live bytecode is byte-identical to the audited release, or every divergence is individually enumerated with a stated reason and none touches privileged or accounting logic; the diff artifact is published and reproducible by any third party.
**Status**: Gap with action
**If Not Found — Gap Action**: If no diff exists, classify G3 and require the operator to publish a reproducible bytecode diff naming the deployment address and audit commit; if a diff exists but divergences are unexplained, classify G2 and require a written rationale for each divergence and confirmation that none alters privileged or accounting paths.
**Source / Precedent**: Resolv, Mar 2026: deployed code carried authority the audited release did not constrain (SERVICE_ROLE minting), and $200K in collateral produced $80M minted ($34M net loss) because the deployed-vs-audited gap was never reconciled.
**Criterion ID(s)**: 7.1, RF02
