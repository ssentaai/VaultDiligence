# F-FIN-087

**Field ID**: F-FIN-087
**Category**: Financial
**Sub-Category**: Carry Economics
**Field Name**: Epoch NAV-Recognition Cadence and Return Smoothing
**What to Collect / Question to Answer**: On what cadence is NAV recognised into the vault's reported return (per-epoch, daily, on settlement), and is the reported return series smoothed (for example by a moving average) such that the economically meaningful carry indicator differs materially from the raw per-period series an allocator would observe day to day?
**Data Type**: Enum cadence + Text (smoothing basis: raw / moving-average window / settlement-recognition lag)
**Vault Types**: Exposure in {private-credit,structured-credit} OR Management=delegated-offchain-IM OR (Exposure in {equities,corporate-fixed-income,sovereign-fixed-income} AND venue=tradfi-primary)  (derived from VT-N; original "Vault Types" value: VT-3, VT-3a, VT-8)
**Collection Tier**: T2
**Pillar(s)**: P9
**Primary Source**: Operator NAV-recognition policy + the raw and reported return series
**Fallback Source**: On-chain or published NAV series inspected for recognition lag and smoothing, with the basis stated
**Evidence Pathway**: Inspection-validatable: inspect the raw per-period NAV series against the reported return series to detect smoothing or recognition lag, measure the dispersion of the raw series, and state the cadence on which NAV is recognised.
**Institutional Standard**: The NAV-recognition cadence is stated, and any smoothing of the reported return (such as a moving-average window) is disclosed alongside the raw per-period series, so the allocator sees both the smoothed carry indicator and the underlying volatility rather than only the smoothed figure.
**Status**: Gap with action
**If Not Found — Gap Action**: Request the NAV-recognition policy and both the raw and reported return series; if only a smoothed series is published, classify the raw-series dimension as G2 naming the per-period NAV data required to assess smoothing and recognition lag.
**Source / Precedent**: a synthetic-dollar and CLO-fund diligence pack, Carry Economics section: raw daily return ranged from -53 to +55 with a standard deviation of 9.85, while a 30-day moving average was described as 'the economically meaningful carry indicator' — the gap between raw and smoothed series is itself the disclosure.
**Criterion ID(s)**: 9.4
