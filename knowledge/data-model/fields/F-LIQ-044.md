# F-LIQ-044

**Field ID**: F-LIQ-044
**Category**: Liquidity
**Sub-Category**: Secondary Market Depth
**Field Name**: Liquidator Atomic-Liquidity Access + Scaling Plan
**What to Collect / Question to Answer**: Can liquidators access atomic liquidity to facilitate liquidations, and how is that liquidity planned to scale as the position size or vault TVL grows?
**Data Type**: Structured (atomic-liquidity routes named, current depth, stated scaling plan)
**Vault Types**: Strategy=lending OR (Structure=multi-asset-pool AND Management=algorithmic AND Exposure=crypto-native) OR Structure in {leveraged,looped}  (derived from VT-N; original "Vault Types" value: VT-1, VT-6, VT-7)
**Collection Tier**: T2
**Pillar(s)**: P9
**Primary Source**: On-chain liquidation-route inspection (DEX-aggregator routing / flash-loan availability against the collateral); liquidation-engine contract configuration
**Fallback Source**: Operator-disclosed liquidity-scaling plan and named liquidator participants
**Evidence Pathway**: Inspection-validatable: trace on-chain the atomic-liquidity routes a liquidator would use against the collateral and confirm executable depth, then read the operator's stated plan for scaling that depth as TVL grows; absent atomic access, liquidations stall and bad debt accrues.
**Institutional Standard**: Liquidators can access atomic liquidity sufficient to clear a liquidation at the current position size, and a stated plan exists to scale that liquidity as the position or vault TVL grows. Liquidation feasibility under stress determines whether bad debt accrues.
**Status**: Gap with action
**If Not Found — Gap Action**: Confirm whether liquidators can source atomic liquidity against the collateral at the current size by tracing on-chain routes, and record the operator's scaling plan. If atomic liquidity is insufficient at position size, state the shortfall in dollar terms. If no scaling plan is disclosed, classify G3 and require the operator to publish one.
**Source / Precedent**: Steakhouse Financial stablecoin-issuer DDQ v1.0 (§1.11): 'Can liquidators access atomic liquidity to facilitate liquidations? How will liquidity be scaled...'
**Criterion ID(s)**: 9.1
