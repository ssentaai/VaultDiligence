# F-TECH-006

**Field ID**: F-TECH-006
**Category**: Technology
**Sub-Category**: RWA-Specific
**Field Name**: Tokenisation-Layer Failure Fallback
**What to Collect / Question to Answer**: If the tokenisation layer or its smart contracts cease to function, what is the documented fallback by which a holder's claim on the underlying asset is preserved and recovered off-chain — for example paper-share-certificate issuance or a transfer-agent register?
**Data Type**: Text / Y-N (fallback exists, mechanism named, who executes, time to recover)
**Vault Types**: Exposure in {private-credit,structured-credit} OR Management=delegated-offchain-IM OR Structure in {leveraged,looped} OR (Exposure in {equities,corporate-fixed-income,sovereign-fixed-income} AND venue=tradfi-primary)  (derived from VT-N; original "Vault Types" value: VT-3, VT-3a, VT-7, VT-8)
**Collection Tier**: T3
**Pillar(s)**: P7
**Primary Source**: Offering memorandum / fund constitutional documents describing the off-chain share register and certificate fallback
**Fallback Source**: Transfer agent or fund administrator confirmation of the off-chain register and recovery process
**Evidence Pathway**: Third-party-evidenced: read the offering memorandum and fund articles for the documented paper-certificate or off-chain-register fallback, corroborated by the named transfer agent or administrator confirming the recovery process and who is entitled to invoke it.
**Institutional Standard**: Good looks like an explicitly documented mechanism by which, if the tokenisation contracts cease to function, a holder's beneficial claim is preserved on an off-chain register and can be reissued (for example as a paper share certificate), naming who executes it and the conditions that trigger it — so that smart-contract failure is not equivalent to loss of the claim.
**Status**: Gap with action
**If Not Found — Gap Action**: Request the offering memorandum section and transfer-agent confirmation describing the off-chain register and certificate-reissuance process. If no fallback is documented, classify as G3 and state that contract failure would leave the holder with no documented off-chain recovery path.
**Source / Precedent**: a synthetic-dollar and CLO-fund diligence, LlamaRisk Part 2 (7 Jun 2026), §I: notes 'fallback paper-share-certificate issuance where Centrifuge or the smart contracts cease to function' for the tokenized CLO fund issuer structure (the issuer's company registration number).
**Criterion ID(s)**: 7.6
