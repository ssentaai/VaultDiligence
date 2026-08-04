# F-BRG-010

**Field ID**: F-BRG-010
**Category**: Bridging
**Sub-Category**: Incident Response
**Field Name**: Bridge Incident-Response & Monitoring Coverage
**What to Collect / Question to Answer**: Is there standing 24/7 reachability across every party with authority to mitigate an in-flight incident (vendor, attestors, issuer), a written and rehearsed exploit procedure, pre-agreed authority for on-call teams to pause contracts and lower rate limits without escalation, and dedicated security and monitoring teams on both the vendor and issuer sides with documented coverage?
**Data Type**: Structured text (per party) + Boolean (rehearsed procedure)
**Vault Types**: ALL (bridge-crossing vaults; N/A single-chain, state why)
**Collection Tier**: T2a
**Pillar(s)**: P12
**Primary Source**: Issuer and vendor incident-response documentation: 24/7 contact rosters across vendor/attestors/issuer, the written and rehearsed exploit procedure, pre-agreed pause authority, and the dedicated monitoring teams on both sides
**Fallback Source**: Vendor-published security/monitoring team disclosures and the issuer's operational-stack disclosure (under NDA where reasonable)
**Evidence Pathway**: Third-party-evidenced — obtain the named 24/7 contact roster and the rehearsed written exploit procedure from the issuer and vendor, and confirm the dedicated monitoring teams and their documented coverage on both sides.
**Institutional Standard**: 24/7 reachability across all parties; a rehearsed written procedure; pre-agreed authority for on-call teams to pause and lower limits (defensive tightening may bypass timelocks, loosening may not); dedicated monitoring teams on both vendor and issuer side. Monitoring offloaded entirely to consuming protocols is below baseline; reachability gaps in any party, or absent dedicated monitoring on either side, are critical conditions.
**Status**: Gap with action
**If Not Found — Gap Action**: Request the 24/7 contact roster across vendor, attestors, and issuer, the rehearsed exploit procedure, and proof of dedicated monitoring teams on both sides. Where any party is unreachable or monitoring is offloaded to consuming protocols, record a critical condition and name the missing party. Seeds SC12.
**Source / Precedent**: Kelp DAO, 18 Apr 2026: the 46-minute detection-to-pause window was the difference between $292M and roughly $492M — incident-response speed is a quantifiable control.
**Criterion ID(s)**: 12.10 (seeds SC12)
