# F-FIN-077

**Field ID**: F-FIN-077
**Category**: Financial
**Sub-Category**: Yield Source Classification
**Field Name**: Yield Source Classification — Single-Value Rollup
**What to Collect / Question to Answer**: Single-value classification of the vault's yield source, derived from F-FIN-016 (yield source breakdown) and F-FIN-075 (single underlying concentration). Takes one of: `sustainable`, `incentive_driven`, `concentrated`, `mixed`. Rules in spec/yield-source-classification.md.
**Data Type**: Enum: `sustainable` | `incentive_driven` | `concentrated` | `mixed`
**Vault Types**: ALL
**Collection Tier**: T3
**Primary Source**: Derived from F-FIN-016 + F-FIN-075. Cite both source fields' evidence in the rationale.
**Fallback Source**: N/A — this field is a derived classification, not a primary observation.
**Pillar(s)**: P6
**D1**: Y
**D2**: Y
**D3**: Y
**D4**: Y
**D5**: Y
**Required?**: Y
**If Not Found — Gap Action**: This field cannot be G2 or G3 — its inputs (F-FIN-016, F-FIN-075) must resolve first. If either input is G2/G3, this field is N/A (not applicable until inputs resolve), not a gap to be filled separately.
**Criterion ID(s)**: 6.1, 6.8
**Red Flag ID(s)**: RF14
