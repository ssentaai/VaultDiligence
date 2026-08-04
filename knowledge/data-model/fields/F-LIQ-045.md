# F-LIQ-045

**Field ID**: F-LIQ-045
**Category**: Liquidity
**Sub-Category**: Redemption Process
**Field Name**: Demonstrated Redemption Execution Event
**What to Collect / Question to Answer**: Is there a demonstrated single-day redemption execution event, and what were its dollar size, share of AUM, realised slippage, executing counterparty, and date?
**Data Type**: Structured (dollar size, share of AUM, slippage in basis points, counterparty, date, NAV/queue impact)
**Vault Types**: Exposure in {private-credit,structured-credit} OR Management=delegated-offchain-IM OR Structure=tranched OR Structure in {leveraged,looped} OR (Exposure in {equities,corporate-fixed-income,sovereign-fixed-income} AND venue=tradfi-primary)  (derived from VT-N; original "Vault Types" value: VT-3, VT-3a, VT-4, VT-7, VT-8)
**Collection Tier**: T2a
**Pillar(s)**: P9
**Primary Source**: On-chain redemption transaction record (redemption/burn event, settlement transfer) plus operator confirmation of counterparty and AUM context
**Fallback Source**: Operator or third-party diligence disclosure of the redemption event with dollar size, slippage, counterparty and date
**Evidence Pathway**: Third-party-evidenced: a named executing counterparty or third-party diligence pack attests the dollar size, share of AUM, slippage and date of the event, corroborated where possible against the on-chain redemption transaction; a demonstrated execution is what conditions a concentration finding.
**Institutional Standard**: A real, dated single-day redemption is recorded with its dollar size, share of AUM, realised slippage, executing counterparty, and confirmation of whether it caused NAV impairment or queue congestion. A demonstrated execution at scale is the evidence against which holder concentration is read.
**Status**: Gap with action
**If Not Found — Gap Action**: Locate the largest observed single-day redemption and record its dollar size, share of AUM, slippage in basis points, counterparty, date, and whether it impaired NAV or congested the queue. If no large redemption has been observed, state that exit capacity is unproven (G3) rather than inferring it from headline depth.
**Source / Precedent**: a synthetic-dollar and CLO-fund a research advisory/LlamaRisk pack, 5 Jun 2026: '$318.6M... Bank of America... ~5 bps... 11 Mar 2026... 42.8 percent of $744.8M AUM... no NAV impairment, no queue congestion.'
**Criterion ID(s)**: 9.8, RF37
