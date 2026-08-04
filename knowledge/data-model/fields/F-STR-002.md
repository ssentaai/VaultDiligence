# F-STR-002

**Field ID**: F-STR-002
**Category**: Strategy Risk
**Sub-Category**: Lending — Rate Model
**Field Name**: Interest-Rate-Model Control & Manipulation Surface
**What to Collect / Question to Answer**: Two facts. (1) CONTROL: is the IRM immutable per market, or can an authority (curator, governance, admin) swap or reparameterise the rate model for a market the vault is in — and if so, who holds that authority and under what timelock? (2) MANIPULATION: can the utilisation input that drives the rate be cheaply griefed — e.g. an actor borrowing to spike utilisation and force the jump rate, or repaying to suppress it — and does any cap or design limit that? Source: contract read of the IRM-setter / access control, plus the market's borrow-cap and utilisation state.
**Data Type**: Structured (IRM-mutability boolean; setter authority + timelock; utilisation-manipulation surface described; any mitigating cap)
**Vault Types**: Strategy = lending
**Collection Tier**: T2
**Pillar(s)**: P7 (propose; secondary P4)
**Primary Source**: On-chain access-control read of the IRM-setter function / market admin role; borrow-cap and utilisation state read on-chain
**Fallback Source**: Governance documentation and curator security disclosures on parameter-change authority
**Evidence Pathway**: Inspection-validatable — read whether the market's IRM can be changed and by whom (and any timelock), and inspect whether utilisation can be moved cheaply enough to manipulate the rate; a swappable IRM or an unbounded utilisation input is a control the allocator must see.
**Institutional Standard**: What a well-run vault evidences: the mutability of each market's IRM and the identity + timelock of any authority able to change it are disclosed; where the rate model is immutable per market, that is stated; the utilisation-manipulation surface and any mitigating cap are described rather than left implicit.
**Status**: Gap with action
**If Not Found — Gap Action**: Read the IRM-setter access control and record mutability + authority + timelock (E). If the authority exists but its constraints are undocumented, mark E(P) and name the role. If the setter cannot be enumerated on-chain and is not disclosed, classify G2. If the vault supplies only immutable-IRM markets with capped borrow, state that as the evidenced control.
**Source / Precedent**: Morpho Blue markets are immutable per market (IRM fixed at market creation), so the control question routes to the *curator's* choice of which markets to allocate to — `docs.morpho.org/curate/concepts/security-considerations/`. Contrast: pooled protocols where governance/admin can reparameterise the rate model. Manipulation anchor: utilisation-griefing (borrow-to-spike / repay-to-suppress) is a known lending grief where borrow caps are absent.
**Criterion ID(s)**: propose 7.2 (parameter-change control) + cross-ref F-CUR-008 (change log) (leave for ratification)
