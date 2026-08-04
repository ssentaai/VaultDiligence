# F-FIN-061b

**Field ID**: F-FIN-061b
**Category**: Financial
**Sub-Category**: Collateral Parameters
**Field Name**: On-Chain Supply Cap vs Announced Deployment Cap
**What to Collect / Question to Answer**: What is the actual on-chain supply cap for this collateral in the lending market? Compare to announced deployment cap. Flag any discrepancy. a tokenized CLO fund precedent: $100M announced vs $40M actual Aave Horizon supply cap.
**Data Type**: USD + Boolean discrepancy flag
**Vault Types**: Structure in {leveraged,looped} OR (Exposure in {equities,corporate-fixed-income,sovereign-fixed-income} AND venue=tradfi-primary)  (derived from VT-N; original "Vault Types" value: VT-7,VT-8)
**Collection Tier**: T1
**Primary Source**: Aave Horizon contract: getConfiguration() + supplyCap field
**Pillar(s)**: P9
**Fallback Source**: Protocol documentation