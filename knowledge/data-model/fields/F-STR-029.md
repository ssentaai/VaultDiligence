# F-STR-029

**Field ID**: F-STR-029
**Category**: Strategy Risk
**Sub-Category**: LP/AMM — Pair Composition
**Field Name**: Pool Pair Composition & Correlation / Depeg Sensitivity
**What to Collect / Question to Answer**: What are the pooled assets and their historical price correlation, and how sensitive is IL to a correlation breakdown or depeg? For pegged or correlated pairs (stable-stable, LST-ETH, wrapped-native), state the largest historical divergence of this pair (or comparable pairs), the one-sided conversion the vault would suffer at that divergence, and whether the position would be left holding the impaired asset.
**Data Type**: Structured (pooled assets, pair correlation + window, largest observed divergence/depeg, resulting one-sided IL)
**Vault Types**: Strategy = LP/AMM-provision
**Collection Tier**: T1 (price-series correlation) + T3 (asset classification)
**Pillar(s)**: P4 (Collateral) primary; cross P6 (Strategy Integrity) — propose; operator confirms
**Primary Source**: Reference price series for the pooled assets (correlation, historical divergence); asset classification per F-FIN-030/031
**Fallback Source**: Documented depeg/decorrelation incidents for the pair or comparable pairs; operator disclosure
**Evidence Pathway**: Inspection-validatable — pair correlation and the largest historical divergence are computed from price series; the resulting one-sided IL follows from the AMM invariant at that divergence.
**Institutional Standard**: A well-run vault records the pooled pair's correlation regime and its worst historical divergence, and states the one-sided IL and residual-asset exposure a correlation break would produce. Treating a pegged/correlated pair as divergence-free without stating the depeg tail is the gap.
**Status**: Gap with action
**If Not Found — Gap Action**: If price series are available, compute correlation and worst divergence and classify E. If assets are named but no divergence analysis is done, classify E(P). If the pair's history is not analysable, classify G3. Cross-reference F-FIN-030/031 (collateral list/classification) — the pair-correlation and depeg-sensitivity angle is the strategy-specific delta those fields lack.
**Source / Precedent**: Constant-function AMM IL-vs-divergence relationship (IL scales with the ratio of relative price change). Depeg/decorrelation precedents (e.g. stablecoin depegs; LST discount episodes) are illustrative anchors, not a single canonical source — flagged as illustrative; the underlying assets should be verified against live data at assessment.
**Criterion ID(s)**: propose at ratification (adjacent to 4.1)
