# F-CTR-006

**Field ID**: F-CTR-006
**Category**: Contract
**Sub-Category**: Governance
**Field Name**: Emergency Pause
**What to Collect / Question to Answer**: Emergency pause function exists? Who can trigger it? Timelock?
**Data Type**: Text
**Vault Types**: ALL
**Collection Tier**: T1
**Primary Source**: Contract: pause() / paused() function / Etherscan ABI
**Fallback Source**: Protocol docs / audit report
**Pillar(s)**: P7
**D1**: Y
**D2**: Y
**D3**: Y
**Required?**: Y
**If Not Found — Gap Action**: Exists with guardian = strong. No pause = flag. Pause with no timelock = governance risk.
**Criterion ID(s)**: 7.2
**Registered Sources (Fix 70)**: blockscout-evm-explorer, etherscan-evm-explorer, thegraph-subgraph
**v54 Refinement (gap audit 2026-06-12)**: Record measured pause latency where an incident exists — detection-to-pause time and the loss blocked — not just pause authority and scope (Kelp pauser froze 46 minutes post-drain, blocking roughly $200M). Cross-ref SC5, F-BRG-010.
