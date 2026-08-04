# F-BRG-011

**Field ID**: F-BRG-011
**Category**: Bridging
**Sub-Category**: Configuration Lifecycle
**Field Name**: Bridge Configuration Lifecycle — Initial / Review / Cadence / Decayed Lanes
**What to Collect / Question to Answer**: Is the bridge configuration governed end-to-end — initial per-lane limits proposed by the issuer at integration and documented per route and direction; independent review completed before the route goes live with divergences documented; re-evaluation at quarterly cadence and out-of-cycle on triggers (new chain, new liquidity venue, sustained transit-volume shift, material authority/verifier/limit change); and decayed lanes closed rather than left at elevated limits?
**Data Type**: Structured text (per lifecycle stage)
**Vault Types**: ALL (bridge-crossing vaults; N/A single-chain, state why)
**Collection Tier**: T2a
**Pillar(s)**: P12
**Primary Source**: Issuer integration records and risk-provider review documentation showing initial per-lane limits, the completed pre-launch review and its divergences, the quarterly and out-of-cycle re-evaluation cadence, and decayed-lane closure records
**Fallback Source**: On-chain read of currently open lanes and their limits, cross-checked against transit volume to surface decayed lanes left open at stale limits
**Evidence Pathway**: Third-party-evidenced — obtain the issuer's initial-limit proposal and the independent reviewer's pre-launch report and cadence records; corroborate decayed-lane closure by reading open lanes and their limits on chain against measured transit volume.
**Institutional Standard**: A documented lifecycle covering initial limits, pre-launch review, quarterly plus out-of-cycle re-evaluation, and decayed-lane closure under the same timelocked authority as rate-limit changes. Routes live without a completed review, or decayed lanes left open at stale limits, are critical conditions.
**Status**: Gap with action
**If Not Found — Gap Action**: Request the initial-limit proposal, the pre-launch review with divergences, and the cadence and decayed-lane closure records. Read open lanes on chain against transit volume; for any lane decayed toward zero usage but still at an elevated limit, name it and request closure under the rate-limit timelock authority.
**Source / Precedent**: A lane opened for a launch campaign and forgotten at its launch limits is an unwatched door: the attack surface persists after the traffic that justified it is gone (a published protocol risk framework §2.14, 9 Jun 2026).
**Criterion ID(s)**: 12.11
