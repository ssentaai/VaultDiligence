# F-HED-003

**Field ID**: F-HED-003
**Category**: Financial
**Sub-Category**: Hedge
**Field Name**: Perpetual / Spot Basis — Historical Maximum Spread
**What to Collect / Question to Answer**: What is the maximum observed basis spread between perpetual and spot price? What date? How long did it persist? Was yield impaired?
**Data Type**: Text
**Vault Types**: Structure=delta-neutral-synthetic OR Structure=tranched  (derived from VT-N; original "Vault Types" value: VT-2,VT-4)
**Collection Tier**: T1
**Primary Source**: Coinglass API: open-api.coinglass.com/api/pro/v1/futures/funding-rate/history?symbol={pair}&exchange={ex}
**Fallback Source**: Operator stress test disclosure — request historical basis data with dates
**Pillar(s)**: P5
**D3**: Y
**Required?**: C
**If Not Found — Gap Action**: No basis risk disclosure = flag. Basis >10% observed with no management mechanism = flag. March 2020: basis widened to eliminate delta-neutral thesis.
**Criterion ID(s)**: 5.3