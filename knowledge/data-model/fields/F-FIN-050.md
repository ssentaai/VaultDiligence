# F-FIN-050 — First-Loss Capital

**Field ID**: F-FIN-050
**Field Name**: First-Loss Capital
**Pillar(s)**: P2
**Vault Types**: Management=delegated-offchain-IM OR (Exposure in {equities,corporate-fixed-income,sovereign-fixed-income} AND venue=tradfi-primary) OR Seniority=junior/first-loss  (derived from VT-N; original "Vault Types" value: VT-3a, VT-8, VT-9)
**Collection Tier**: T1
**Primary Source**: On-chain / Protocol docs
**D1**: N
**D2**: Y
**Required?**: N
**TTL**: 720h (30 days)

## Description

Does the curator or sponsor hold a first-loss equity position that absorbs losses before depositors are affected. Amount, denomination, and on-chain verification address.

## Failure Mode

Absence of first-loss capital means depositors bear the first loss in any credit event. Presence of first-loss capital is a material alignment signal.

## If Not Found — Gap Action

Confirm whether curator or sponsor holds a first-loss position. If yes: confirm amount, denomination, on-chain address, and subordination structure. If no: note absence — allocator applies own policy.
