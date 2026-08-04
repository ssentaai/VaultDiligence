# F-COL-010

**Field ID**: F-COL-010
**Category**: Financial
**Sub-Category**: Collateral Contagion
**Field Name**: Underlying Portfolio Look-Through
**What to Collect / Question to Answer**: On a full look-through of the underlying portfolio, what is the per-position and per-manager concentration, the rating distribution, and are there any positions that breach the fund's stated per-position or per-manager mandate limits?
**Data Type**: Text + Percent (position HHI, manager HHI, top-N position shares, rating buckets, named breaches)
**Vault Types**: Exposure in {private-credit,structured-credit} OR Management=delegated-offchain-IM OR Structure in {leveraged,looped} OR (Exposure in {equities,corporate-fixed-income,sovereign-fixed-income} AND venue=tradfi-primary)  (derived from VT-N; original "Vault Types" value: VT-3, VT-3a, VT-7, VT-8)
**Collection Tier**: T3
**Pillar(s)**: P4
**Primary Source**: Fund holdings report / factsheet with full constituent list; investment management agreement stating mandate limits
**Fallback Source**: Administrator NAV pack or auditor-confirmed holdings schedule
**Evidence Pathway**: Inspection-validatable: inspect the published constituent holdings file to compute position-HHI, manager-HHI and the rating distribution, then read each share against the IMA's per-position and per-manager caps to enumerate breaches; mandate limits are Third-party-evidenced against the executed IMA.
**Institutional Standard**: Good looks like a constituent-level holdings schedule that resolves to named positions and managers, computed position and manager concentration indices, a rating distribution, and an explicit list of any holdings exceeding the fund's own per-position or per-manager limits — distinguishing aggregate quality claims from the actual measured distribution.
**Status**: Gap with action
**If Not Found — Gap Action**: Request the dated full constituent holdings file and the IMA's per-position/per-manager caps. If only aggregate or rating-bucket data is published, classify the per-position look-through as G2 and name the administrator as the entity holding the constituent schedule.
**Source / Precedent**: a synthetic-dollar and CLO-fund diligence (a research advisory + LlamaRisk, 5-7 Jun 2026): 20 CLO positions, all AAA, Madison Park 17.42 percent, top 10 equal to 83.3 percent, position HHI 5.4 percent, manager HHI 9.0 percent, with six positions exceeding the stated 5-percent-per-CLO limit because the Centrifuge wrapper mandate is intentionally more concentrated than the branded ETF.
**Criterion ID(s)**: 4.5, RF12
**Registered Sources (Fix 70)**: an issuer-disclosure source, a tokenization-pool data source, fitch-credit-ratings (candidate), a branded-fund factsheet source, kbra-credit-ratings (candidate), moodys-credit-ratings (candidate), sp-global-credit-ratings (candidate)
