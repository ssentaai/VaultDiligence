---
source_id: S50
name: Webacy DD APIs
tier: T2a
type: Automated blockchain risk intelligence — contract, address, token, vault
url: https://docs.webacy.com/
dashboard: https://dd.xyz
pricing: Enterprise — contact required. Not self-serve. Not free.
added: 2026-04-29
---

# S50 — Webacy DD APIs

## What It Is

Enterprise-grade automated blockchain risk intelligence. Covers contract
vulnerability detection, address/wallet screening, token security analysis,
vault risk scoring (Vault Universe — 2,800+ vaults, 6 chains), stablecoin
depeg monitoring (DEWS early warning system), and sanctions screening.

Their DD.xyz dashboard exposes most functionality without an API key.
Use dd.xyz for manual lookups during investigation. API integration
requires enterprise contract.

## What It Covers

**Contract risk tags (200+)**
Structured vulnerability taxonomy. Key tags for vault investigations:
  centralized_risk_high/medium/low — drainer-like logic in contract
  mint_high/low — arbitrary minting risk
  unprotected_upgrade — contract can be self-destructed
  pess_unprotected_initialize — initialize function can be hijacked
  arbitrary_send_erc20 — approval allows attacker to drain tokens
  reentrancy_with_eth_transfer — reentrancy attack vector
  hidden_owner — hidden ownership enabling post-renouncement control
  owner_change_balance — owner can modify anyone's balance

**Vault Universe**
2,800+ vaults scored across 6 chains. 15 sub-scores, additive penalties,
hard floors, listing verdicts, withdrawal risk, incident history.

**DEWS — Depeg Early Warning System**
11 forward-looking pre-depeg signals. Surfaces stress 6-48h before price
breaks. Threat bands: CALM / WATCH / ALERT / DANGER.
Relevant for any vault holding stablecoin collateral or issuing stablecoins.

**Address and wallet screening**
Sanctions (OFAC + global), hacker associations, mixer usage, drainer activity,
fund flow to sanctioned entities.

## What It Does NOT Cover

Redemption waterfall structure (counterparty T+N).
Legal entity verification (use GLEIF for this).
Governance structure and DAO accountability.
Team identity confirmation.
These require VaultDiligence investigation criteria and T1 sources.

## How to Use in a VaultDiligence Investigation

**Contract-reading skill**
When the ABI read surfaces a vulnerability, classify it using the Webacy
tag vocabulary rather than free text. Structured tags improve consistency
across investigations and make the field machine-readable in the structured output.

Example:
  NOT: "The contract may have a vulnerability allowing re-initialization"
  YES: "pess_unprotected_initialize detected — initialize function can be
        hijacked by attacker. Source: Webacy tag taxonomy, docs.webacy.com/
        essentials/risk-tags. Verify on-chain before classifying."

**OFAC/sanctions screening**
Webacy OFAC screening can cross-reference against our primary OFAC SDN
list query. Use as a corroboration source, not a sole source.

**Vault Universe**
When a Webacy vault score exists for the subject vault: cite it in the
Operational Risk section as T2a evidence. Note: automated heuristic score,
not a primary source. Always verify material findings on-chain.

**DEWS signals (manual)**
For vaults with stablecoin exposure: check dd.xyz depeg monitor for the
relevant stablecoin before investigation. Threat band WATCH or above is a
flag to add a monitoring note to the pack.

## Citation Format

Evidence state: E(P) for Webacy outputs (automated heuristic, not primary).
Never E — automated detection requires on-chain verification.

Format:
  "Webacy contract scan — [tag name] detected on [contract address].
  Source: dd.xyz/contract/[address], [date].
  Note: automated heuristic. Verified on-chain at [etherscan URL]: [finding]."

## Source Bias and Limitations

Automated heuristics produce false positives. A centralized_risk_medium
tag does not mean the contract is malicious — it means a pattern
consistent with centralisation risk was detected. Always verify the
specific function flagged before citing in a pack.

Webacy is not a neutral academic source. They have commercial interests
in their risk scoring products. Cite as T2a (expert analysis tool),
never as FORMAL.

The enterprise API requires a sales conversation. For investigation use:
  Manual lookups: dd.xyz (free dashboard)
  Vocabulary reference: docs.webacy.com/essentials/risk-tags
  API integration: only justified at scale with enterprise agreement
