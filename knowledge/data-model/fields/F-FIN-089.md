# F-FIN-089

**Field ID**: F-FIN-089
**Category**: Financial
**Sub-Category**: Stress Extension
**Field Name**: Proxy-Index Stress Extension — Correlation and Beta
**What to Collect / Question to Answer**: Where the vault's own price history is too short to capture a severe stress, which liquid proxy index is used to extend the stress assessment, what is the correlation and beta of the vault to that proxy, and what drawdown does the proxy exhibit in the worst historical episode beyond the vault's own live history?
**Data Type**: Text (named proxy index) + Numeric (correlation, beta, proxy stress drawdown)
**Vault Types**: Exposure in {private-credit,structured-credit} OR Management=delegated-offchain-IM OR (Exposure in {equities,corporate-fixed-income,sovereign-fixed-income} AND venue=tradfi-primary)  (derived from VT-N; original "Vault Types" value: VT-3, VT-3a, VT-8)
**Collection Tier**: T2
**Pillar(s)**: P9
**Primary Source**: Named proxy-index price history + the vault's own return series, used to compute correlation and beta
**Fallback Source**: Published proxy-index drawdown data from a market data provider, with the proxy selection and fit documented
**Evidence Pathway**: Inspection-validatable: compute correlation and beta between the vault's return series and the named proxy index over the overlapping period, then read the proxy's worst historical drawdown to extend the stress beyond the vault's own live history.
**Institutional Standard**: Where the vault's live history is too short for a severe-stress estimate, a liquid proxy index with documented correlation and beta is used to extend the drawdown assessment, the proxy is named, and its worst historical episode is stated so the allocator sees a stress beyond the benign live window.
**Status**: Gap with action
**If Not Found — Gap Action**: Identify the most defensible liquid proxy, compute correlation and beta over the overlap, and state the proxy's worst historical drawdown; if no adequate proxy exists, classify as G3 and state that the severe-stress estimate cannot be evidenced from available history.
**Source / Precedent**: a synthetic-dollar and CLO-fund diligence pack, Volatility and Drawdown section: the tokenized CLO fund ETF's own history showed a max single-day -0.60 (12 May 2022) and max drawdown -2.42 (14 Jul 2022), but the CLOSE proxy index (correlation 0.86, beta 0.95) extended the stress to -8.33 in the COVID episode of 24 Mar 2020.
**Criterion ID(s)**: 9.4
