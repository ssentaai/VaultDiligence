# F-ORC-002

**Field ID**: F-ORC-002
**Category**: Oracle
**Sub-Category**: Architecture
**Field Name**: Primary Oracle Provider(s)
**What to Collect / Question to Answer**: Named oracle provider(s) with contract addresses on each chain
**Data Type**: Text
**Vault Types**: ALL
**Collection Tier**: T1
**Primary Source**: On-chain: oracle() or priceFeed() call on vault contract / Etherscan read
**Fallback Source**: Protocol documentation
**Pillar(s)**: P3
**D1**: Y
**D2**: Y
**D3**: Y
**Required?**: Y
**If Not Found — Gap Action**: Read the contract. Confirm oracle address. Verify it matches documentation.
**Criterion ID(s)**: 3.1
**Registered Sources (Fix 70)**: blockscout-evm-explorer, direct-rpc-read, etherscan-evm-explorer
**Red Flag ID(s)**: RF08