# F-ENT-010 — Fund Manager and Investment Manager Separation

**Field ID**: F-ENT-010
**Field Name**: Fund Manager and Investment Manager Separation
**Pillar(s)**: P2
**Vault Types**: Management=delegated-offchain-IM OR (Exposure in {equities,corporate-fixed-income,sovereign-fixed-income} AND venue=tradfi-primary)  (derived from VT-N; original "Vault Types" value: VT-3a, VT-8)
**Collection Tier**: T1
**Primary Source**: GLEIF / Entity documents
**D1**: N
**D2**: Y
**Required?**: Y
**TTL**: 8760h (365 days)

## Description

Are the fund manager (responsible for fund administration, NAV calculation, investor relations) and investment manager (responsible for portfolio decisions) separate legal entities with independent governance. Standard institutional safeguard.

## Failure Mode

When fund manager and investment manager are the same entity, there is no independent check on portfolio decisions. Valuation disputes, fee overcharging, and self-dealing have no independent arbiter.

## If Not Found — Gap Action

Confirm whether the fund manager and investment manager are separate legal entities with independent governance. If the same entity controls both fund administration and investment decisions: classify as material condition — concentration of control without independent oversight.
