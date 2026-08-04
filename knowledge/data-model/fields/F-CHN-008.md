# F-CHN-008

**Field ID**: F-CHN-008
**Category**: Chain
**Sub-Category**: Tooling
**Field Name**: Chain Tooling & Monitoring Support
**What to Collect / Question to Answer**: Can the monitoring a vault assessment depends on actually run on this chain: a block explorer with verified-source upload and event decoding; indexing/analytics coverage; RPC provider diversity; risk-monitoring and oracle providers operating at the required cadence; and on-chain data availability for asset-state and authority-queue signals?
**Data Type**: Structured text (explorer functionality; indexing/analytics platforms; RPC provider list; oracle/monitoring providers + cadence; data-availability assessment)
**Vault Types**: ALL
**Collection Tier**: T1
**Pillar(s)**: P13
**Primary Source**: Chain block-explorer feature set (verified-source upload, event decoding); RPC-provider listings; indexing platform coverage (Dune, DeFiLlama, theGraph); oracle-provider deployment on the chain
**Fallback Source**: Third-party tooling-coverage references (indexer chain-support pages, RPC-provider directories, oracle-provider network listings)
**Evidence Pathway**: Inspection-validatable: confirm the block explorer accepts verified-source uploads and decodes events by inspecting a deployed contract page; Third-party-evidenced: cite the indexer/analytics and RPC-provider directories and oracle-provider network listing for chain coverage and cadence.
**Institutional Standard**: Full explorer functionality (verified-source upload, event decoding, contract interaction); multi-provider indexing and RPC; oracle and monitoring infrastructure live on the chain at the cadence the monitoring layer requires.
**Status**: Gap with action
**If Not Found — Gap Action**: Name the missing tooling layer (explorer functionality, indexer/analytics coverage, RPC-provider diversity, or oracle/monitoring cadence) and state the resulting monitoring-coverage gap; where the chain cannot be monitored at the required cadence, mark every continuous-monitoring claim for vaults on it as unverifiable until the coverage gap is closed.
**Source / Precedent**: a published protocol risk framework, 9 Jun 2026, §4.8: chains where the monitoring layer cannot operate at the required cadence, or where indexing and analytics support is materially below the standard expected for an Aave deployment, materially constrain the chain's exposure tier.
**Criterion ID(s)**: 13.8
**Registered Sources (Fix 70)**: rpc-provider-status (candidate)
