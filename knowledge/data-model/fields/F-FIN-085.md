# F-FIN-085

**Field ID**: F-FIN-085
**Category**: Financial
**Sub-Category**: Wrong-Way Risk
**Field Name**: Third-Party-Leverage Register with Refresh Cadence
**What to Collect / Question to Answer**: What are all known third-party leveraged positions in this vault's token on external lending protocols, sized and located by venue, and is this register refreshed on a stated cadence and before any cap or sizing decision so second-order redemption-queue pressure can be quantified independently of the asset's own quality?
**Data Type**: Table (lending venue -> leveraged position size -> liquidation parameters) + refresh cadence
**Vault Types**: ALL
**Collection Tier**: T2
**Pillar(s)**: P9
**Primary Source**: On-chain reads of external lending markets holding the vault token (supply/borrow positions per venue)
**Fallback Source**: Lending-protocol analytics dashboards (per-market position data) corroborating the on-chain reads
**Evidence Pathway**: Inspection-validatable: enumerate external lending markets holding the vault token and read each leveraged position's size and liquidation parameters on-chain; record the refresh cadence and the date last refreshed.
**Institutional Standard**: A register of all known third-party leveraged holdings of the vault token is maintained per venue with sized positions and liquidation thresholds, refreshed on a stated cadence and refreshed again before any cap or sizing decision; the register exists so forced-deleverage queue pressure can be sized even when the underlying NAV is at par.
**Status**: Gap with action
**If Not Found — Gap Action**: Build the third-party-leverage register from on-chain lending-market reads and state the refresh cadence; if a venue's positions cannot be read, classify as G2 naming the lending protocol and the position data required, and flag that no cap or sizing decision should rely on a stale register.
**Source / Precedent**: a synthetic-dollar and CLO-fund diligence pack, Wrong-Way Risk section: a recommended 'monthly mapping of all known third party leveraged a tokenized CLO fund positions on lending protocols, updated before any cap decision' — grounded in Resolv's $100M a tokenized CLO fund loop on Aave Horizon, USR depeg to $0.025, and insolvency at $95M assets against $173M liabilities.
**Criterion ID(s)**: 9.4
**Registered Sources (Fix 70)**: aave-protocol-data, defillama-lendborrow, direct-rpc-read, dune-custom-queries, morpho-blue-api
