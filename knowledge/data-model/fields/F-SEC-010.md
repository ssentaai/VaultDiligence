# F-SEC-010

**Field ID**: F-SEC-010
**Category**: Security
**Sub-Category**: Infrastructure
**Field Name**: Privileged Key Storage Architecture
**What to Collect / Question to Answer**: Specific key storage method for each privileged role (minting, admin, pause, upgrade). AWS KMS / HSM / MPC / hardware wallet. Risk ranking: AWS KMS = highest risk; HSM/MPC = acceptable; hardware wallet multisig = good.
**Data Type**: Text (per role)
**Vault Types**: ALL
**Collection Tier**: T4
**Primary Source**: Operator CTO disclosure / security documentation
**Fallback Source**: Audit scope sections
**Pillar(s)**: P7
**D1**: Y
**D2**: Y
**D3**: Y
**D4**: Y
**D5**: Y
**Required?**: Y
**If Not Found — Gap Action**: Request from operator CTO. If cloud KMS only: RF41 trigger. Named counterparty: operator CTO.
**Criterion ID(s)**: 7.16
**Registered Sources (Fix 70)**: defisafety-process-reviews (candidate), immunefi-bug-bounty-programs
**Red Flag ID(s)**: RF41