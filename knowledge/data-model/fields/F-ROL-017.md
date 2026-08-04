# F-ROL-017

**Field ID**: F-ROL-017
**Category**: Counterparty
**Sub-Category**: Infrastructure
**Field Name**: Security Monitor — Named Party
**What to Collect / Question to Answer**: Name the party that provides the real-time security threat feed, as a function distinct from running the risk control loop in this vault's stack. If the role exists in the structure but is undisclosed, record it as gapped; if no such role exists in this structure, record N/A with the reason.
**Data Type**: Text (named party) + evidence-state
**Vault Types**: ALL (each role resolves N/A by vault type — state why when N/A)
**Collection Tier**: T2
**Pillar(s)**: P17
**Primary Source**: Fund documentation / offering memorandum / service-provider register naming the party; on-chain contract roles where the party is an on-chain actor
**Fallback Source**: Issuer or operator disclosure; independent aggregator or registry (RWA.xyz, GLEIF, regulator register)
**Evidence Pathway**: Third-party-evidenced: obtain the fund/service-provider document or registry entry naming the party; Inspection-validatable where the role maps to an on-chain address or role.
**Institutional Standard**: The party filling this role is named to a verifiable entity, or the role is explicitly recorded as gapped or N/A — never a silent absence. Detail: F-ENT-070 (Third-Party Risk Monitor), which currently conflates security monitoring with risk monitoring. This field identifies the Security Monitor (e.g. Hypernative) distinctly from the Risk Control Operator (F-ROL-001).
**Status**: Gap with action
**If Not Found — Gap Action**: Named and independently verified: E. Named but unverified this session: E(P). Named but details restricted: G2. The role exists in the structure but is unnamed or undisclosed: G3 — a finding (the accountable party cannot be assessed). No such role in this vault type: N/A with a stated reason.
**Source / Precedent**: role-registry-reconciliation 2026-07-08: F-ENT-070 conflated security monitor and risk monitor; this field disentangles the Security Monitor role.
**Criterion ID(s)**: 17.3 (P17 Counterparty & Role Registry)
