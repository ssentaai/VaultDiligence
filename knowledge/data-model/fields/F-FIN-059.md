# F-FIN-059

**Field ID**: F-FIN-059
**Category**: Financial
**Sub-Category**: Capital Structure
**Field Name**: Capital Source Stickiness — Open-Term vs Committed TVL Split
**What to Collect / Question to Answer**: What % of vault TVL is open-term on-chain liquidity with no notice period (can leave in one block)? What % is committed institutional capital with a documented redemption notice? This is the vault's effective liability duration on the funding side.
**Data Type**: Percent
**Vault Types**: ALL
**Collection Tier**: T3
**Primary Source**: Vault depositor composition: request from operator. Check if subscription agreement applies to all depositors or only institutional tranche. Token holder analysis via Etherscan for wallet type distribution.
**Fallback Source**: Arkham Intelligence / Nansen wallet labels — institutional vs retail classification of top holders
**Pillar(s)**: P6,P9
**D3**: Y
**D4**: Y
**Required?**: Y
**If Not Found — Gap Action**: Open-term DeFi capital >70% of TVL with no lock-up = flag. Blume (Two Prime, March 2026): 'capital can leave at almost any time and has no loyalty or relationship behind it' — key duration mismatch signal.
**Criterion ID(s)**: 6.3 / 9.4
**Red Flag ID(s)**: RF27