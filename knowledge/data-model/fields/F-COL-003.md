# F-COL-003

**Field ID**: F-COL-003
**Category**: Financial
**Sub-Category**: Collateral Contagion
**Field Name**: Collateral Issuance Mechanism — Per Token
**What to Collect / Question to Answer**: For each accepted collateral: how is it issued? On-chain autonomous / off-chain signed two-step / algorithmic / RWA-backed. Off-chain signed = elevated risk (Resolv precedent).
**Data Type**: Text (per token)
**Vault Types**: Strategy=lending OR (Structure=multi-asset-pool AND Management=algorithmic AND Exposure=crypto-native) OR Structure in {leveraged,looped}  (derived from VT-N; original "Vault Types" value: VT-1,VT-6,VT-7)
**Collection Tier**: T3
**Primary Source**: Token issuer documentation / smart contract source code
**Fallback Source**: Audit reports for collateral token
**Pillar(s)**: P4
**D1**: P0
**D2**: Y
**D3**: N
**D4**: N
**D5**: Y
**Required?**: Y
**If Not Found — Gap Action**: Read smart contract issuance logic for each collateral token. Off-chain signed minting without on-chain cap = RF31 trigger.
**Criterion ID(s)**: 4.1 / 7.14
**Red Flag ID(s)**: RF31