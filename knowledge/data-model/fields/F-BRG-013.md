# F-BRG-013

**Field ID**: F-BRG-013
**Category**: Bridging
**Sub-Category**: Configuration Uniformity
**Field Name**: Bridge-Config Uniformity vs Per-Chain Flexibility
**What to Collect / Question to Answer**: Does the asset use a uniform default security architecture across all chain expansions, or bespoke per-chain configurations — and where bespoke, is each deviation explicitly justified and disclosed under route topology, with uniformity reviewed at every cadence point?
**Data Type**: Categorical (uniform / bespoke) + structured text (per deviation)
**Vault Types**: ALL (bridge-crossing vaults; N/A single-chain, state why)
**Collection Tier**: T2
**Pillar(s)**: P12
**Primary Source**: Cross-route comparison of the security configuration (verifier set, libraries, timelocks, rate limits) read on chain across every chain expansion, against the issuer's stated default architecture
**Fallback Source**: Issuer route-topology disclosure identifying and justifying each bespoke per-chain deviation from the default architecture
**Evidence Pathway**: Inspection-validatable — read the configuration on each chain expansion and compare against the asset's stated default to surface any undisclosed per-chain divergence, which voids the assumption that assessing one route assesses them all.
**Institutional Standard**: Either a uniform default architecture across expansions, or bespoke deviations explicitly justified and disclosed. Undisclosed per-chain configuration divergence is a critical condition — it voids the assumption that assessing one route assesses them all.
**Status**: Gap with action
**If Not Found — Gap Action**: Compare the on-chain configuration of every chain expansion against the stated default. For any divergence not disclosed and justified in route topology, record a critical condition and request that the issuer document and justify the bespoke configuration — especially any route configured below the asset's own default.
**Source / Precedent**: A bespoke route configured below the asset's own default is invisible to anyone who assessed only the flagship route — configuration drift is where uniform-sounding security claims quietly fail (a published protocol risk framework §2.16, 9 Jun 2026).
**Criterion ID(s)**: 12.13
