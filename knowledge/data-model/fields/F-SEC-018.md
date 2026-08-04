# F-SEC-018

**Field ID**: F-SEC-018
**Category**: Security
**Sub-Category**: Infrastructure
**Field Name**: Release-Pipeline Controls
**What to Collect / Question to Answer**: Are all production releases subject to mandatory manual approval, automated CI checks, and checksum validation of build artifacts before deployment?
**Data Type**: Text (control checklist)
**Vault Types**: ALL
**Collection Tier**: T3
**Pillar(s)**: P7
**Primary Source**: Operator engineering/security documentation / CI-CD policy / DDQ response
**Fallback Source**: CI pipeline configuration in the public repository (branch-protection and required-check settings) plus operator attestation of manual approval and checksum validation
**Evidence Pathway**: Inspection-validatable: inspect the public repository's CI configuration and branch-protection/required-check settings to confirm automated checks and gated merges, then obtain operator attestation that manual approval and artifact checksum validation gate every production release.
**Institutional Standard**: Every production release passes through a controlled supply chain: mandatory manual approval, automated CI checks that must pass, and checksum validation of build artifacts, so unauthorised or tampered code cannot reach production without an auditable, gated step.
**Status**: Gap with action
**If Not Found — Gap Action**: Request the operator's release process: confirm whether production releases require manual approval, which automated CI checks gate the release, and whether build-artifact checksums are validated at deploy. Where any control is absent or unconfirmed, classify as a gap (G2) and name the operator engineering lead as the entity that must produce evidence.
**Source / Precedent**: Steakhouse Financial stablecoin-issuer DDQ v1.0, §2.20: 'Are all production releases subject to manual approval, CI checks, and checksum validation?' The release-integrity counterpart to §2.17's commit/repo/on-chain deployment-provenance validation, addressing the supply-chain path into production.
**Criterion ID(s)**: 7.16
