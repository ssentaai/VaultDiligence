# Adversarial Questions — VT-8 TradFi-Primary / Onchain-Wrapped

**Applies when:** Exposure in {equities, corporate-fixed-income, sovereign-fixed-income} AND venue = tradfi-primary. [Phase 3 (2026-07-09): dimension-keyed; filename retained as a historical label.]

Questions that vaults whose primary yield instrument is a publicly
traded security (listed equity, preferred stock, bond, ETF, MMF) wrapped
onchain do not want you to ask.
Seeded from: P0 VT-8 classification note, a preferred-equity-backed vault/a preferred-equity-backed token structural analysis,
an ODD source fund-governance ingestion, and TradFi prime-brokerage failure cases.
Updated after every VT-8 pack completed.

---

## Seeded Questions (from structural analysis)

### Instrument & Issuer

What exactly is the primary instrument, who is the corporate issuer, and
on what exchange is it listed? Is the corporate issuer's solvency the real
backing of the vault token? (cf. a listed preferred instrument issued by a corporate issuer.)

Is the headline yield contractual or discretionary? A preferred-equity
dividend can be suspended without default. What is the issuer's cash-reserve
coverage and for how many months? (F-FIN-086, P6.7)

Has any portion of distributions been classified as return of capital for
tax purposes? Return of capital is not income — it reduces basis. Does the
vault disclose this to depositors? (P10.6)

### Custody (TradFi, not crypto)

Is the underlying security held at a SIPC-member prime broker? SIPC covers
securities, not crypto, and only to a limited per-account amount. Is
rehypothecation explicitly prohibited in the prime-brokerage agreement, or
does the broker retain standard rehypothecation rights? (P2.11)

Are execution and custody held by the same entity or separated? What is the
prime broker's own financial health and stress-event track record?

In prime-broker insolvency, what is the recovery mechanism and timeline for
the underlying securities, and who bears the months-long gap?

### Wrapper & Settlement Chain

What is the full settlement chain from onchain token to the listed security,
and what is the aggregated redemption timeline across every counterparty
(tokenisation platform, transfer agent, prime broker, custodian)? (F-LIQ-013)

If the tokenisation layer fails, is there a paper-certificate or off-chain
recovery path to the underlying security? (F-TECH-006)

Does the onchain NAV track the listed instrument's market price, its par, or
an issuer-stated value — and what happens when they diverge intraday?

### Concentration

Is the vault's yield and value dependent on a single listed instrument or a
single corporate issuer? What is the secondary yield floor if that issuer
suspends the distribution or the instrument trades below par? (P6.8)

### Board Cadence & Escalation (mandated — an ODD source fund-governance ingestion)

At what cadence does the board receive governance information? If quarterly
board packs only: what mechanism catches a concentration breach, counterparty
deterioration, or valuation anomaly in week five of a quarter before it
reaches the board in week twelve? Do independent directors have any capability
to interrogate exposure, compliance status, and NAV integrity between meetings,
or do they operate only on manager-prepared packs? (F-GOV-021)

What is the documented escalation pathway when a concentration or NAV anomaly
is detected — who is alerted, at what threshold, and within what response
window? (F-GOV-021, RF34)

---

## Questions Added from Completed Packs

[None yet. Add after every VT-8 pack completion.]

Format:
Pack: [vault name] | Date: [YYYY-MM-DD]
Question: [what we should have asked]
Why missed: [why it was not in the initial adversarial brief]
Evidence that would close it: [what source or document]
