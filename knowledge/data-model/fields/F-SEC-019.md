# F-SEC-019

**Field ID**: F-SEC-019
**Category**: Security
**Sub-Category**: Infrastructure
**Field Name**: Cross-Chain Infrastructure Audit & Failover Resilience
**What to Collect / Question to Answer**: Has the operator's cross-chain infrastructure layer — RPC providers, cross-chain message verifiers/DVNs, and DDoS/failover paths — been audited with the same rigour as the smart contracts, and is the failover behaviour (including whether failover can collapse a multi-verifier path to a single verifier) documented and tested?
**Data Type**: Text
**Vault Types**: Strategy in {staking,restaking} OR Structure in {leveraged,looped}  (derived from VT-N; original "Vault Types" value: VT-5, VT-7)
**Collection Tier**: T2b
**Pillar(s)**: P7
**Primary Source**: Infrastructure-layer audit / penetration-test report covering RPC, DVN, and failover/DDoS resilience (firm name, date, scope statement)
**Fallback Source**: On-chain inspection of the cross-chain verifier configuration and its documented failover/default behaviour, plus operator confirmation of RPC redundancy and DDoS posture
**Evidence Pathway**: Third-party-evidenced: obtain the named infrastructure-layer audit or pentest report and confirm RPC, DVN/verifier, and failover/DDoS resilience are explicitly in its scope, with the failover-to-single-verifier path tested. Where no such report exists, inspect the verifier configuration and failover default on-chain.
**Institutional Standard**: The cross-chain infrastructure layer — RPC endpoints, message verifiers/DVNs, and DDoS/failover paths — is audited to the same standard as the contracts, with redundant RPC, a documented and tested failover that cannot silently collapse a multi-verifier quorum to a single verifier, and DDoS resilience evidenced by a named review.
**Status**: Gap with action
**If Not Found — Gap Action**: Request a named infrastructure-layer audit or pentest covering RPC providers, the cross-chain verifier/DVN set, and failover/DDoS behaviour, with date and scope statement. Confirm whether any failover path can reduce the verifier quorum to one. If no such review exists, classify as a gap (G2), trigger RF41, and name the operator's infrastructure owner as the entity that must produce it.
**Source / Precedent**: Buzko Krasnov legal analysis, 27 Apr 2026: Kelp DAO, 18 Apr 2026 — $292M drained (116,500 rsETH, ~18 percent of supply) via a forced-failover to a 1-of-1 LayerZero DVN, a single cross-chain verifier; the firm argues infrastructure (RPC/DVN/failover/DDoS) must be audited with the same rigour as contracts.
**Criterion ID(s)**: 7.16, RF41
**Registered Sources (Fix 70)**: layerzero-scan-dvn (candidate)
