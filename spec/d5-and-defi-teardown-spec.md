# D5 Interview Framework — Specification

## Purpose

Pre-populated questions for each named counterparty in a vault investigation.
Questions derive from open D4 gaps. Standard question library per entity type.
Verbatim response recording. Used to close T4 gaps that cannot be resolved
from public sources.

a preferred-equity-backed vault interview questions: packs/example-vault/example-crawl-map.md
Use that pack as a worked example. Do not replicate vault-specific
questions here.

---

## Counterparty Categories

| Category | Entity type examples | Applies to vault types |
|----------|---------------------|----------------------|
| A — Issuer / Protocol Founder | Protocol team, fund manager | All |
| B — Investment Manager | Asset manager, strategy team | VT-3, VT-3a, VT-8 |
| C — Fund Administrator | the fund administrator, APEX, SS&C | VT-3, VT-3a, VT-8 |
| D — Custodian (crypto) | BitGo, Anchorage, Copper, Coinbase Custody | VT-1, VT-2, VT-3, VT-5 |
| E — Prime Broker (TradFi) | Institutional prime broker | VT-8 |
| F — Execution Broker | Crypto or TradFi execution desk | VT-8 |
| G — Tokenisation Platform | Centrifuge, Securitize, Ondo | VT-3, VT-3a, VT-7 |
| H — Legal Counsel | External legal firm | All |
| I — Curator | Steakhouse, Gauntlet, Re7 | VT-1, VT-6, VT-7 |
| J — Risk Monitor | LlamaRisk, Chaos Labs, Hypernative | All |
| K — Financial Auditor | Big 4 or specialist crypto auditor | VT-3, VT-4, VT-8 |
| L — Oracle Provider | Chainlink, Pyth, Chronicle | All |

---

## Standard Question Library per Category

Questions apply to any vault of the relevant type.
Replace {vault-name}, {token}, {underlying} with actual values.

### Category A — Issuer / Protocol Founder

1. Walk me through the complete deposit and redemption path from {deposit-asset}
   to {token} and back. Name every counterparty and their settlement time.
2. What is the legal structure governing the {token} holder's claim?
   Is there a written legal opinion confirming enforceability?
3. Where are the privileged signing keys stored? AWS KMS, HSM, or MPC wallet?
   Who has access and what is the threshold?
4. Has off-chain infrastructure been explicitly in scope for any security audit?
   Which firm? When? What was out of scope?
5. What is the wind-down procedure? Who acts as independent trustee?
   What is the recovery timeline for depositors?
6. What is the documented process if a multisig signer is compromised
   or unavailable?
7. Has your team received any communications from regulators about this
   product's classification under applicable law?
8. What is the secondary yield source or floor if the primary yield
   mechanism is unavailable?

### Category B — Investment Manager

1. What is the investment mandate? Is current collateral concentration
   a policy choice or a transitional state?
2. What are the trigger conditions for shifting between collateral types
   under the risk model?
3. How frequently is the portfolio rebalanced? Who authorises rebalancing?
4. What is the stress scenario where you would reduce {primary-collateral}
   exposure? What is the execution timeline?
5. What is the maximum position size of {primary-collateral} relative to
   total outstanding supply?

### Category C — Fund Administrator

1. What is your specific role in the {vault-name} structure?
2. How often do you calculate NAV? What pricing sources do you use?
3. What happens to your NAV calculation if {primary-collateral} trades
   below par or book value?
4. What KYC/AML procedures apply to minting? Who conducts the KYC check?
5. What are your redemption processing SLAs? Under what conditions
   would you gate redemptions?

### Category D — Custodian (crypto)

1. Confirm the exact segregation model. Are client assets held in a
   separate legal entity?
2. Is there an explicit contractual prohibition on rehypothecation?
   Provide the clause reference.
3. What insurance covers custodied assets? Carrier, amount, covered
   perils, renewal date.
4. What percentage of assets are in cold storage vs hot wallet?
5. What is the key management implementation (OES, MPC, HSM)?

### Category E — Prime Broker (TradFi)

1. Confirm SIPC membership. Provide the SIPC member reference number.
2. What are the rehypothecation rights under the prime brokerage agreement?
   Are they waived?
3. What is the standard settlement timeline for {primary-collateral} sell
   orders in normal and stressed markets?
4. What happens to client securities in a prime broker insolvency?
   What is the regulatory process and typical timeline?
5. Is execution and custody held by the same entity or separated?

### Category F — Execution Broker

1. What is the execution SLA for a {primary-collateral} sell order
   of $1M, $5M, $10M?
2. What is the typical bid-ask spread at those sizes?
3. What happens to an in-flight order if your systems are unavailable?
4. Do you maintain a market-making commitment? Under what conditions
   would you withdraw?

### Category G — Tokenisation Platform

1. Walk me through the exact on-chain mechanism for {token} minting
   and redemption.
2. Who controls the contract upgrade mechanism? What is the timelock?
3. Who holds the pause function? Under what conditions would you pause?
4. What is the oracle configuration for the NAV feed? Update frequency
   and staleness threshold?
5. What is the cross-chain architecture? If the primary chain contract
   is paused, what happens on other chains?

### Category H — Legal Counsel

1. Has your firm produced a written opinion on the enforceability of the
   {token} holder's claim?
2. What is the governing law for the token holder's claim?
3. Is {token} a security under applicable law? What is your analysis?
4. What jurisdiction and dispute resolution mechanism applies to
   token holder claims?
5. What are the conditions under which the token holder's claim would
   be subject to insolvency proceedings of any counterparty?

### Category I — Curator

1. What is your documented process for monitoring {primary-collateral}
   price vs par or book value?
2. What are your automated circuit breaker conditions for this vault?
3. Have you been through a live stress event with this vault or a
   comparable strategy? What happened?
4. Do you have your own capital deployed in this vault?
5. What is your conflict of interest policy regarding advisory
   relationships with protocol teams whose tokens you accept?

### Category J — Risk Monitor

1. What is the scope of your monitoring mandate for this vault?
2. What on-chain conditions trigger an alert? What is the alert
   escalation process?
3. Have you issued any risk alerts or recommendations for this vault
   in the last 12 months?
4. What is your assessment of the primary tail risk for this vault?
5. Are you compensated by the protocol or independently?

### Category K — Financial Auditor

1. What is the scope of your audit engagement for this vault?
2. What financial statements do you audit? What period?
3. Are fund assets confirmed as existing and correctly valued as of
   audit date?
4. Did your audit include review of custody arrangements?
5. What were the findings of the most recent audit?

### Category L — Oracle Provider

1. What is the update frequency for the NAV or price feed for this vault?
2. What is the staleness threshold before the feed is considered stale?
3. Who can update or change the oracle configuration?
4. What is the failover mechanism if the primary oracle is unavailable?
5. Has this oracle feed ever deviated materially from the true underlying
   value? When and why?

---

## Interview Record Template

```yaml
---
interview_id: INT-{vault-slug}-{NNN}
vault: {vault-slug}
counterparty_category: {A through L}
entity: {organisation name}
interviewee_name: {full name}
interviewee_title: {role}
interviewee_email: {email}
date: {YYYY-MM-DD}
method: Video call / Email / In-person
interviewer: {VaultDiligence analyst name}
gaps_addressed: [{gap-id-1}, {gap-id-2}]
---
```

## Questions and Responses

### Q1: {Question text}

**Response:** {Verbatim or direct paraphrase with interviewee confirmation.
Note: "verbatim" or "paraphrase confirmed by {name} on {date}"}

**Gap closed:** {Gap ID if this response closes a gap — Y/N/Partial}
**Evidence state update:** {G2 → E | G2 → E(P) | remains G2}
**Follow-up required:** {Y/N — if yes: what}

---

# DeFi-Native Teardown — Format Specification

## Purpose

Same D3 data. Four paragraphs. DeFi-native language.
For an analyst who will verify on-chain in parallel.
Lead with numbers. No institutional framing. No hedging language.

---

## Format Rules

Maximum four paragraphs. No section headers inside the paragraphs.
Numbers first, context second. Cite sources in brackets.
If something is not confirmed: say so directly and state what is missing.
No scoring language. No verdicts.

---

## Paragraph Structure by Vault Type

### VT-1 (DeFi Lending)

Paragraph 1: TVL, utilisation rate, withdrawable liquidity today,
net APY (share price basis), LLTV per market, oracle last update age,
max position at 1% slippage (1inch confirmed).

Paragraph 2: Curator identity and track record (bad debt history named),
automated allocation (Public Allocator yes/no, circuit breaker yes/no),
governance (multisig threshold, timelock hours), audit firm and date,
bug bounty ($M), privileged roles enumerated.

Paragraph 3: Loop exposure multiplier, oracle type (hardcoded vs updatable),
collateral DEX depth at $10M, Nash equilibrium utilisation threshold,
any triggered conditions from the investigation.

Paragraph 4: Open gaps. What could not be confirmed. Who holds it.
Specific ask.

### VT-3a (Tokenised Institutional Fund)

Paragraph 1: AUM/TVL, net APY (share price basis), yield source and type,
max position at 1% slippage, standard redemption timeline every step named,
oracle last update age.

Paragraph 2: Legal structure (entity, jurisdiction), fund administrator,
custodian, tokenisation platform, audit status, bug bounty.
Mechanism of yield: what produces it, who controls it, how it reaches
the token holder.

Paragraph 3: Redemption waterfall bottleneck (name the slowest step and
the condition that extends it), legal opinion status (Y/N),
rehypothecation confirmation (Y/N), any triggered conditions.

Paragraph 4: Open gaps. What could not be confirmed. Who holds it.
Specific ask.

### VT-8 (TradFi-Primary / Onchain-Wrapped)

Paragraph 1: TVL, net realised yield (single number, share price basis),
yield obligation type (contractual vs discretionary), underlying
concentration (% and named issuer), max position at 1% slippage,
standard redemption timeline every step named.

Paragraph 2: Structure (what the underlying instrument is, who manages it,
how yield reaches the token), custody (prime broker + SIPC status,
crypto custodian), tokenisation platform, oracle for NAV, audit status.

Paragraph 3: Key risks specific to this vault: yield mechanism
(what suspends it, under what conditions), single underlying concentration,
return of capital vs income classification if applicable, off-chain
signing key risk, redemption chain bottleneck.

Paragraph 4: Open gaps. What could not be confirmed. Who holds it.
Specific ask.

### Other vault types

Follow the same four-paragraph structure:
P1: The numbers that matter most for this vault type.
P2: The structure and counterparties.
P3: The risks that matter for this vault type specifically.
P4: The open gaps.

Derive from knowledge/framework/vault-types/{VT-X}.md for the
specific metrics and risk factors relevant to each type.

---

## Worked Example

The preferred-equity-backed vault investigation (VT-8) is the first worked example.
Interview questions and teardown output:
packs/example-vault/

Do not replicate a preferred-equity-backed vault-specific content in this spec file.
This spec defines the pattern. The pack contains the application.
