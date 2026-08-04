# F-FIN-051

**Field ID**: F-FIN-051
**Category**: Financial
**Sub-Category**: Collateral
**Field Name**: Double-Collateral Detection — Re-use Across Protocols
**What to Collect / Question to Answer**: Is the same underlying asset identified as active collateral in two or more protocols simultaneously? Has the vault token been deposited as collateral elsewhere without disclosure?
**Data Type**: Y/N/Investigate
**Vault Types**: ALL
**Collection Tier**: T1
**Primary Source**: Etherscan token holder list for vault token — check if vault token appears in Morpho/Aave/Compound collateral lists
**Fallback Source**: Exponential.fi dependency map — cross-protocol collateral reuse detection
**Pillar(s)**: P4
**D3**: Y
**D4**: Y
**Required?**: Y
**If Not Found — Gap Action**: Check if vault token is used as collateral in any third-party lending market. Undisclosed = RF24. Double-counting destroys collateral quality assumptions.
**Criterion ID(s)**: 4.8
**Red Flag ID(s)**: RF24