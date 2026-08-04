# F-OPS-031 — Investment Mandate Drift

**Field ID**: F-OPS-031
**Field Name**: Investment Mandate Drift
**Pillar(s)**: P8
**Vault Types**: ALL
**Collection Tier**: T1
**Primary Source**: On-chain / Protocol docs
**D1**: N
**D2**: Y
**Required?**: Y
**TTL**: 168h (7 days)

## Description

Is the current vault allocation consistent with its stated investment mandate and restrictions. Checks whether the curator is operating within the strategy described in documentation versus what is actually deployed on-chain.

## Failure Mode

Mandate drift means the allocator is not deploying into the strategy they paid for. A vault marketed as conservative USDC lending that is actually deploying into leveraged positions is a material misrepresentation.

## If Not Found — Gap Action

Confirm current vault allocation against stated strategy. Does the current on-chain allocation match the stated investment mandate? If material deviation exists: flag as triggered condition with percentage deviation and structural consequence.
**v54 Refinement (gap audit 2026-06-12)**: Add the wrapper-mandate-weaker dimension: where a permissionless wrapper (e.g. deRWA) exists, confirm whether the wrapper's underlying mandate is more concentrated or weaker than the branded fund it tracks — mandate drift can be structural, not only allocation-level. Source: a synthetic-dollar and CLO-fund (Centrifuge wrapper intentionally more concentrated than the branded ETF). Cross-ref F-LIQ-012, F-COL-010.
