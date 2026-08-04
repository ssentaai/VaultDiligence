# F-FIN-049

**Field ID**: F-FIN-049
**Category**: Financial
**Sub-Category**: Counterparty
**Field Name**: Trading Counterparty List — Named Exchanges and OTC Desks
**What to Collect / Question to Answer**: For strategies using exchanges or OTC desks: what are the named counterparties? What % of positions are held at each?
**Data Type**: Text
**Vault Types**: Structure=delta-neutral-synthetic OR Structure=tranched OR (Exposure in {equities,corporate-fixed-income,sovereign-fixed-income} AND venue=tradfi-primary)  (derived from VT-N; original "Vault Types" value: VT-2,VT-4,VT-8)
**Collection Tier**: T4
**Primary Source**: Operator disclosure — request counterparty list with % allocation per venue
**Fallback Source**: Coinglass OI by exchange: open-api.coinglass.com — confirm where perp positions are held
**Pillar(s)**: P2
**D3**: Y
**Required?**: C
**If Not Found — Gap Action**: Applicable VT-2 and VT-4 only. Undisclosed counterparties = flag. >30% single exchange = flag. FTX failure mode.
**Criterion ID(s)**: 2.6