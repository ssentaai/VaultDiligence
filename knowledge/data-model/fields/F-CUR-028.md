# F-CUR-028

**Field ID**: F-CUR-028
**Category**: Curator
**Sub-Category**: Signals
**Field Name**: Risk Signals Computed & Own-Book Use
**What to Collect / Question to Answer**: Which risk signals does the risk control operator compute, at what cadence, and at what level (protocol solvency, vault utilisation/collateral, market liquidity / exit-cost / whale-concentration, anomaly detection), and does it run those same signals on its own book? Record the signal inventory and cadence as evidence.
**Data Type**: Structured (signal inventory by level + cadence; own-book use Boolean)
**Vault Types**: ALL (curator-managed; N/A for unmanaged/immutable vaults with no active Risk Control Operator — gate off F-ROL-001 Risk Control Operator, do not assume the curator fills it, state why)
**Collection Tier**: T2
**Pillar(s)**: P16
**Primary Source**: Risk Control Operator risk-analytics documentation listing computed signals, levels, and cadence; evidence of own-book application
**Fallback Source**: Risk Control Operator DDQ response; public risk-analytics surface if one exists
**Evidence Pathway**: Third-party-evidenced: obtain the risk control operator's signal inventory (protocol / vault / market level, cadence, anomaly detection) and evidence it applies the same signals to its own positions; Inspection-validatable where a public analytics surface exposes the signals.
**Institutional Standard**: The risk control operator computes named risk signals at a stated cadence across protocol, vault, and market levels, and applies the same signals to its own positions — alignment between what it measures for clients and for itself.
**Status**: Gap with action
**If Not Found — Gap Action**: Ask for the computed-signal inventory, cadence, and evidence of own-book use. If no computed signals beyond static reporting, or signals marketed but not run on the risk control operator's own book: gap in capability and alignment. Record the signal set; do not rate it.
**Source / Precedent**: Concept surfaced by the risk-infrastructure provider methodology (pp.13-14, Risk Radar block-by-block signals and the return-of-capital-before-return-on-capital own-book statement); validated on first principles. Cross-reference F-OPS-030 (quantitative risk reporting).
**Criterion ID(s)**: 16.3 (cross-ref F-OPS-030)
