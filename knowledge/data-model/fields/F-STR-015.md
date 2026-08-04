# F-STR-015

**Field ID**: F-STR-015
**Category**: Strategy Risk
**Sub-Category**: Restaking
**Field Name**: Restaking Modality — Native vs LRT
**What to Collect / Question to Answer**: Does the vault restake *natively* (direct EigenPod / operator delegation, no liquid receipt) or does it hold / issue a *liquid restaking token* (LRT — e.g. ezETH, rsETH, weETH)? If LRT: name the issuer and receipt token, state its backing (1:1 redeemable through the unbonding queue, or reserve-backed?), and whether the vault holds the canonical or a bridged representation of the LRT.
**Data Type**: Enum `{ native-restaking | LRT-holder | LRT-issuer }` + LRT detail `{ issuer, receipt_token, backing_basis, canonical_or_bridged, chain }`.
**Vault Types**: `Strategy = restaking`
**Collection Tier**: T1
**Pillar(s)**: P4 (Collateral). *(propose; operator confirms)*
**Primary Source**: Vault on-chain composition — the restaked position or the held / issued receipt token; the LRT contract for issuer and backing.
**Fallback Source**: Protocol documentation stating the restaking modality and LRT backing.
**Evidence Pathway**: Inspection-validatable — read the vault's holdings on-chain to classify native vs LRT, and read the LRT contract (and any bridge/lockbox) to confirm issuer, backing, and canonical-vs-bridged status.
**Institutional Standard**: The modality is stated unambiguously; for an LRT, the issuer, receipt token, backing basis, and canonical-or-bridged status are recorded so the allocator knows whether the position carries LRT depeg / bridge / secondary-market risk on top of the restaking risk.
**Status**: Gap with action
**If Not Found — Gap Action**: E if the modality and (for LRT) issuer / backing / canonical-vs-bridged are readable on-chain and dated. E(P) if the modality is clear but the LRT backing basis is undocumented. G2 if backing terms exist but are unpublished. G3 if no backing basis is defined for the receipt token. N/A never for a restaking vault — modality is always determinable.
**Source / Precedent**: Sevim & Ferreira Torres, arXiv:2604.03274 — the LRT-vs-native distinction; the LRT wrapper adds depeg, bridge, and secondary-market risk beyond native restaking. Buzko Krasnov, 27 Apr 2026 — rsETH receipt model.
**Criterion ID(s)**: propose at ratification.
