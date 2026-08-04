# F-SEC-013

**Field ID**: F-SEC-013
**Category**: Security
**Sub-Category**: Infrastructure
**Field Name**: Infrastructure Incident Response Plan
**What to Collect / Question to Answer**: Documented incident response plan for key management compromise. Tested? Pause mechanism latency — how fast can protocol be paused after compromise detected?
**Data Type**: Text / Y/N
**Vault Types**: ALL
**Collection Tier**: T4
**Primary Source**: Operator documentation
**Fallback Source**: SOC-2 incident response section
**Pillar(s)**: P7
**D1**: Y
**D2**: Y
**D3**: Y
**D4**: Y
**D5**: Y
**Required?**: Y
**If Not Found — Gap Action**: Request incident response runbook from operator CTO. Confirm pause latency. Resolv: attacker had ~17 minutes to extract before pause.
**Criterion ID(s)**: 7.16
**Registered Sources (Fix 70)**: defisafety-process-reviews (candidate)
**Red Flag ID(s)**: RF41