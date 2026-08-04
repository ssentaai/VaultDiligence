# F-BRG-002

**Field ID**: F-BRG-002
**Category**: Bridging
**Sub-Category**: Verifier Threshold
**Field Name**: Verifier-Set Threshold — Minimum Three Independent
**What to Collect / Question to Answer**: Does every route carrying vault exposure have at least three independent verifiers (validators, attestors, nodes, or message verifiers), counting a verifier network run by a single organisation as one trust domain regardless of internal node count — and is the configuration vendor-default or operator-chosen?
**Data Type**: Integer count (per route) + Boolean (vendor-default flag)
**Vault Types**: ALL (bridge-crossing vaults; N/A single-chain, state why)
**Collection Tier**: T2
**Pillar(s)**: P12
**Primary Source**: On-chain read of the verifier/attestor/DVN set configured on the receive side of each route, collapsed to independent operator/trust domains
**Fallback Source**: Bridge vendor configuration documentation naming the verifier operators (treated as a claim to confirm on chain, not as the terminal source)
**Evidence Pathway**: Inspection-validatable — read the configured verifier set on each route directly from contract state and count distinct operating organisations; do not rely on vendor documentation alone.
**Institutional Standard**: At least three independent verifiers on every route. One-of-N and two-of-N configurations are below baseline regardless of vendor; the record states whether the weak configuration is a vendor default or operator-chosen, since a known-weak default is a finding in both cases.
**Status**: Gap with action
**If Not Found — Gap Action**: Read the verifier set on chain for each route and collapse to independent operators. If a route resolves to one-of-N or two-of-N, record RF44 critical condition, name whether it is vendor-default or operator-chosen, and request the issuer's plan to reach three independent verifiers.
**Source / Precedent**: Kelp DAO, 18 Apr 2026: $292M drained via a forced-failover to a 1-of-1 LayerZero DVN — LayerZero shipped 1-of-1 as the default configuration for a large share of integrators.
**Criterion ID(s)**: 12.2, RF44
**Registered Sources (Fix 70)**: layerzero-scan-dvn (candidate)
