# F-LEG-024

**Field ID**: F-LEG-024
**Category**: Legal
**Sub-Category**: On-Chain Transfer Control
**Field Name**: On-Chain Transfer-Freeze Authority over the Holder's Own Position
**What to Collect / Question to Answer**: Does any role in the vault token contract hold the on-chain authority to freeze, blacklist, pause transfers of, or claw back the holder's own position, independent of the settlement-asset issuer's powers? Which role, under what conditions, and with what delay or notice?
**Data Type**: Text
**Vault Types**: ALL
**Collection Tier**: T2a
**Pillar(s)**: P10
**Primary Source**: Vault token contract bytecode / ABI on-chain — enumerate freeze, blacklist, pause-transfer, and clawback functions and the role authorised to call each
**Fallback Source**: Operator documentation of admin roles and conditions under which a transfer freeze would be exercised over a holder's position
**Evidence Pathway**: Inspection-validatable: read the deployed token contract's ABI and bytecode to enumerate any freeze / blacklist / pause / clawback function over a holder's balance, identify the authorised role, and confirm whether a timelock or notice precedes its use.
**Institutional Standard**: Any on-chain authority to freeze, blacklist, or claw back the holder's own position is disclosed, the controlling role and its key-management are named, and the conditions and any delay or notice governing its use are stated — or the contract demonstrably lacks such authority.
**Status**: Gap with action
**If Not Found — Gap Action**: Read the token contract on-chain and enumerate every transfer-freeze, blacklist, pause, or clawback function and its controlling role; if such authority exists, document the role, conditions, and delay. Undisclosed freeze authority over the holder's own position is a critical condition the allocator must weigh.
**Source / Precedent**: McCollum v. Circle (S.D.N.Y. 1:26-cv-03280, filed 14 Apr 2026): the dispute turns on a token-contract freeze/blacklist function — Circle had selectively frozen 16 wallets nine days before declining to freeze a ~$232M balance over roughly six hours — demonstrating that a contract-level transfer-freeze power over a holder's own position is a live, material authority that must be enumerated on-chain.
**Criterion ID(s)**: 10.2
