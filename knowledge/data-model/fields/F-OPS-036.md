# F-OPS-036

**Field ID**: F-OPS-036
**Category**: Operations
**Sub-Category**: Internal Controls
**Field Name**: Reconciliation Cycle & Exception-Log Evidence
**What to Collect / Question to Answer**: What is the reconciliation cycle (frequency and scope) between reported balances and underlying positions, and is there a maintained exception log evidencing breaks, their resolution, and segregation of duties?
**Data Type**: Text (cycle frequency + scope) + Document (exception log) + Boolean (segregation of duties)
**Vault Types**: Exposure in {private-credit,structured-credit} OR Management=delegated-offchain-IM OR Structure=tranched OR (Exposure in {equities,corporate-fixed-income,sovereign-fixed-income} AND venue=tradfi-primary)  (derived from VT-N; original "Vault Types" value: VT-3, VT-3a, VT-4, VT-8)
**Collection Tier**: T3
**Pillar(s)**: P8
**Primary Source**: Operator internal-control narrative / reconciliation policy stating cycle and scope; sample exception log
**Fallback Source**: Fund administrator confirmation of reconciliation cadence; SOC-2 control description (cross-ref F-LEG-010)
**Evidence Pathway**: Third-party-evidenced: obtain the reconciliation policy stating cycle frequency and scope, and inspect a sample exception log showing breaks logged, resolved with timestamps, and reconciled by a party segregated from the position-taker.
**Institutional Standard**: Good practice is a documented reconciliation cycle (commonly daily or at each NAV strike) with a maintained exception log recording each break, its resolution, and an owner segregated from the position-taker; NAV being calculated with no evidenced reconciliation cycle or exception log leaves reported balances unverified against underlying positions.
**Status**: Gap with action
**If Not Found — Gap Action**: Obtain the reconciliation policy (cycle frequency and scope) and a sample exception log evidencing breaks and resolutions. If reconciliation is asserted but no exception log or segregation evidence is produced: G2 — name the operator/administrator and the missing artifact. If no reconciliation cycle exists: G3 — operator must establish one. Distinct from F-OPS-030/031.
**Source / Precedent**: an operational due-diligence checklist: the operations domain requires NAV, reconciliation cycle, exception logs, and internal controls; a tree search returns no field for reconciliation cycle, exception logs, or segregation of duties (F-OPS-030/031 are the closest but are risk reporting and mandate drift, not reconciliation).
**Criterion ID(s)**: 8.4
