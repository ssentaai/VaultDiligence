# F-CUS-002

**Field ID**: F-CUS-002
**Category**: Financial
**Sub-Category**: TradFi Custody
**Field Name**: Rehypothecation Rights in Prime Brokerage Agreement
**What to Collect / Question to Answer**: Does the prime brokerage agreement grant the broker rehypothecation rights over client securities? Standard PB agreements typically include this. Explicit prohibition required.
**Data Type**: Text / Y/N
**Vault Types**: Exposure in {private-credit,structured-credit} OR Structure=tranched OR (Exposure in {equities,corporate-fixed-income,sovereign-fixed-income} AND venue=tradfi-primary)  (derived from VT-N; original "Vault Types" value: VT-3,VT-4,VT-8)
**Collection Tier**: T3
**Primary Source**: Prime brokerage agreement — must be reviewed directly. Not inferrable from operator description.
**Fallback Source**: Operator disclosure
**Pillar(s)**: P2
**D1**: N
**D2**: N
**D3**: Y
**D4**: Y
**D5**: N
**Required?**: Y
**If Not Found — Gap Action**: Request prime brokerage agreement from operator. Read Section covering margin lending and rehypothecation. Any permissive language = flag. Named counterparty: operator CFO and prime broker relationship manager.
**Criterion ID(s)**: 2.11
**Red Flag ID(s)**: RF01