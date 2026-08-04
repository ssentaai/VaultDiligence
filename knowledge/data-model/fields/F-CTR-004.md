# F-CTR-004

**Field ID**: F-CTR-004
**Category**: Contract
**Sub-Category**: Governance
**Field Name**: Upgrade Timelock (hours)
**What to Collect / Question to Answer**: Minimum delay on contract upgrades in hours
**Data Type**: Number
**Vault Types**: ALL
**Collection Tier**: T1
**Primary Source**: Contract: TimelockController.getMinDelay() / ProxyAdmin timelock
**Fallback Source**: Etherscan contract read
**Pillar(s)**: P7
**D1**: Y
**D2**: Y
**D3**: Y
**Required?**: Y
**If Not Found — Gap Action**: <12 hours = flag. 0 = auto-disqualifier. 48h+ = strong. Note emergency vs standard timelock separately.
**Criterion ID(s)**: 7.2
**Registered Sources (Fix 70)**: direct-rpc-read, etherscan-evm-explorer
**Red Flag ID(s)**: RF03