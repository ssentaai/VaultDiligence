# F-BRG-006

**Field ID**: F-BRG-006
**Category**: Bridging
**Sub-Category**: Pause Pathways
**Field Name**: Independent Pause Pathways
**What to Collect / Question to Answer**: Are there at least two independent pause pathways on the route — an issuer-side pause independent of the vendor (including native rate limits set to zero), a vendor-side verification halt exercisable by the vendor's incident-response team, and any protocol-controllable pause via the monitoring layer — each documented and tested under standing incident-response procedures?
**Data Type**: Structured text (per pause path) + Integer count
**Vault Types**: ALL (bridge-crossing vaults; N/A single-chain, state why)
**Collection Tier**: T2
**Pillar(s)**: P12
**Primary Source**: On-chain read of the pause/rate-limit-to-zero authorities held by the issuer and the vendor on each route, plus the issuer's documented and rehearsed incident-response procedures
**Fallback Source**: Vendor incident-response documentation describing the verification-halt path; monitoring-layer integration documentation for any protocol-controllable pause
**Evidence Pathway**: Inspection-validatable — read the pause and rate-limit authorities on each route to confirm an issuer-side path exists independent of the vendor, then confirm the documented vendor-side halt and any monitoring-layer pause against incident-response procedures.
**Institutional Standard**: At least two independent pause pathways, each documented and tested. Single-path pause concentration is below baseline. A pause is also an exit-freeze for holders (SC12), so the concentration of pause authority is itself a finding.
**Status**: Gap with action
**If Not Found — Gap Action**: Map every pause path on the route and confirm at least one is exercisable by the issuer independent of the vendor. If pause depends on a single party, name that party as the single point of incident-response authority and request an independent issuer-side path. Seeds SC12.
**Source / Precedent**: Kelp DAO, 18 Apr 2026: a pauser froze the bridge 46 minutes post-drain, blocking roughly $200M of follow-on theft — pause latency and pause authority decided the loss boundary.
**Criterion ID(s)**: 12.6 (seeds SC12)
