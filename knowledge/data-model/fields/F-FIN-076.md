# F-FIN-076

**Field ID**: F-FIN-076
**Category**: Financial
**Sub-Category**: Yield Concentration
**Field Name**: Secondary Yield Floor — If Primary Source Fails
**What to Collect / Question to Answer**: If the primary yield source is suspended or depegs, what is the secondary yield? For a preferred-equity-backed vault: if the preferred-instrument dividend suspended, vault shifts to T-bill backing (USDat treasury yield ~3.5%). State floor yield and conditions triggering shift.
**Data Type**: Percent / Text
**Vault Types**: ALL
**Collection Tier**: T3
**Primary Source**: Vault documentation / RFC / operator disclosure
**Fallback Source**: On-chain vault composition logic
**Pillar(s)**: P6
**D1**: Y
**D2**: Y
**D3**: Y
**D4**: Y
**D5**: Y
**Required?**: Y
**If Not Found — Gap Action**: Read adaptive LTV model or equivalent in vault documentation. State floor yield. If no secondary source: floor = 0% — state this explicitly.
**Criterion ID(s)**: 6.8