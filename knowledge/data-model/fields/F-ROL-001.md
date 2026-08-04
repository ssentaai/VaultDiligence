# F-ROL-001

**Field ID**: F-ROL-001
**Category**: Counterparty
**Sub-Category**: Principal
**Field Name**: Risk Control Operator — Named Party
**What to Collect / Question to Answer**: Name the party that runs the continuous risk control apparatus for the vault — live monitoring, risk triggers, and escalation — as a function distinct from setting parameters or making investment decisions in this vault's stack. If the role exists in the structure but is undisclosed, record it as gapped; if no such role exists in this structure, record N/A with the reason.
**Data Type**: Text (named party) + evidence-state
**Vault Types**: ALL (each role resolves N/A by vault type — state why when N/A)
**Collection Tier**: T2
**Pillar(s)**: P17
**Primary Source**: Fund documentation / offering memorandum / service-provider register naming the party; on-chain contract roles where the party is an on-chain actor
**Fallback Source**: Issuer or operator disclosure; independent aggregator or registry (RWA.xyz, GLEIF, regulator register)
**Evidence Pathway**: Third-party-evidenced: obtain the fund/service-provider document or registry entry naming the party; Inspection-validatable where the role maps to an on-chain address or role.
**Institutional Standard**: The party filling this role is named to a verifiable entity, or the role is explicitly recorded as gapped or N/A — never a silent absence. This field disentangles the Risk Control Operator from F-CUR-009 (Third-Party Risk Manager) and F-ENT-070 (Third-Party Risk Monitor), and from the Curator (F-ROL-005) and Investment Manager (F-ROL-003). The dimension pillars P14-P16 gate off this field.
**Status**: Gap with action
**If Not Found — Gap Action**: Named and independently verified: E. Named but unverified this session: E(P). Named but details restricted: G2. The role exists in the structure but is unnamed or undisclosed: G3 — a finding (the accountable party cannot be assessed). No such role in this vault type: N/A with a stated reason.
**Source / Precedent**: role-registry-reconciliation 2026-07-08: a search for 'risk control operator' returned zero fields; the role was previously conflated into F-CUR-001/009 and F-ENT-070.
**Criterion ID(s)**: 17.1 (P17 Counterparty & Role Registry)
