# F-LEG-012

**Field ID**: F-LEG-012
**Category**: Legal
**Sub-Category**: Tax
**Field Name**: Tax Treatment — Depositor Tax Opinion
**What to Collect / Question to Answer**: Is there a tax counsel opinion on depositor tax treatment? Is the deposit a taxable event? Staking rewards as income? K-1 or 1099 reporting?
**Data Type**: Text
**Vault Types**: Exposure in {private-credit,structured-credit} OR Structure=tranched OR (Exposure in {equities,corporate-fixed-income,sovereign-fixed-income} AND venue=tradfi-primary)  (derived from VT-N; original "Vault Types" value: VT-3,VT-4,VT-8)
**Collection Tier**: T4
**Primary Source**: Operator tax counsel disclosure — request tax opinion document
**Fallback Source**: Protocol documentation — any published tax guidance
**Pillar(s)**: P10
**D3**: Y
**Required?**: C
**If Not Found — Gap Action**: No tax guidance for US family office or pension = blocking. On-chain yield events (harvest, rebase) may constitute taxable income. Allocator must engage own tax counsel regardless.
**Criterion ID(s)**: 10.5