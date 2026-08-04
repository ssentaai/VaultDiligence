# F-ENT-050

**Field ID**: F-ENT-050
**Category**: Entity
**Sub-Category**: Fund Administrator
**Field Name**: Entity Name + NAV Calc Frequency
**What to Collect / Question to Answer**: Administrator name and how often NAV is calculated (daily/weekly/real-time)
**Data Type**: Text
**Vault Types**: Exposure in {private-credit,structured-credit} OR Structure=tranched OR Structure in {leveraged,looped} OR (Exposure in {equities,corporate-fixed-income,sovereign-fixed-income} AND venue=tradfi-primary)  (derived from VT-N; original "Vault Types" value: VT-3,VT-4,VT-7,VT-8)
**Collection Tier**: T3
**Primary Source**: Fund prospectus / administrator website
**Fallback Source**: RWA.xyz profile
**Pillar(s)**: P3,P8
**D2**: Y
**D3**: Y
**Required?**: C
**If Not Found — Gap Action**: Independence of administrator from manager is critical. Same entity = flag.
**Criterion ID(s)**: 2.1 / 8.4
**Registered Sources (Fix 70)**: an issuer-disclosure source, gleif-lei (candidate)
