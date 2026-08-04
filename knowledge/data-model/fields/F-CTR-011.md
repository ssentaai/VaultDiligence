# F-CTR-011

**Field ID**: F-CTR-011
**Category**: Contract
**Sub-Category**: Bug Bounty
**Field Name**: Bug Bounty Program
**What to Collect / Question to Answer**: Platform, max critical payout, active since date, URL
**Data Type**: Text
**Vault Types**: ALL
**Collection Tier**: T1
**Primary Source**: Immunefi: immunefi.com/bug-bounty/{protocol} / Cantina / Sherlock
**Fallback Source**: Protocol security page
**Pillar(s)**: P7
**D1**: Y
**D2**: Y
**D3**: Y
**Required?**: Y
**If Not Found — Gap Action**: No bug bounty = flag. <$100K max = flag RF17. Note: bounty incentivises disclosure, not insurance.
**Criterion ID(s)**: 7.3
**v54 Refinement (gap audit 2026-06-12)**: Apply the Aave/LlamaRisk section 1.4 baseline: a critical-finding payout floor of at least $50,000 regardless of TVL, a TVL-scaled maximum, and a scope checklist covering loss of user funds, key or password exposure, infrastructure compromise, and domain takeover — smart-contract-only scope is no longer sufficient. Cross-ref RF46.
**Red Flag ID(s)**: RF17