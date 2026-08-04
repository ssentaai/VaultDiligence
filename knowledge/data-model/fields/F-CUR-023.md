# F-CUR-023

**Field ID**: F-CUR-023
**Category**: Curator
**Sub-Category**: Data Health
**Field Name**: Data-Health / Monitor-the-Monitor
**What to Collect / Question to Answer**: Does the risk control operator monitor its own monitoring: freshness checks on source data, record-count history, and schema snapshots, with staleness surfaced as a state rather than silently suppressed? Confirm a stale feed is displayed as stale.
**Data Type**: Boolean (freshness checks, record-count history, schema snapshots present; staleness surfaced)
**Vault Types**: ALL (curator-managed; N/A for unmanaged/immutable vaults with no active Risk Control Operator — gate off F-ROL-001 Risk Control Operator, do not assume the curator fills it, state why)
**Collection Tier**: T2
**Pillar(s)**: P15
**Primary Source**: Risk Control Operator data-health documentation; dashboard evidence that staleness is displayed
**Fallback Source**: Risk Control Operator DDQ response on data-quality monitoring
**Evidence Pathway**: Third-party-evidenced: obtain evidence of freshness checks, record-count history, and schema-stability monitoring, and confirm on the live surface that a stale feed is shown as stale rather than hidden.
**Institutional Standard**: Source-data freshness, record-count continuity, and schema stability are checked and their failures surfaced; a stale feed is shown as stale, so the reader can discount it.
**Status**: Gap with action
**If Not Found — Gap Action**: Ask for the data-health checks and confirm staleness is surfaced. If the monitoring layer cannot detect or does not surface its own staleness: G3 — downstream controls silently inherit stale inputs. Cross-reference F-OPS-004 (data lag).
**Source / Precedent**: Concept surfaced by the risk-infrastructure provider methodology (pp.10, 12, data-health checks and honest-staleness dashboard reads); validated on first principles. Cross-reference F-OPS-004.
**Criterion ID(s)**: 15.3 (cross-ref F-OPS-004)
