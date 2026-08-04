# F-TAX-001

**Field ID**: F-TAX-001
**Category**: Legal
**Sub-Category**: Tax Character
**Field Name**: Underlying Instrument Tax Character — ROC vs Income
**What to Collect / Question to Answer**: What is the tax character of distributions from the underlying yield instrument? Ordinary income / qualified dividend / return of capital / capital gain. Source: issuer SEC Form 8937 or equivalent.
**Data Type**: Text
**Vault Types**: ALL
**Collection Tier**: T1
**Primary Source**: SEC EDGAR Form 8937: search efts.sec.gov/LATEST/search-index?q=%228937%22+{issuer_name}
**Fallback Source**: Issuer investor relations
**Pillar(s)**: P10
**D1**: Y
**D2**: Y
**D3**: Y
**D4**: Y
**D5**: Y
**Required?**: Y
**If Not Found — Gap Action**: Search SEC EDGAR for Form 8937 filings from underlying instrument issuer. Strategy: 100% ROC in 2025. If non-US issuer: equivalent regulatory filing.
**Criterion ID(s)**: 10.6