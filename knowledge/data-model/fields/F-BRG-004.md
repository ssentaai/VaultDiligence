# F-BRG-004

**Field ID**: F-BRG-004
**Category**: Bridging
**Sub-Category**: Library Pinning
**Field Name**: Send/Receive Library Pinning
**What to Collect / Question to Answer**: Are the receive libraries (or vendor equivalent) pinned so that a vendor-side authority compromise cannot silently change the verifier set or message-handling logic — with library upgrades requiring issuer explicit re-attestation rather than a vendor-controlled upgrade path, verifier-set changes gated by bridge-authority timelocks on every chain, and the pinned configuration documented in route topology?
**Data Type**: Boolean (pinned) + structured text (upgrade-authority path)
**Vault Types**: ALL (bridge-crossing vaults; N/A single-chain, state why)
**Collection Tier**: T2
**Pillar(s)**: P12
**Primary Source**: On-chain read of the receive-library configuration and the authority controlling library upgrades on each route, confirming pinning and the issuer re-attestation requirement
**Fallback Source**: Vendor documentation describing the default vs pinned library model and the upgrade-authority path (confirm against contract state)
**Evidence Pathway**: Inspection-validatable — read the configured receive library and its upgrade authority from contract state to confirm it is pinned and that changes require issuer re-attestation gated by a timelock, not a vendor-controlled path.
**Institutional Standard**: Libraries are pinned; library upgrades require issuer re-attestation; verifier-set changes are gated by bridge-authority timelocks on every chain; the pinned configuration is documented in route topology. Unpinned receive libraries on routes carrying vault exposure are a critical condition until pinning is in place.
**Status**: Gap with action
**If Not Found — Gap Action**: Read each route's receive-library configuration on chain. If a vendor-controlled upgrade path can change the library or verifier set without issuer re-attestation, record it as a critical condition and request that the issuer pin libraries and place changes behind a timelocked re-attestation.
**Source / Precedent**: Vendor-side authority compromise can rewire verification without the issuer ever signing — the attack needs no exploit of the issuer at all (a published protocol risk framework §2.4, 9 Jun 2026).
**Criterion ID(s)**: 12.4
**Registered Sources (Fix 70)**: layerzero-scan-dvn (candidate)
