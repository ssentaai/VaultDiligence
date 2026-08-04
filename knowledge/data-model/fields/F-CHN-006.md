# F-CHN-006

**Field ID**: F-CHN-006
**Category**: Chain
**Sub-Category**: Operational History
**Field Name**: Chain Operational History
**What to Collect / Question to Answer**: What is the chain's documented incident record (halts with duration, root cause and resolution; reorgs with depth and resolution; published post-mortems; time-to-recovery), and does that record show any unaddressed recurrence pattern when measured against the chain's stated design properties?
**Data Type**: Structured text (incident list: type, date, duration/depth, root cause, resolution, post-mortem link; time-to-recovery; recurrence assessment)
**Vault Types**: ALL
**Collection Tier**: T1
**Pillar(s)**: P13
**Primary Source**: Chain foundation incident post-mortems and status-page history; block-explorer halt/reorg records; published outage timelines
**Fallback Source**: Third-party incident records and outage trackers (chain status-page archives, independent post-mortem aggregations)
**Evidence Pathway**: Inspection-validatable: inspect block-explorer block-production gaps and reorg depth on-chain to corroborate reported halts and reorgs; Third-party-evidenced: cite the chain foundation's published post-mortems and status-page incident history.
**Institutional Standard**: Incident record compiled with post-mortems for material incidents, time-to-recovery documented, and no unaddressed recurrence pattern; where the record disagrees with the stated design properties, the record governs.
**Status**: Gap with action
**If Not Found — Gap Action**: Name each incident lacking a duration, root cause, resolution, or published post-mortem and request it from the chain foundation; flag repeated halts or reorgs on the same root cause without structural remediation as critical conditions (cross-ref SC11 and SC13).
**Source / Precedent**: Solana 2021-2022: repeated chain-wide halts on related root causes. Design documentation promised liveness; the operational record was the binding truth.
**Criterion ID(s)**: 13.6, SC11, SC13
