# F-CUR-024

**Field ID**: F-CUR-024
**Category**: Curator
**Sub-Category**: Severity Encoding
**Field Name**: Alert-Severity Ordering
**What to Collect / Question to Answer**: Does the risk control operator's alerting encode a defensible severity ordering — an LLTV / liquidation-threshold change treated as the highest severity because it reprices liquidation risk on existing positions, and a supply/borrow cap change treated as lower because it bounds new flow? Capture the actual mapping as evidence.
**Data Type**: Structured (parameter-change type -> encoded severity)
**Vault Types**: ALL (curator-managed; N/A for unmanaged/immutable vaults with no active Risk Control Operator — gate off F-ROL-001 Risk Control Operator, do not assume the curator fills it, state why)
**Collection Tier**: T2
**Pillar(s)**: P15
**Primary Source**: Risk Control Operator alert-configuration documentation showing severity assigned per parameter-change type
**Fallback Source**: Risk Control Operator DDQ response describing severity assignment
**Evidence Pathway**: Third-party-evidenced: obtain the risk control operator's alert-severity configuration and record which parameter-change types map to which severity; confirm LLTV-change ranks above cap-change.
**Institutional Standard**: The alert model encodes parameter-change severity by real consequence: an LLTV move (reprices existing positions' liquidation risk) ranks above a cap change (bounds new flow), and the mapping is documented.
**Status**: Gap with action
**If Not Found — Gap Action**: Request the severity configuration. If a cap change is treated as more severe than an LLTV change, or parameter changes are not classified by consequence: critical condition — the most dangerous change is not the loudest alert. Record the mapping; do not rate it.
**Source / Precedent**: Concept surfaced by the risk-infrastructure provider methodology (p.11, LLTV changes as critical / cap changes as warning); validated on first principles. Cross-reference F-OPS-005 (incident response SLA), P2.9 (curator stress record).
**Criterion ID(s)**: 15.4 (cross-ref F-OPS-005, P2.9)
