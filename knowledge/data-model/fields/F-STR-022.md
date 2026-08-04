# F-STR-022

**Field ID**: F-STR-022
**Category**: Financial
**Sub-Category**: Loss Isolation
**Field Name**: Reserve / Insurance Fund Adequacy vs Negative-Funding Burn
**What to Collect / Question to Answer**: Given the backstop whose existence, size, and enforceability `F-FIN-081` records: how many days of negative funding *at position size* can it absorb, measured against the strategy's own historical maximum negative-funding streak and burn rate (`F-HED-004`)? State the reserve size, the modelled daily burn under a defined negative-funding scenario, the implied coverage in days, and the fund's disclosed drawdown/replenishment policy — with source and date. This is the *adequacy-ratio* question, distinct from `F-FIN-081`'s *existence/size/enforceability* question.
**Data Type**: Structured (reserve size + date; modelled daily burn at position size; implied coverage in days; drawdown/replenishment policy; source)
**Vault Types**: `Strategy = basis/funding-trade`
**Collection Tier**: T2a
**Pillar(s)**: P9 (propose; cross-refs P5) — operator confirms
**Primary Source**: Operator reserve-fund disclosure / on-chain reserve address balance + drawdown methodology; funding-rate history (`F-HED-004` source, e.g. Coinglass) to size the burn
**Fallback Source**: Independent reserve-adequacy analysis (e.g. risk-provider drawdown methodology); governance-forum reserve-fund updates
**Evidence Pathway**: Inspection-validatable: read the reserve balance (on-chain or attested) and the disclosed drawdown/replenishment policy, model the daily burn under the strategy's historical maximum negative-funding streak at position size, and state the implied coverage in days.
**Institutional Standard**: The reserve/insurance fund's size, its modelled daily burn under a defined negative-funding scenario at position size, the implied coverage in days, and its drawdown/replenishment policy are recorded with source and date — so the allocator can see whether the backstop covers the strategy's own worst observed negative-funding streak, not merely that a backstop exists. (Fact to record, never a pass/fail threshold.)
**Status**: Gap with action
**If Not Found — Gap Action**: Reserve size + modelled burn + coverage-in-days assembled from primary data: E. Reserve size disclosed but burn/coverage not modelled: E(P). Reserve exists but size undisclosed: G2 (name the operator as the entity that must disclose it). No reserve/backstop at all: state it as the finding (E on the absence; note RF35 per `F-FIN-081`). N/A if the strategy carries no negative-funding exposure (e.g. pure spot).
**Source / Precedent**: `F-FIN-081` captures the *existence, size, and enforceability* of a bad-debt-isolation / recapitalisation backstop (P9, RF35) generically; it does not test *adequacy against the negative-funding burn rate*. a synthetic-dollar issuer reserve fund — "a source of capital to pay for periods of negative funding" that "step[s] in … when the combined revenue … is negative" (the issuer documentation; the issuer documentation, retrieved 2026-07-09; historical longest consecutive negative streak stated as 13 days, 8.84% of days sum-negative). CryptoQuant/LlamaRisk have flagged reserve-fund *adequacy* as the monitoring metric for a synthetic-dollar vault holders (a published risk-methodology; reserve-fund adequacy warning, Yahoo Finance/CryptoQuant, 2026).
**Criterion ID(s)**: propose new under P9 (operator assigns); relates to criterion 9.4, RF35, and P5 criterion 5.4
**Cross-references**: F-FIN-081 (backstop existence/enforceability, extended here with the adequacy-ratio facet); F-STR-005 (bad-debt loss-order facet).
