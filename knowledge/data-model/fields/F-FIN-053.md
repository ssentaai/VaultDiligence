# F-FIN-053

**Field ID**: F-FIN-053
**Category**: Financial
**Sub-Category**: Credit
**Field Name**: Borrower Pool — Identity and Underwriting Standard
**What to Collect / Question to Answer**: For lending and credit vaults: who are the borrowers? Overcollateralised DeFi positions or institutional undercollateralised credit? What underwriting applies?
**Data Type**: Text
**Vault Types**: Strategy=lending OR Exposure in {private-credit,structured-credit} OR Structure=tranched OR (Exposure in {equities,corporate-fixed-income,sovereign-fixed-income} AND venue=tradfi-primary)  (derived from VT-N; original "Vault Types" value: VT-1,VT-3,VT-4,VT-8)
**Collection Tier**: T1
**Primary Source**: Morpho API: api.morpho.org/vaults/{address}/markets — confirm LLTV per market (overcollateralisation ratio). All positions >100% CR = evidenced.
**Fallback Source**: Credora rating pointer — request from operator for undercollateralised institutional lending
**Pillar(s)**: P6
**D3**: Y
**Required?**: C
**If Not Found — Gap Action**: Anonymous borrowers with no underwriting documentation = flag. Maple Finance $36M default: undercollateralised loans to Orthogonal Trading with no credit assessment.
**Criterion ID(s)**: 6.2