# F-CTR-018

**Field ID**: F-CTR-018
**Category**: Contract
**Sub-Category**: Cross-Chain Trust Model
**Field Name**: Cross-Chain Message Verification Mechanism
**What to Collect / Question to Answer**: For every cross-chain message dependency (asset bridging, message bridging, or oracle relaying), classify the verification mechanism by trust model class. Distinct from F-CTR-010 (which names the bridge); this field captures HOW the bridge verifies messages. The KelpDAO/LayerZero (early 2026) incident was a misconfigured DVN setup — not a code defect, a parameter choice. This field captures that parameter choice. State trust model class plus, for LayerZero-shaped bridges, the DVN configuration completeness (named DVNs in send and receive paths, plus required threshold). For light-client bridges, state which chains' light clients are implemented. For optimistic bridges, state fraud-proof window duration in hours.
**Data Type**: Enum + structured detail. Enum: `cryptographic_zk` | `economically_bonded` | `honest_validator_majority` | `honest_signer_multisig` | `optimistic_with_fraud_window` | `mixed_or_unknown`. Detail: { dvn_config: text or N/A, light_client_chains: list or N/A, fraud_window_hours: number or N/A }.
**Vault Types**: Exposure in {private-credit,structured-credit} OR Structure in {leveraged,looped}  (derived from VT-N; original "Vault Types" value: VT-3, VT-7 (cross-chain native), plus ANY vault whose collateral or yield path crosses chains)
**Collection Tier**: T1
**Primary Source**: Bridge protocol documentation describing verification architecture + on-chain inspection of DVN/oracle/relayer configuration. For LayerZero: read the OAppCore configuration. For Wormhole: read guardian set + signed VAA path. For zk-bridges: read circuit verification contracts.
**Fallback Source**: Audit report's cross-chain section + bridge protocol's threat model documentation
**Pillar(s)**: P7
**D1**: Y
**D2**: Y
**D3**: Y
**D4**: Y
**D5**: Y
**Required?**: C (conditional — required if cross-chain dependency exists)
**If Not Found — Gap Action**: G2 if cross-chain dependency exists but verification mechanism is undocumented. `mixed_or_unknown` is acceptable as a final state ONLY when multiple verification paths exist and the dominant one cannot be identified; otherwise it indicates the diligence is incomplete. State explicitly which trust assumption an attacker would need to break to forge a message — that is the structural finding.
**Criterion ID(s)**: 7.7, 7.8
**v54 Refinement (gap audit 2026-06-12)**: Record whether the verification configuration (e.g. DVN quorum) is the vendor default or operator-chosen — a known-weak default is a finding in both cases (LayerZero shipped 1-of-1 as default). Cross-ref F-BRG-002, F-BRG-003, RF44.
**Red Flag ID(s)**: RF26, RF-CTL-004 (verification mechanism unstated or misconfigured)
