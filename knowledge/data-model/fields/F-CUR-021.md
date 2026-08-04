# F-CUR-021

**Field ID**: F-CUR-021
**Category**: Curator
**Sub-Category**: Live Control Loop
**Field Name**: Live Control-Loop Element Coverage
**What to Collect / Question to Answer**: Which live-control elements does the risk control operator run: scheduled monitoring jobs, a stated run cadence, cap-utilisation flag bands (for example at eighty, ninety, and full utilisation), and defined data-freshness SLAs? Record each element as present or absent with evidence — this is an element inventory, recorded as evidence.
**Data Type**: Structured (per element: present/absent + evidence)
**Vault Types**: ALL (curator-managed; N/A for unmanaged/immutable vaults with no active Risk Control Operator — gate off F-ROL-001 Risk Control Operator, do not assume the curator fills it, state why)
**Collection Tier**: T2
**Pillar(s)**: P15
**Primary Source**: Risk Control Operator monitoring documentation; live dashboard evidencing scheduled jobs, cadence, cap-utilisation bands, and freshness SLAs
**Fallback Source**: Risk Control Operator DDQ response listing monitoring jobs and cadence; dashboard screenshots
**Evidence Pathway**: Third-party-evidenced: obtain the risk control operator's monitoring job schedule and dashboard and confirm each element (scheduled jobs, cadence, cap-utilisation bands, freshness SLA) is present; Inspection-validatable where a public dashboard exposes the cadence and utilisation bands.
**Institutional Standard**: The risk control operator runs scheduled checks at a stated cadence against the approved universe and mandates, with cap-utilisation flag bands and freshness SLAs defined; each element is evidenced as present, not asserted.
**Status**: Gap with action
**If Not Found — Gap Action**: List the risk control operator's scheduled jobs, cadence, cap-utilisation bands, and freshness SLAs from its monitoring surface. If no scheduled job / no cadence / no freshness SLA on a managed vault: G3 (cross-ref RF15) — the risk control operator must run a live control loop.
**Source / Precedent**: Concept surfaced by the risk-infrastructure provider methodology (pp.10-12, live monitoring layers); validated on first principles. Cross-reference F-OPS-004 (real-time monitoring dashboard), P8.3 (real-time monitoring), F-LIQ-048 (host-pool utilisation).
**Criterion ID(s)**: 15.1 (cross-ref F-OPS-004, P8.3, F-LIQ-048; RF15)
