# F-FIN-088

**Field ID**: F-FIN-088
**Category**: Financial
**Sub-Category**: AUM Trajectory
**Field Name**: AUM/TVL Trajectory and Peak-to-Current Decline
**What to Collect / Question to Answer**: What is the vault's AUM/TVL trajectory over the observation window, what is its peak value and date, what is the current value and date, what is the peak-to-current decline, and what attribution explains the change?
**Data Type**: Time series (AUM/TVL by date) + peak value/date + current value/date + decline + attribution text
**Vault Types**: ALL
**Collection Tier**: T1
**Pillar(s)**: P9
**Primary Source**: On-chain TVL series across all deployment chains (block explorer / Dune / protocol analytics)
**Fallback Source**: Protocol dashboard or operator reporting of AUM, reconciled to on-chain TVL where the asset is on-chain
**Evidence Pathway**: Inspection-validatable: read the TVL series on-chain across all chains, identify the peak value and date and the current value and date, compute the peak-to-current decline, and attribute the change to observable outflows or price moves.
**Institutional Standard**: AUM/TVL is reported as a dated trajectory with the peak value and date and the current value and date stated, the peak-to-current decline computed, and the decline attributed to redemptions versus mark-to-market rather than reported as a single point-in-time figure.
**Status**: Gap with action
**If Not Found — Gap Action**: Build the AUM/TVL trajectory from on-chain reads and compute peak-to-current decline with attribution; if off-chain AUM cannot be reconciled to on-chain TVL, classify the unreconciled portion as G2 naming the operator AUM report required.
**Source / Precedent**: a synthetic-dollar and CLO-fund diligence pack, AUM section: peak of $1,022M on 6 Jan 2026 declining to $409M on 9 May 2026, a peak-to-current decline of about three-fifths — surfaced as a MONITOR condition with attribution rather than as a headline TVL alone.
**Criterion ID(s)**: 9.10
**Registered Sources (Fix 70)**: a tokenization-pool data source
