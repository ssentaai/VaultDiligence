# F-BRG-008

**Field ID**: F-BRG-008
**Category**: Bridging
**Sub-Category**: Rate Limiting
**Field Name**: Per-Route Rate Limiting
**What to Collect / Question to Answer**: Is rate limiting present and enforced at the bridge stack or app level as a standing property (not a stress contingency), configured per route with inbound and outbound sized separately, documented under route topology, and — where native rate limiting is unavailable — layered externally with equivalent enforceability?
**Data Type**: Boolean (present) + numeric limit (per route, per direction)
**Vault Types**: ALL (bridge-crossing vaults; N/A single-chain, state why)
**Collection Tier**: T2
**Pillar(s)**: P12
**Primary Source**: On-chain read of the rate-limit configuration enforced on each route, inbound and outbound, at the bridge stack or app level
**Fallback Source**: Vendor documentation publicly cross-referencing the native per-route rate limits (preferred where present, as an independent cross-check on the issuer's claim)
**Evidence Pathway**: Inspection-validatable — read the enforced inbound and outbound rate-limit values on each route from contract state; where limits are externally layered, inspect the layering contract to confirm equivalent enforceability.
**Institutional Standard**: Per-route, per-direction rate limits are enforced and documented on every route carrying vault exposure, with native limits publicly documented by the vendor preferred. Routes with material exposure and no effective rate limit are a critical condition — the worst-case single-transaction drain is unbounded.
**Status**: Gap with action
**If Not Found — Gap Action**: Read each route's inbound and outbound rate limits on chain. For any route with material exposure and no enforced limit, record RF44 critical condition and request that the issuer configure a binding per-route, per-direction limit (native, or externally layered with equivalent enforceability).
**Source / Precedent**: Wormhole, Feb 2022: a single forged message minted 120K wETH ($326M) in one transaction — a binding per-route limit bounds exactly this class of loss.
**Criterion ID(s)**: 12.8, RF44
