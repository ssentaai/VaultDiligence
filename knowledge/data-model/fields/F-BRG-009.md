# F-BRG-009

**Field ID**: F-BRG-009
**Category**: Bridging
**Sub-Category**: Rate-Limit Sizing
**Field Name**: Rate-Limit Sizing — Highest Sustained Flow
**What to Collect / Question to Answer**: Are the rate-limit values sized to the highest observed sustained flow per route (not peak burst), with headroom over sustained flow explicit and bounded, and inbound and outbound evaluated separately because cross-chain flow is typically asymmetric?
**Data Type**: Numeric (limit vs highest sustained flow, per route, per direction) + ratio
**Vault Types**: ALL (bridge-crossing vaults; N/A single-chain, state why)
**Collection Tier**: T2
**Pillar(s)**: P12
**Primary Source**: On-chain transaction-history analysis of highest sustained flow per route and direction, compared against the configured rate-limit value read from contract state
**Fallback Source**: Issuer flow-sizing methodology documentation stating the sustained-flow basis and bounded headroom for each route and direction (confirm against on-chain history)
**Evidence Pathway**: Inspection-validatable — measure highest sustained flow per route and direction from on-chain transaction history and compare it to the configured limit to confirm bounded, explicit headroom rather than an optimistic multiple.
**Institutional Standard**: Limits are sized to highest sustained flow with explicit bounded headroom, per direction. Unbounded headroom is the absence of a meaningful limit and is treated as a rate-limit failure. Depends on F-BRG-008 being present.
**Status**: Gap with action
**If Not Found — Gap Action**: Measure highest sustained inbound and outbound flow per route from on-chain history and compare to the configured limit. Where headroom is unbounded or the limit is set to a large multiple of any flow the route has carried, treat as equivalent to no limit and request a sustained-flow-based resize.
**Source / Precedent**: A limit sized to ten times any flow the route has ever carried binds nothing: a forged package drains to the limit, and the limit was set by optimism (a published protocol risk framework §2.9, 9 Jun 2026).
**Criterion ID(s)**: 12.9
