# F-RIS-007

**Field ID**: F-RIS-007
**Category**: Risk
**Sub-Category**: Incident
**Field Name**: NAV-Decline-to-Liquidation Headroom
**What to Collect / Question to Answer**: For leveraged holders of this asset on a lending protocol, how far can NAV decline before the position is liquidated — what is the computed headroom between the liquidation LTV and the current borrow position?
**Data Type**: Percent (computed headroom, with the LT and current-LTV inputs)
**Vault Types**: Structure in {leveraged,looped} OR Management=delegated-offchain-IM OR (Exposure in {equities,corporate-fixed-income,sovereign-fixed-income} AND venue=tradfi-primary)  (derived from VT-N; original "Vault Types" value: VT-7, VT-3a, VT-8)
**Collection Tier**: T3
**Pillar(s)**: P7
**Primary Source**: Lending-protocol risk parameters (liquidation threshold, current LTV) read on-chain or from governance config
**Fallback Source**: Third-party risk report stating the leveraged-holder parameters and computed headroom
**Evidence Pathway**: Inspection-validatable: read the liquidation threshold and the current borrow LTV for the leveraged position from the lending protocol's on-chain configuration and compute the headroom directly; the formula and its inputs are fully reproducible by anyone with the addresses.
**Institutional Standard**: Good looks like a computed NAV-decline-to-liquidation headroom for the material leveraged-holder positions, stated as a percentage with its liquidation-threshold and current-LTV inputs shown, so the allocator can see how small a move in the underlying NAV would trigger liquidation and second-order queue pressure rather than relying on a qualitative oracle-link statement.
**Status**: Gap with action
**If Not Found — Gap Action**: Read the lending-protocol liquidation threshold and current LTV for the leveraged positions and compute headroom as (1 minus current-LTV divided by liquidation-LTV). If the position parameters are not observable, state the gap and name the protocol whose config must be read.
**Source / Precedent**: a synthetic-dollar and CLO-fund diligence (a research advisory, Jun 2026), Wrong-way-risk section: computed headroom of (1 minus 0.80/0.875) times 100 equals 8.57 percent for the leveraged a tokenized CLO fund position, against the Resolv precedent of a $100M a tokenized CLO fund loop on Aave Horizon.
**Criterion ID(s)**: 7.4
**Registered Sources (Fix 70)**: a research-advisory source (candidate)
