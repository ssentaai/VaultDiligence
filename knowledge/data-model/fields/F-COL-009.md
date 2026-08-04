# F-COL-009

**Field ID**: F-COL-009
**Category**: Financial
**Sub-Category**: Collateral Contagion
**Field Name**: Historical Collateral Drawdown Profile and Recurrence Conditions
**What to Collect / Question to Answer**: What is the worst historical peak-to-trough drawdown of the underlying collateral or reserve assets, over what window, and which specific market or structural conditions produced it and could reproduce it?
**Data Type**: Text + Percent (per asset, with dated drawdown events)
**Vault Types**: Strategy=lending OR (Structure=multi-asset-pool AND Management=algorithmic AND Exposure=crypto-native) OR Structure in {leveraged,looped} OR Exposure in {private-credit,structured-credit} OR Management=delegated-offchain-IM OR (Exposure in {equities,corporate-fixed-income,sovereign-fixed-income} AND venue=tradfi-primary)  (derived from VT-N; original "Vault Types" value: VT-1, VT-6, VT-7, VT-3, VT-3a, VT-8)
**Collection Tier**: T3
**Pillar(s)**: P4
**Primary Source**: Operator/curator drawdown disclosure; underlying-asset NAV or price time-series from the reserve manager
**Fallback Source**: Independent price/NAV history (issuer attestation series, custodian statements, or proxy-index reconstruction where the asset is too young)
**Evidence Pathway**: Inspection-validatable: reconstruct the peak-to-trough series from on-chain price history or published NAV files and inspect the dated trough events; the recurrence-condition narrative is Third-party-evidenced against the operator's written stress disclosure.
**Institutional Standard**: Good looks like a quantified worst-case historical drawdown for each collateral component with the exact date and magnitude, an explicit attribution of the conditions that caused it, and a stated view on whether those conditions can recur — extended via a named proxy index where the asset's own history is shorter than a full market cycle.
**Status**: Gap with action
**If Not Found — Gap Action**: Request the operator's documented drawdown history per reserve component; where the asset is younger than one full cycle, name the proxy index used and state the reconstructed worst-case with its date. Do not present a forward blast-radius estimate (F-COL-007) as a substitute for observed history.
**Source / Precedent**: Steakhouse Financial stablecoin-issuer DDQ v1.0, §4.6: 'What is the historical drawdown profile of the underlying collateral or reserves? What conditions contributed... and could cause them again?' Anchored by the tokenized CLO fund CLOSE-proxy extension: COVID drawdown of 8.33 percent on 24 Mar 2020 vs the live a tokenized CLO fund ETF max single-day decline of 0.60 percent (12 May 2022).
**Criterion ID(s)**: 4.5, 4.3
**Registered Sources (Fix 70)**: bluechip-stablecoin-ratings, a tokenization-pool data source, a branded-fund factsheet source
