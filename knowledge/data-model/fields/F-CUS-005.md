# F-CUS-005

**Field ID**: F-CUS-005
**Category**: Financial
**Sub-Category**: TradFi Custody
**Field Name**: TradFi Insurance Coverage — SIPC Excess, Fidelity Bond
**What to Collect / Question to Answer**: Beyond base SIPC ($500K): does the prime broker carry excess SIPC coverage? Fidelity bond? E&O insurance? State amounts, carriers, scope.
**Data Type**: Text / Currency
**Vault Types**: Exposure in {private-credit,structured-credit} OR Structure=tranched OR (Exposure in {equities,corporate-fixed-income,sovereign-fixed-income} AND venue=tradfi-primary)  (derived from VT-N; original "Vault Types" value: VT-3,VT-4,VT-8)
**Collection Tier**: T3
**Primary Source**: Prime broker disclosure / insurance certificate
**Fallback Source**: Operator disclosure
**Pillar(s)**: P2
**D1**: N
**D2**: N
**D3**: Y
**D4**: Y
**D5**: N
**Required?**: Y
**If Not Found — Gap Action**: Request insurance documentation from prime broker. Standard institutional prime brokers carry excess SIPC. If the prime broker: confirm excess SIPC amount.
**Criterion ID(s)**: 2.11
**Registered Sources (Fix 70)**: sipc-member-list (candidate)
