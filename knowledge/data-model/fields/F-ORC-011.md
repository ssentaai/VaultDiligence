# F-ORC-011

**Field ID**: F-ORC-011
**Category**: Oracle
**Sub-Category**: RWA-Specific
**Field Name**: NAV Source Chain (RWA only)
**What to Collect / Question to Answer**: For RWA vaults: what is the off-chain pricing source feeding the NAV oracle?
**Data Type**: Text
**Vault Types**: Exposure in {private-credit,structured-credit} OR Structure=tranched OR Structure in {leveraged,looped}  (derived from VT-N; original "Vault Types" value: VT-3,VT-4,VT-7)
**Collection Tier**: T3
**Primary Source**: Fund prospectus / administrator disclosure / oracle provider docs
**Fallback Source**: Particula or rating report
**Pillar(s)**: P3
**D1**: Y
**D2**: Y
**D3**: Y
**Required?**: C
**If Not Found — Gap Action**: S&P Global Pricing, Bloomberg, Refinitiv = institutional grade. Operator self-reported = flag.
**Criterion ID(s)**: 3.1 / 3.5