# F-LEG-026

**Field ID**: F-LEG-026
**Category**: Legal
**Sub-Category**: Settlement-Asset Issuer Authority
**Field Name**: Settlement-Asset Issuer Freeze Authority & Posture
**What to Collect / Question to Answer**: For each stablecoin or settlement asset the vault holds, does the issuer hold freeze, blacklist, or seize authority over balances, and what is its demonstrated posture — has it frozen selectively, refused to freeze a known illicit balance, or failed to act within a stated response window?
**Data Type**: Text
**Vault Types**: ALL
**Collection Tier**: T2a
**Pillar(s)**: P10
**Primary Source**: Settlement-asset issuer contract on-chain — enumerate freeze/blacklist/seize functions and authorised roles — plus the issuer's published freeze/seizure policy
**Fallback Source**: Issuer transparency reports and documented historical freeze/non-freeze actions; litigation or regulatory filings evidencing the issuer's demonstrated posture
**Evidence Pathway**: Inspection-validatable: read the settlement-asset contract's freeze/blacklist/seize functions and authorised roles on-chain; corroborate the issuer's demonstrated posture with its published policy and documented historical actions.
**Institutional Standard**: Every settlement asset's issuer freeze/seize authority is enumerated from the contract, the authorised role and conditions are disclosed, and the issuer's demonstrated posture — including any selective freezing or failure to freeze a known illicit balance within a stated window — is documented so the allocator can weigh both freeze risk and duty-of-care risk.
**Status**: Gap with action
**If Not Found — Gap Action**: Enumerate the settlement-asset issuer's freeze authority on-chain and document its demonstrated posture from transparency reports and any litigation; where the issuer can freeze the vault's own balance, or has shown an inconsistent freeze posture, record it as a critical condition. Maintain a monitoring trigger on any McCollum v. Circle ruling.
**Source / Precedent**: McCollum v. Circle (S.D.N.Y. 1:26-cv-03280, filed 14 Apr 2026): alleges ~$232M USDC was not frozen over roughly six hours despite notice, while Circle had selectively frozen 16 wallets nine days earlier — putting issuer freeze authority and duty-of-care squarely in issue. No tree field or monitoring trigger previously covered settlement-asset issuer freeze authority and posture.
**Criterion ID(s)**: 10.2
