# F-HED-001

**Field ID**: F-HED-001
**Category**: Financial
**Sub-Category**: Hedge
**Field Name**: Hedge Strategy — Named Venues and Contract Specs
**What to Collect / Question to Answer**: What exchanges are used for hedging? What contract specifications? What are the position limits per venue? Is there multi-venue redundancy?
**Data Type**: Text
**Vault Types**: Structure=delta-neutral-synthetic OR Structure=tranched  (derived from VT-N; original "Vault Types" value: VT-2,VT-4)
**Collection Tier**: T4
**Primary Source**: Operator strategy documentation — request named venues, contract specs, position limits
**Fallback Source**: Governance forum — any published hedge documentation
**Pillar(s)**: P5
**D3**: Y
**Required?**: C
**If Not Found — Gap Action**: Undocumented hedge = flag. Proprietary strategy claim with no spec = flag. FTX concentration: single-venue dependency destroyed delta-neutral strategies.
**Criterion ID(s)**: 5.1