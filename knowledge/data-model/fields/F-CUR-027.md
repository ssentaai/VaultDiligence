# F-CUR-027

**Field ID**: F-CUR-027
**Category**: Curator
**Sub-Category**: Coverage Gap Profile
**Field Name**: Where Coverage Gaps Fall
**What to Collect / Question to Answer**: Given a published coverage map (F-CUR-026), where do the not-covered and partial requirements fall — concentrated in tail-risk categories (correlation, liquidity) that drive drawdowns in systemic stress, or in easily-instrumented categories (leverage)? Record the gap distribution by category as evidence.
**Data Type**: Structured (per risk category: full / partial / not-covered counts)
**Vault Types**: ALL (curator-managed; N/A for unmanaged/immutable vaults with no active Risk Control Operator — gate off F-ROL-001 Risk Control Operator, do not assume the curator fills it, state why)
**Collection Tier**: T2
**Pillar(s)**: P16
**Primary Source**: The risk control operator's coverage map (F-CUR-026), read by category
**Fallback Source**: Risk Control Operator DDQ response on where its monitoring is thinnest and its remediation plan
**Evidence Pathway**: Third-party-evidenced: from the coverage map, record the gap distribution by risk category and identify whether the uncovered requirements concentrate in tail-risk categories (correlation, liquidity) versus easily-instrumented ones.
**Institutional Standard**: The disclosed coverage gaps are distributed away from the tail-risk categories; where gaps concentrate in correlation and liquidity, that concentration is stated plainly so the allocator sees where monitoring is thinnest exactly where stress bites.
**Status**: Gap with action
**If Not Found — Gap Action**: Map the coverage gaps by category. If coverage concentrates in easily-instrumented categories while correlation and liquidity are largely uncovered: critical condition for stress resilience — the strong coverage is where it is easiest, not where it matters most. If no coverage map exists: inherits F-CUR-026 gap.
**Source / Precedent**: Concept surfaced by the risk-infrastructure provider methodology (p.4, per-category coverage readout) and the gap-profile reasoning in the VaultDiligence findings section 5; validated on first principles. Cross-reference F-CUR-026.
**Criterion ID(s)**: 16.2 (cross-ref F-CUR-026)
