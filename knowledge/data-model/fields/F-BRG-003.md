# F-BRG-003

**Field ID**: F-BRG-003
**Category**: Bridging
**Sub-Category**: Verifier Independence
**Field Name**: Verifier Independence — Organisation, Jurisdiction, Infrastructure
**What to Collect / Question to Answer**: Does the nominal verifier set survive three independence tests — organisational (distinct operators, no economic co-dependence), jurisdictional (no concentration under a single regulatory action), and infrastructure (no shared RPC providers, cloud accounts, hardware, or key infrastructure) — with any identifiable overlap documented?
**Data Type**: Structured text (per independence dimension)
**Vault Types**: ALL (bridge-crossing vaults; N/A single-chain, state why)
**Collection Tier**: T2
**Pillar(s)**: P12
**Primary Source**: Issuer/vendor disclosure of each verifier operator's organisation, jurisdiction, and hosting infrastructure, tested for overlap across the three dimensions
**Fallback Source**: Verifier operators' published infrastructure and entity registrations; RPC/cloud provider attribution from public node-operator documentation
**Evidence Pathway**: Third-party-evidenced — obtain per-operator organisation, jurisdiction, and infrastructure attributions and cross-reference shared RPC/cloud/hardware dependencies against the operators' own published disclosures.
**Institutional Standard**: Verifiers are independent across organisation, jurisdiction, and infrastructure, with bare-metal or comparably isolated infrastructure preferred. Nominal decentralisation that collapses on any one dimension is a single point of failure and must be stated as such.
**Status**: Gap with action
**If Not Found — Gap Action**: Request per-verifier organisation, jurisdiction, and hosting disclosures. Where shared RPC, cloud, hardware, or economic co-dependence is found, document it and state that the effective independent count is lower than the nominal count for risk-assessment purposes.
**Source / Precedent**: A three-of-five verifier set sharing one cloud provider or one RPC vendor is one verifier under stress — supply-chain concentration converts redundancy to theatre (a published protocol risk framework §2.3, 9 Jun 2026).
**Criterion ID(s)**: 12.3
**Registered Sources (Fix 70)**: layerzero-scan-dvn (candidate)
