# F-ENT-005

**Field ID**: F-ENT-005
**Category**: Entity
**Sub-Category**: Fund Vehicle
**Field Name**: LEI (Legal Entity Identifier)
**What to Collect / Question to Answer**: 20-character alphanumeric LEI code
**Data Type**: Text
**Vault Types**: ALL
**Collection Tier**: T1
**Primary Source**: GLEIF API: api.gleif.org/api/v1/fuzzycompletions?term={entity_name}
**Fallback Source**: lei.bloomberg.com
**Pillar(s)**: P1
**D3**: Y
**Required?**: OPT
**If Not Found — Gap Action**: Search GLEIF by entity name. Note if LEI not registered — some BVI entities do not hold LEI.
**Criterion ID(s)**: 1.4
**Registered Sources (Fix 70)**: gleif-lei (candidate)
