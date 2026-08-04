# F-CTR-010

**Field ID**: F-CTR-010
**Category**: Contract
**Sub-Category**: Architecture
**Field Name**: Cross-Chain Bridge Used
**What to Collect / Question to Answer**: Bridge protocol name and contract address if cross-chain
**Data Type**: Text
**Vault Types**: Exposure in {private-credit,structured-credit} OR Structure in {leveraged,looped}  (derived from VT-N; original "Vault Types" value: VT-3,VT-7)
**Collection Tier**: T1
**Primary Source**: Contract: bridge() call / protocol docs / Wormhole/LayerZero explorer
**Pillar(s)**: P7
**D1**: Y
**D2**: Y
**D3**: Y
**Required?**: C
**If Not Found — Gap Action**: No fallback procedure = flag RF26. Note bridge exploit history (Wormhole $320M Feb 2022).
**Criterion ID(s)**: 7.7
**Registered Sources (Fix 70)**: etherscan-evm-explorer
**Red Flag ID(s)**: RF26