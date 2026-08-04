# F-ORC-009

**Field ID**: F-ORC-009
**Category**: Oracle
**Sub-Category**: Resilience
**Field Name**: Fallback Oracle Configured
**What to Collect / Question to Answer**: Is there a fallback oracle if primary fails? What is it?
**Data Type**: Text
**Vault Types**: ALL
**Collection Tier**: T1
**Primary Source**: Contract: fallbackOracle() / protocol docs
**Fallback Source**: Protocol governance forum
**Pillar(s)**: P3
**D1**: Y
**D2**: Y
**D3**: Y
**Required?**: Y
**If Not Found — Gap Action**: Single oracle no fallback = flag especially for liquidation-dependent vaults.
**Criterion ID(s)**: 3.1
**Red Flag ID(s)**: RF08