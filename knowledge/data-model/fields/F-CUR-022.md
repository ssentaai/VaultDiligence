# F-CUR-022

**Field ID**: F-CUR-022
**Category**: Curator
**Sub-Category**: Drift Detection
**Field Name**: Parameter-Baseline Drift Detection
**What to Collect / Question to Answer**: Does the risk control operator compare current protocol parameters against a stored prior baseline and flag changes in LLTV, supply/borrow caps, oracle fields, collateral lists, and market membership? Confirm the baseline is retained and the comparison runs each cycle — distinct from merely displaying current values.
**Data Type**: Boolean (baseline retained; diff runs) + Text (which parameter classes are diffed)
**Vault Types**: ALL (curator-managed; N/A for unmanaged/immutable vaults with no active Risk Control Operator — gate off F-ROL-001 Risk Control Operator, do not assume the curator fills it, state why)
**Collection Tier**: T2
**Pillar(s)**: P15
**Primary Source**: Risk Control Operator monitoring documentation evidencing a retained parameter baseline and a diff process
**Fallback Source**: Risk Control Operator DDQ response on how parameter changes are detected
**Evidence Pathway**: Third-party-evidenced: obtain evidence that the risk control operator retains a prior parameter baseline and diffs current-vs-baseline each cycle, flagging LLTV/cap/oracle/collateral changes; confirm on a sample change record if available.
**Institutional Standard**: Current parameters are diffed against a retained baseline each cycle, and material changes (LLTV, cap, oracle, collateral) are flagged automatically rather than noticed by chance.
**Status**: Gap with action
**If Not Found — Gap Action**: Ask whether the risk control operator retains a parameter baseline and diffs against it. If it only displays current values with no baseline diff: G3 — a silent protocol-side change would reach the risk control operator only after it repriced risk. Net-new capability, distinct from presence-of-monitoring (F-CUR-021).
**Source / Precedent**: Concept surfaced by the risk-infrastructure provider methodology (p.11, protocol-vault monitoring compares current parameters against prior baselines); validated on first principles.
**Criterion ID(s)**: 15.2
