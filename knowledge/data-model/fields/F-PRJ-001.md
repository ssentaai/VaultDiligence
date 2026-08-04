# F-PRJ-001

**Field ID**: F-PRJ-001
**Category**: Entity
**Sub-Category**: Project Gate
**Field Name**: Legal Entity Name — Verified
**What to Collect / Question to Answer**: Full registered legal name confirmed via GLEIF or domicile company registry. Not operator-stated.
**Data Type**: Text
**Vault Types**: ALL
**Collection Tier**: T1
**Primary Source**: GLEIF API: api.gleif.org/api/v1/fuzzycompletions?term={entity_name}
**Fallback Source**: OpenCorporates: api.opencorporates.com
**Pillar(s)**: P0
**D1**: Y
**D2**: Y
**D3**: Y
**D4**: Y
**D5**: Y
**Required?**: Y
**If Not Found — Gap Action**: Search GLEIF and domicile registry. If not found: request registration number from operator. Named counterparty: operator CFO or legal counsel.
**Criterion ID(s)**: 0.1