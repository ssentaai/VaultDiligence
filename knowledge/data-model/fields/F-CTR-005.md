# F-CTR-005

**Field ID**: F-CTR-005
**Category**: Contract
**Sub-Category**: Governance
**Field Name**: Multisig Configuration
**What to Collect / Question to Answer**: M-of-N multisig. Contract address on-chain.
**Data Type**: Text
**Vault Types**: ALL
**Collection Tier**: T1
**Primary Source**: Contract: GnosisSafe.getThreshold() + getOwners() / Etherscan
**Fallback Source**: Tally / Boardroom governance page
**Pillar(s)**: P7
**D1**: Y
**D2**: Y
**D3**: Y
**Required?**: Y
**If Not Found — Gap Action**: Single signer = flag. Low M (e.g. 2-of-10) = flag. Note signer count and threshold.
**Criterion ID(s)**: 7.2
**Registered Sources (Fix 70)**: blockscout-evm-explorer, direct-rpc-read, etherscan-evm-explorer
**Red Flag ID(s)**: RF03