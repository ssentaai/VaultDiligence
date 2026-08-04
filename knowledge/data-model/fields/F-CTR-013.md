# F-CTR-013

**Field ID**: F-CTR-013
**Category**: Contract
**Sub-Category**: Oracle Architecture
**Field Name**: Oracle Hardcoded vs Governance-Updatable
**What to Collect / Question to Answer**: Is the oracle address hardcoded in contract bytecode or points to upgradeable proxy? If hardcoded: permanent design risk, cannot be corrected without redeployment. Matthew Graham pattern: Renzo, Usual, Resolv -- three hardcoded oracle failures.
**Data Type**: Enum: Hardcoded / Proxy / Governance-updatable
**Vault Types**: ALL
**Collection Tier**: T1
**Primary Source**: Contract bytecode analysis (Etherscan ABI)
**Pillar(s)**: P7
**Fallback Source**: Protocol documentation