# F-LEG-019

**Field ID**: F-LEG-019
**Category**: Legal
**Sub-Category**: Events of Default & Remedies
**Field Name**: Events of Default + Remedies Matrix
**What to Collect / Question to Answer**: Are there defined events of default or termination events (e.g. operator insolvency, regulatory action, reserve shortfall, covenant breach), and for each, what specific remedies and enforcement mechanisms are provided to holders (acceleration, forced liquidation, foreclosure on collateral, governance intervention)?
**Data Type**: Text
**Vault Types**: ALL
**Collection Tier**: T3
**Pillar(s)**: P1
**Primary Source**: Signed master agreement / subscription documents / PPM enumerating events of default and the remedy and enforcement mechanism mapped to each
**Fallback Source**: Operator-published legal terms or governing-law clause read for default and termination triggers; on-chain liquidation/foreclosure logic where remedies are encoded in contract
**Evidence Pathway**: Third-party-evidenced: obtain the executed legal agreement and confirm each named default event maps to an enforceable remedy; corroborate any on-chain enforcement mechanism (e.g. forced-liquidation function) by reading the contract that executes it.
**Institutional Standard**: Defined events of default (insolvency, regulatory action, reserve shortfall) are enumerated, and each is paired with a stated remedy and a named enforcement mechanism that turns a paper claim into a recoverable one — acceleration, forced liquidation, foreclosure, or governance intervention.
**Status**: Gap with action
**If Not Found — Gap Action**: Request the operator's full events-of-default schedule and the remedy/enforcement mechanism for each. The audited tree showed these terms hit the source file only across the entire framework; absence of a defined-default-to-remedy mapping is a G2 gap (request the agreement) or G3 (operator must draft and publish one).
**Source / Precedent**: Steakhouse §5.4 framework requirement: 'Are there defined events of default or termination events...? For each, what remedies and enforcement mechanisms are provided...?' The audit found these terms hit the source file only across the entire tree — the contractual machinery that turns a paper claim into a recoverable one was absent.
**Criterion ID(s)**: 1.3
