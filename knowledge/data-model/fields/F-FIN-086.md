# F-FIN-086

**Field ID**: F-FIN-086
**Category**: Financial
**Sub-Category**: Carry Economics
**Field Name**: Net Carry Spread over SOFR — Methodology, Floor, Negative-Quarter Handling
**What to Collect / Question to Answer**: What is the vault's net carry spread over SOFR, computed by what stated methodology, against what disclosed floor, and how are negative-carry quarters recognised and disclosed rather than smoothed away?
**Data Type**: Numeric (basis points over SOFR per period) + methodology statement + floor + negative-quarter treatment
**Vault Types**: Exposure in {private-credit,structured-credit} OR Management=delegated-offchain-IM OR (Exposure in {equities,corporate-fixed-income,sovereign-fixed-income} AND venue=tradfi-primary)  (derived from VT-N; original "Vault Types" value: VT-3, VT-3a, VT-8)
**Collection Tier**: T2
**Pillar(s)**: P9
**Primary Source**: Operator/fund carry methodology disclosure + periodic NAV series used to derive realised carry
**Fallback Source**: Computed from the on-chain or published NAV series against the published SOFR fixing, with the derivation basis stated
**Evidence Pathway**: Inspection-validatable: take the periodic NAV series and the published SOFR fixings for the same periods, compute the net spread per the stated methodology, and verify any disclosed floor and the treatment of negative-carry quarters against the series.
**Institutional Standard**: Net carry over SOFR is computed by a stated, reproducible methodology against a disclosed floor, and negative-carry quarters are recognised and disclosed explicitly rather than netted or smoothed; the spread is sourced to a period NAV series the allocator can independently recompute.
**Status**: Gap with action
**If Not Found — Gap Action**: Request the carry methodology, floor, and negative-quarter treatment, and recompute the spread from the NAV series against SOFR; if the NAV series or methodology is not available, classify as G2 naming the period NAV series and methodology document required to close it.
**Source / Precedent**: a synthetic-dollar and CLO-fund diligence pack, Carry Spread section: quarterly mean carry of +61.1 basis points against a disclosed 50 basis-point floor, with Q1 2026 at -62.0 basis points — a negative-carry quarter that must be recognised explicitly, not smoothed.
**Criterion ID(s)**: 9.4
