# F-CTR-019

**Field ID**: F-CTR-019
**Category**: Contract
**Sub-Category**: Cross-Chain Dependencies
**Field Name**: Per-Bridge Dependency Enumeration
**What to Collect / Question to Answer**: Enumerate EVERY bridge in the dependency chain, not just the most-prominent one. F-CTR-010 names "the bridge"; F-CTR-019 enumerates the full set including bridges in the dependency graph that the operator may not advertise. A vault using Stargate that holds collateral itself bridged via Wormhole has compounded bridge risk: both bridges can fail independently, neither is captured by naming Stargate alone. For each entry, capture: (a) bridge name and contract address, (b) role (asset bridging / message bridging / oracle relay / multiple), (c) trust model class linking to F-CTR-018 enum, (d) historical incident count from the incidents registry, (e) layer in dependency graph (top = direct user interaction, deeper = collateral / dependency-chain bridges).
**Data Type**: Structured list — each entry: { bridge_name, contract_address, role, trust_model_class, historical_incidents, dependency_layer }
**Vault Types**: Exposure in {private-credit,structured-credit} OR Structure in {leveraged,looped}  (derived from VT-N; original "Vault Types" value: VT-3, VT-7, plus ANY vault with cross-chain collateral or yield path (a vault on Ethereum holding bridged assets has cross-chain dependencies even if it does not natively bridge))
**Collection Tier**: T2
**Primary Source**: F-CTR-008 (protocol dependency map) walked recursively + F-CTR-010 (the named bridge) + on-chain inspection of every collateral asset's origin chain. For each asset, trace: was this asset minted on this chain or bridged from elsewhere? If bridged, which bridge?
**Fallback Source**: Operator disclosure of full dependency chain + cross-check against on-chain
**Pillar(s)**: P7
**D1**: Y
**D2**: Y
**D3**: Y
**D4**: Y
**D5**: Y
**Required?**: C (conditional — required if any cross-chain dependency exists at any layer)
**If Not Found — Gap Action**: G2 — operator must disclose every bridge in the dependency chain. Single-bridge listings on bridge-using protocols are almost always incomplete. The Resolv precedent of unexpected dependency exposure applies: the second-order dependencies are the failure surface, not the named one.
**Criterion ID(s)**: 7.7, 7.8
**Registered Sources (Fix 70)**: etherscan-evm-explorer
**Red Flag ID(s)**: RF26, RF-CTL-005 (compound bridge dependency)
