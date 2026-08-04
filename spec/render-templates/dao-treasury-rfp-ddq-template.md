---
template_id: DAO-RFP-DDQ-v1
template_name: DAO Treasury RFP Questionnaire
description: >
  Standard questionnaire structure used by DAO treasury committees when
  evaluating yield vault products for treasury allocation. Derived from
  common elements across multiple DAO RFP processes. Not Arbitrum-specific.
  Industry-standard questions for institutional DeFi treasury evaluation.
added: 2026-04-29
relevant_vault_types: [VT-1, VT-3a, VT-7, VT-8, VT-9]
---

# DAO Treasury RFP DDQ — Standard Template

When a subscriber is responding to a DAO treasury RFP, use /render-custom
with this template. VaultDiligence maps the evidence register to these sections.

## Section 1: Applicant Information

Name of entity
Address and jurisdiction
Primary contact name and title
Website and governance forum handle

VaultDiligence mapping:
  F-ENT-001 (entity name) → Name of entity
  F-ENT-002 (jurisdiction) → Address and jurisdiction
  F-ENT-003 (team identity) → Primary contact

## Section 2: Product Overview

Description of proposed product and underlying assets.
Target yield and basis (gross/net, methodology).
Expected maturity or duration.
Minimum and maximum transaction size.
Current AUM for this product.
Current AUM for the issuer overall.

VaultDiligence mapping:
  F-COL-001 (TVL) → Current AUM for product
  F-FIN-010 (net APY) → Target yield
  F-FIN-011 (gross APY) → Gross yield
  F-LIQ-001 (min transaction) → Minimum transaction size

## Section 3: Legal and Structural

Describe legal and contractual structure. Identify all legal jurisdictions.
Are investor assets bankruptcy remote from the issuer entity?
Provide the legal basis for bankruptcy remoteness.
Does the issuer issue more than one asset class? Priority relationships?
Is there separation between fund manager and investment manager (F-ENT-010)?

VaultDiligence mapping:
  F-LEG-001 (legal structure) → Legal and contractual structure
  F-LEG-010 (bankruptcy remoteness) → Bankruptcy remote basis
  F-ENT-010 (FM/IM separation) → Manager separation

## Section 4: Cash Flow Diagram

Provide a detailed cash flow diagram showing:
  Flow of funds from deposit to investment in underlying asset.
  Payment of expenses and fees.
  Sale of underlying asset and return to depositor.
  All counterparties and legal jurisdictions at each step.

VaultDiligence mapping:
  Yield dependency chain diagram (VT-8/VT-3a) → Cash flow diagram
  F-LIQ-010 (redemption waterfall) → Return flow
  F-ENT-005 (custody chain) → Counterparties

## Section 5: Risk Management

Describe risk management framework for normal and stressed conditions.
What quantitative risk metrics are produced (VaR, stress tests)? (F-OPS-030)
What is the time-to-liquidity and are there any lockup periods?
How are strategies unwound in emergencies?
What is the depeg risk for any stablecoin components?

VaultDiligence mapping:
  F-OPS-030 (quantitative risk reporting) → Risk metrics
  F-LIQ-020 (redemption timeline standard) → Time to liquidity
  F-LIQ-021 (redemption timeline stress) → Emergency unwinding

## Section 6: Conflict of Interest Disclosure

Does the entity or key personnel have conflicts of interest? (F-GOV-020)
Does the manager hold positions in assets it recommends for allocation?
Are there advisor relationships with counterparty protocols?
Has a formal conflict of interest policy been published?

VaultDiligence mapping:
  F-GOV-020 (conflict of interest disclosure) → Full section
  Social-map.md → Supplementary CT-level conflicts

## Section 7: Performance Reporting

Proposed performance benchmarks and rationale.
Format, frequency, and preparation process for performance reports.
Who provides the reports?
Formal audit process and timing.

VaultDiligence mapping:
  F-OPS-020 (reporting cadence) → Frequency
  F-OPS-021 (reporting format) → Format and content
  F-SEC-003 (audit status) → Audit process

## Section 8: Smart Contract and Architecture

How many audits and by which auditors? (F-SEC-001)
Is the product permissioned? How are identities managed? (F-SEC-005)
Is it present on multiple chains? Cross-chain interactions? (F-SEC-010)
How are trusted roles and admins managed? (F-SEC-006)
First-loss capital: amount, denomination, source? (F-FIN-050)

VaultDiligence mapping:
  F-SEC-001 (audit count and names) → Audits
  F-SEC-005 (permissioning) → Identity management
  F-SEC-006 (privileged roles) → Trusted roles
  F-SEC-010 (cross-chain) → Multi-chain presence
  F-FIN-050 (first-loss capital) → First-loss section

## Section 9: Fees and Compensation

Management fee (basis points per annum).
Performance fee (if any).
Minting and redemption fees.
Fee payment frequency and position in cash waterfall.

VaultDiligence mapping:
  F-FIN-030 (management fee) → Management fee
  F-FIN-031 (performance fee) → Performance fee
  F-FIN-032 (redemption fee) → Redemption fee

## Gaps Section

Any field in the above sections classified as G2 or G3 in the evidence
register will be listed here with the responsible party and action required.
The allocator reads the gaps and decides what to request before allocating.
