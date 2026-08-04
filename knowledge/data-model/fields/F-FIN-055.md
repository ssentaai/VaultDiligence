# F-FIN-055

**Field ID**: F-FIN-055
**Category**: Financial
**Sub-Category**: Duration
**Field Name**: Liability Duration — Redemption Notice Period
**What to Collect / Question to Answer**: What is the effective liability duration? Depositor redemption notice period defines how quickly liabilities can be presented.
**Data Type**: Number (days)
**Vault Types**: Exposure in {private-credit,structured-credit} OR Structure=tranched OR (Exposure in {equities,corporate-fixed-income,sovereign-fixed-income} AND venue=tradfi-primary)  (derived from VT-N; original "Vault Types" value: VT-3,VT-4,VT-8)
**Collection Tier**: T3
**Primary Source**: Subscription agreement — redemption notice period clause. Protocol documentation for on-chain redemption timeline.
**Fallback Source**: Fund prospectus — redemption terms section
**Pillar(s)**: P6
**D3**: Y
**Required?**: C
**If Not Found — Gap Action**: Asset duration minus liability duration = mismatch. >90 day mismatch for credit vaults = flag. Document both and calculate gap.
**Criterion ID(s)**: 6.3