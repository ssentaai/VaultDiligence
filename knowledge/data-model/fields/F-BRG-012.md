# F-BRG-012

**Field ID**: F-BRG-012
**Category**: Bridging
**Sub-Category**: Stack Infrastructure Risk
**Field Name**: Bridge-Stack Infrastructure-Risk Evaluation
**What to Collect / Question to Answer**: For each cross-chain stack in the dependency chain, has the assessment covered all five dimensions — vendor and attestor operational security; code quality and audit reports for on-chain and off-chain components; novel architectural attack surfaces unique to the design; exploit history including recurrence and remediation quality; and the standing monitoring effort the stack demands?
**Data Type**: Structured text (per stack, per dimension)
**Vault Types**: ALL (bridge-crossing vaults; N/A single-chain, state why)
**Collection Tier**: T2a
**Pillar(s)**: P12
**Primary Source**: Vendor and attestor security disclosures, published audit reports for the stack's on-chain and off-chain components, and the documented exploit history with remediation evidence for each stack in the dependency chain
**Fallback Source**: Independent security-research and incident post-mortems on the stack; the issuer's enumeration of every cross-chain stack in the dependency chain (cross-ref F-CTR-019)
**Evidence Pathway**: Third-party-evidenced — for each stack, obtain the named audit reports and post-mortems, the vendor/attestor operational-security disclosures, and the documented exploit-and-remediation history, then state the standing monitoring effort each stack demands.
**Institutional Standard**: Each stack is assessed on all five dimensions with sources cited. Stacks whose monitoring cost is disproportionate to the exposure they secure are findings. Un-assessed stacks in the dependency chain are gaps, not assumed-safe defaults.
**Status**: Gap with action
**If Not Found — Gap Action**: Enumerate every cross-chain stack in the dependency chain (cross-ref F-CTR-019) and, for each, obtain operational-security disclosures, audit reports, novel-attack-surface analysis, and exploit/remediation history. Mark any un-assessed stack as a gap, not an assumed-safe default, and state the monitoring effort it demands.
**Source / Precedent**: Every bridge stack added to a dependency chain is an independent failure vector — compounded, not averaged, across the chain (a published protocol risk framework §2.15, 9 Jun 2026; cf. F-CTR-019 full bridge enumeration).
**Criterion ID(s)**: 12.12
