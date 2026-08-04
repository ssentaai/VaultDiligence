# F-STR-025

**Field ID**: F-STR-025
**Category**: Strategy Risk
**Sub-Category**: LP/AMM — Net Return
**Field Name**: Fee-Yield vs IL/LVR Break-Even — Net LP Return
**What to Collect / Question to Answer**: Over a stated window, does accrued swap-fee income exceed the sum of impermanent loss (F-STR-023), LVR (F-STR-024), and gas/rebalancing cost — i.e. is the LP position net-positive? State the four components in the same units and the net figure, and whether the break-even holds after emissions are excluded (see F-STR-030).
**Data Type**: Structured (fee income, IL, LVR, gas/rebalancing cost, net) all as % or bps over one window
**Vault Types**: Strategy = LP/AMM-provision
**Collection Tier**: T1 (calculated from the component fields)
**Pillar(s)**: P6 (Family B: Strategy Integrity) — propose; operator confirms
**Primary Source**: Calculated: swap-fee income (pool fee events attributable to the position) minus F-STR-023, F-STR-024, and on-chain gas/rebalancing cost, over one window
**Fallback Source**: Operator net-of-cost LP PnL disclosure with the components itemised
**Evidence Pathway**: Inspection-validatable — each component is separately evidenced (fee events on-chain, IL and LVR per their fields, gas from transaction receipts); the net is their sum over one consistent window.
**Institutional Standard**: A well-run vault states net LP return with all four components itemised over a consistent window, and discloses whether the position is net-positive before and after token emissions. Advertising a fee APR without netting IL + LVR + gas is the gap — a pool can present a high fee APR and still be net-negative to the LP.
**Status**: Gap with action
**If Not Found — Gap Action**: If all components are available, compute the net and classify E. If some components are disclosed but IL or LVR is missing, classify E(P) and name the missing component. If only a gross fee APR is published, classify G3 and require the operator to publish a net-of-cost figure. Cross-reference F-FIN-014 (net yield to investor) and F-FIN-016 (yield source breakdown) — this field is the LP-specific extension that nets the cost-of-LP, which those fields do not.
**Source / Precedent**: Milionis, Moallemi & Roughgarden, "Automated Market Making and Arbitrage Profits in the Presence of Fees", arXiv:2305.14604 (2023) — models when swap fees do and do not offset arbitrage/LVR cost; fees scale down arbitrage profit by the fraction of blocks presenting profitable trading opportunities. Keyrock 2025 gross-vs-net precedent (P6 criterion 6.6) is the general net-yield analogue.
**Criterion ID(s)**: propose at ratification (adjacent to 6.1 / 6.6)
