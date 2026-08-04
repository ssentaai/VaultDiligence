# F-LIQ-040 — Redemption Currency Concentration

**Field ID**: F-LIQ-040
**Field Name**: Redemption Currency Concentration
**Pillar(s)**: P9
**Vault Types**: ALL
**Collection Tier**: T1
**Primary Source**: Protocol docs / Contract
**D1**: Y
**D2**: Y
**Required?**: Y
**TTL**: 720h (30 days)

## Description

What currencies can the depositor receive on redemption. Single-stablecoin redemption creates concentration risk: if that stablecoin is frozen, blacklisted, or depegs, the depositor cannot exit.

## Failure Mode

A vault redeemable only in USDC is exposed to Circle freeze authority, USDC depeg, and Circle CCTP bridge risk. McCollum v. Circle (S.D.N.Y. 2026) is directly relevant to this field.

## If Not Found — Gap Action

Confirm which currencies redemption can be received in. If limited to a single stablecoin: confirm that stablecoin has sufficient on-chain liquidity at position size. If single-stablecoin and issuer is Circle or Tether: note McCollum v. Circle (filed April 2026) as pending legal risk on freeze authority.
**Registered Sources (Fix 70)**: goldrush-covalent-api
