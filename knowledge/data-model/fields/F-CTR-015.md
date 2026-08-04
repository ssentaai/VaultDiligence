# F-CTR-015

**Field ID**: F-CTR-015
**Category**: Contract
**Sub-Category**: Custody Architecture
**Field Name**: Custody Chain by Layer — Where the Funds Actually Sit
**What to Collect / Question to Answer**: Enumerate every protocol or custodian that holds depositor funds at each layer of the stack. A user's noncustodial wallet is irrelevant if the protocol deposits funds in custodial sub-protocols. State each layer's custody type (noncustodial smart contract / multisig / centralized custodian / regulated trust) and what authority can move funds at that layer. Resolv precedent: smart-contract-noncustodial at the top layer, but custodial OTC venue at the funding leg.
**Data Type**: Structured list — each entry: { layer_name, custody_type, controlling_authority, can_move_funds_unilaterally: bool }
**Vault Types**: ALL
**Collection Tier**: T2
**Primary Source**: On-chain inspection of contract dependencies (F-CTR-008) + protocol documentation describing where funds are deposited at each step
**Fallback Source**: Operator disclosure with on-chain verification
**Pillar(s)**: P1, P7
**D1**: Y
**D2**: Y
**D3**: Y
**D4**: Y
**D5**: Y
**Required?**: Y
**If Not Found — Gap Action**: G2 — operator must disclose every custody layer with on-chain or third-party verification. A protocol that cannot enumerate its own custody chain at every layer is itself the finding.
**Criterion ID(s)**: 1.4, 7.5
**Red Flag ID(s)**: RF-CTL-001 (custody-chain control failure)
