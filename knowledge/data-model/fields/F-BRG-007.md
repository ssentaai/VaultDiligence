# F-BRG-007

**Field ID**: F-BRG-007
**Category**: Bridging
**Sub-Category**: Bridge-Layer Custody
**Field Name**: Bridge-Layer Custody — Both Sides, Weaker Governs
**What to Collect / Question to Answer**: Is institutional-grade key custody confirmed on every authority that can affect vault-relevant bridged assets (mint, burn, pause, rate-limit change) on both the bridge-stack side and the issuer side — with arrangements disclosed, custody changes disclosed in advance as material changes, and the weaker of the two sides recognised as governing the surface?
**Data Type**: Structured text (per authority, per side)
**Vault Types**: ALL (bridge-crossing vaults; N/A single-chain, state why)
**Collection Tier**: T2a
**Pillar(s)**: P12
**Primary Source**: Issuer and bridge-vendor custody disclosure (under NDA where reasonable) naming the custody arrangement for each mint/burn/pause/rate-limit authority on both sides, cross-referenced to the on-chain signer surface
**Fallback Source**: On-chain read of the signer set and quorum behind each authority (a single EOA or sub-honest-majority multisig is a custody finding regardless of stated arrangement)
**Evidence Pathway**: Third-party-evidenced — obtain the named custody arrangement for each authority on both the bridge-stack and issuer sides from the operators' disclosures, corroborated by reading the on-chain signer surface behind each authority.
**Institutional Standard**: Institutional-grade key custody on both bridge-stack and issuer authorities, disclosed and current. Weak custody on either side, or undisclosed arrangements, is a critical condition — the weaker side sets the exposure.
**Status**: Gap with action
**If Not Found — Gap Action**: Enumerate every mint/burn/pause/rate-limit authority on both sides and obtain the custody arrangement for each. Where either side is undisclosed or resolves on chain to a single key or sub-honest-majority multisig, record the weaker side as governing and flag it as a critical condition.
**Source / Precedent**: Ronin, Mar 2022: five of nine validator keys compromised, $625M lost. Multichain, Jul 2023: CEO-held keys, $126M gone with one person. Bridge custody failures are total-loss events.
**Criterion ID(s)**: 12.7 (cross-ref F-CTR-015)
