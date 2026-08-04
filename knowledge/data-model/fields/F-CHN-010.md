# F-CHN-010

**Field ID**: F-CHN-010
**Category**: Chain
**Sub-Category**: Propagation
**Field Name**: Chain-Risk Propagation to Asset Exposure
**What to Collect / Question to Answer**: Does the assessment output state explicitly how the chain evaluation bounds the vault — that the chain's standing constraints apply to every asset on the deployment regardless of asset-level findings, that cross-chain expansion onto a weaker chain carries that chain's constraints onto the bridged asset, and that material chain-risk degradation without remediation is a deprecation-class event for the deployment?
**Data Type**: Structured text (chain-tier-as-upper-bound statement per deployment; bridged-asset constraint inheritance; deprecation-class degradation note)
**Vault Types**: ALL
**Collection Tier**: T1
**Pillar(s)**: P13
**Primary Source**: VaultDiligence chain evaluation (F-CHN-001 through F-CHN-009 conclusions) read against the vault's per-deployment asset-level findings
**Fallback Source**: The vault's own deployment manifest and per-chain exposure breakdown, to confirm each deployment carries the bound statement
**Evidence Pathway**: Inspection-validatable: confirm the assessment output contains, for each deployment, an explicit statement that the chain-level constraints from F-CHN-002 to F-CHN-009 upper-bound the asset-level findings, and that any bridged-asset exposure carries the weaker chain's constraints.
**Institutional Standard**: Chain-tier-as-upper-bound stated in the assessment output for each deployment; bridged-asset exposure carries the weaker chain's constraints; material chain-risk degradation without remediation flagged as a deprecation-class event for the deployment.
**Status**: Gap with action
**If Not Found — Gap Action**: Where the assessment reports asset-level findings without stating the chain-level bound for a deployment, add the explicit bound statement; flag the omission as a precision overstatement, since the chain bound is mandatory output rather than optional context.
**Source / Precedent**: a published protocol risk framework, 9 Jun 2026, §4.10: the chain's evaluation tier sets an upper bound on the LTV, supply cap, and borrow cap of every asset listed on the chain regardless of the asset's own Layer 1 evaluation, and whole-deployment deprecation is triggered when chain risk degrades materially without remediation.
**Criterion ID(s)**: 13.10
