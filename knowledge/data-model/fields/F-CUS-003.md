# F-CUS-003

**Field ID**: F-CUS-003
**Category**: Financial
**Sub-Category**: TradFi Custody
**Field Name**: Execution / Custody Separation
**What to Collect / Question to Answer**: Are execution and custody functions held by separate entities? Separation reduces single point of failure and conflict of interest. a preferred-equity-backed vault: the execution broker (execution) / the prime broker (custody) — separated.
**Data Type**: Text / Y/N
**Vault Types**: Exposure in {private-credit,structured-credit} OR Structure=tranched OR (Exposure in {equities,corporate-fixed-income,sovereign-fixed-income} AND venue=tradfi-primary)  (derived from VT-N; original "Vault Types" value: VT-3,VT-4,VT-8)
**Collection Tier**: T3
**Primary Source**: Vault documentation / RFC / operator disclosure
**Fallback Source**: Prime brokerage agreement
**Pillar(s)**: P2
**D1**: N
**D2**: N
**D3**: Y
**D4**: Y
**D5**: N
**Required?**: Y
**If Not Found — Gap Action**: Confirm from vault documentation whether execution and custody are separated. Name both entities.
**Criterion ID(s)**: 2.11