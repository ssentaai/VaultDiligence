# F-CTR-022

**Field ID**: F-CTR-022
**Category**: Smart Contract
**Sub-Category**: Deployment Integrity
**Field Name**: Deployment Provenance Triple
**What to Collect / Question to Answer**: Can the audit report, the source repository at a specific commit hash, and the on-chain deployed bytecode all be demonstrated to be the same code — i.e. exact commit and repo URL stated and validated identical across all three?
**Data Type**: Structured: { repo_url, deployment_commit_hash, audited_commit_hash, onchain_address, all_three_match: bool }
**Vault Types**: ALL
**Collection Tier**: T1
**Pillar(s)**: P7
**Primary Source**: On-chain: verified source on the block explorer plus the operator-stated repo URL and deployment commit; recompile that commit and confirm the resulting bytecode matches eth_getCode and that the audit report cites the same commit
**Fallback Source**: Operator deployment manifest stating repo URL and commit, cross-checked against the audit report's scope/commit section
**Evidence Pathway**: Inspection-validatable: obtain the stated repo URL and commit, recompile, and confirm the same commit hash appears in the audit report's scope and that the recompiled bytecode equals the on-chain bytecode.
**Institutional Standard**: A single commit hash and repo URL are stated and shown identical across the audit report, the source repository, and the on-chain bytecode, with zero unaudited changes between audited commit and deployed commit.
**Status**: Gap with action
**If Not Found — Gap Action**: If any leg of the triple is unstated or unverifiable, classify G2 and require the operator to specify the exact repo URL and deployment commit and confirm the audit covered that commit; if the audited commit differs from the deployed commit, classify the field as Investigate and demand the intervening change list.
**Source / Precedent**: Resolv, Mar 2026: the on-chain code that minted $80M of unbacked supply ($34M net loss) was never reconciled to the audited commit, so the audit covered a different state than the one holding depositor funds.
**Criterion ID(s)**: 7.1, RF02
