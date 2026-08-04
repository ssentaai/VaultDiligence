# Adversarial Questions — VT-3a Tokenised Institutional Funds

**Applies when:** Management = delegated-offchain-IM. [Phase 3 (2026-07-09): dimension-keyed; filename retained as a historical label.]

Questions that BVI SPC and Cayman-domiciled tokenised fund vaults
do not want you to ask.
Seeded from: general RWA structural failure modes and redemption stress cases.
Updated after every VT-3a pack completed.

---

## Seeded Questions (from structural analysis)

### Redemption Waterfall

At which specific step in the redemption waterfall does the process
break under stress? Name the counterparty and the condition.

If the fund administrator and the tokenisation platform disagree on NAV
on the same day a large redemption is requested: whose number governs,
what is the resolution process, and what happens to the redemption
request during resolution?

What is the fund administrator's published SLA for processing redemption
instructions? Is this SLA contractual or aspirational? Where is it stated?

### Legal Structure

Is the legal isolation of the fund from the tokenisation platform's
insolvency confirmed in a legal opinion? If yes: who issued it, when,
and does it cover the specific token structure (not just the fund)?

In insolvency of the tokenisation platform: what is the legal mechanism
by which a depositor recovers their underlying asset? Name the specific
clause in the subscription agreement.

Is the token itself a security in any jurisdiction where the
fund's investors are domiciled? Has legal counsel opined on this?

### Custody

Are the underlying assets held in a bankruptcy-remote custody structure?
Is rehypothecation prohibited in the custody agreement and is this
prohibition stated in a document the depositor can read?

If the custodian fails: what is the recovery mechanism and the timeline?
Has this scenario been addressed in the fund's legal opinions?

### NAV and Pricing

How frequently is NAV calculated and by whom? Is there an independent
NAV calculation agent separate from the fund administrator?

If the underlying asset is illiquid (e.g. CLO tranches, private credit):
what is the mark methodology and who can challenge it?

### Onchain Wrapper

If there is a secondary market DEX wrapper: is the DEX price anchored
to the NAV by an arbitrage mechanism? Who executes the arbitrage?
What happens to the peg if the arbitrage mechanism fails during a
period when the primary redemption queue is long?

---

## Questions Added from Completed Packs

[None yet. Add after every VT-3a pack completion.]

Format:
Pack: [vault name] | Date: [YYYY-MM-DD]
Question: [what we should have asked]
Why missed: [why it was not in the initial adversarial brief]
Evidence that would close it: [what source or document]

---

## Questions Added from an ODD source Article (April 2026)

Source: cv5capital.io/insights/ai-in-fund-governance
Added: 2026-04-29

Question: At what cadence does the board receive governance information?
If quarterly board packs only: what mechanism catches a concentration breach,
counterparty deterioration, or valuation anomaly in week five of a quarter
before it reaches the board in week twelve?

Why this matters: The board pack model creates a four-to-six-week response
delay. For a tokenised fund with a fund administrator, custodian, and
tokenisation platform, a gap of this length between anomaly and board
escalation is a material governance weakness. An independent director
with no real-time interrogation capability cannot catch problems early.

Evidence to look for: Does the fund prospectus or offering memorandum
describe real-time oversight capability or continuous compliance monitoring?
Does the governance section describe how independent directors access
fund data between meetings? If silent: classify as G2.

What closes it: Written description of the oversight model between board
meetings, with named roles responsible for continuous monitoring and
escalation thresholds.


---

## Institutional Governance Questions (from DAO treasury RFP analysis)

Added: 2026-04-29
Source: First principles — standard institutional due diligence

**Fund manager / investment manager separation**

Are the fund manager (administration, NAV, investor relations) and investment
manager (portfolio decisions) separate legal entities with independent governance?
If the same entity controls both: no independent check on portfolio decisions.
Valuation disputes, fee overcharging, and self-dealing have no independent arbiter.

Evidence to look for: two separately incorporated entities with separate boards,
separate employees, and separate legal relationships to the fund.
If one entity: classify as material condition.

**Investment mandate drift**

Is the current on-chain allocation consistent with the stated investment mandate?
A vault marketed as conservative USDC lending that is actually deploying into
leveraged positions is a material misrepresentation. Verify on-chain allocation
against stated strategy at assessment date.

**First-loss capital**

Does the fund sponsor or manager hold a first-loss position that absorbs losses
before depositors are affected? Absence is not a disqualifier but is a relevant
alignment signal. Presence confirms sponsor has skin in the game.

**Cash flow diagram**

Has the issuer published a detailed cash flow diagram showing the complete path
from deposit to yield to redemption including all counterparties and jurisdictions?
If not: G3. Request from issuer. Required before positions above $1M.
