---
schema_version: 1
id: accountable-data-feeds
name: Accountable Data Verification Network
provider: Accountable Capital
url_base: https://accountable.capital
docs_url: https://accountable.capital/data-feeds
source_tier: FORMAL
purpose:
  - proof-of-reserves
  - reserve-vs-liability-verification
  - collateral-composition-monitoring
auth: unknown
access_mode: pointer-gated
freshness_typical: realtime
freshness_max_trusted: 24h
covers_chains:
  - ALL
covers_field_ids:
  - F-FIN-018       # primary: proof of reserves
  - F-COL-001       # secondary: collateral composition (per integrated issuer)
  - F-COL-002       # secondary: collateral concentration
covers_stablecoins_known:
  - aegis-yusd      # Aegis (BTC-collateralized): aegis.accountable.capital
  - yuzu-yzusd      # Yuzu Money: yuzu.accountable.capital
fallback_sources:
  - chainlink-por
  - issuer-direct-reserves
  - sec-edgar-attestation
status: candidate
added_in: v47
notes_url:
---

## What this source provides

Accountable operates a Data Verification Network for stablecoin
issuers. Each integrated issuer gets a dedicated subdomain dashboard
(e.g. `aegis.accountable.capital`, `yuzu.accountable.capital`) showing
continuous on-chain Proof of Reserves: reserves backing the
stablecoin, liabilities (outstanding tokens), and where applicable
yield performance verification. Marketing positions the network as
"continuous" or "real-time" verification with cryptographic backing.

Per-dashboard surfaces (observed via marketing/external references):
reserves composition, liabilities outstanding, yield performance
metrics, and collateral concentration breakdown.

## Source tier rationale

FORMAL, not ON-CHAIN. Although the verification mechanism includes
on-chain components, what VaultDiligence consumes is Accountable's
published dashboards, which are aggregations and visualisations on
top of the underlying on-chain state. The aggregation layer is
methodology-dependent and operated by Accountable, which is the
defining characteristic of FORMAL tier.

Accountable qualifies as FORMAL because:
- Named firm with attributable maintainer (Accountable Capital)
- Multiple production integrations with named stablecoin issuers
  (Aegis YUSD, Yuzu yzUSD, others likely)
- Public-facing dashboards with consistent format across issuers,
  suggesting documented methodology
- Records-of-record positioning — the dashboards are presented as
  authoritative reserves verification, not opinion

Tier could escalate to ON-CHAIN for specific evidence claims if
VaultDiligence reads the underlying smart contracts directly (rather
than the dashboard). In that case, the relevant entry is
`direct-rpc-read`, not this one.

## When to use it

Use Accountable as primary FORMAL source for proof-of-reserves
evidence ONLY when:

1. The stablecoin being analysed is on Accountable's integration list
   (currently confirmed: Aegis YUSD, Yuzu yzUSD; unconfirmed others
   likely exist — verify via the data-feeds page or Accountable's
   public communications before citing).

2. The evidence supports state=E for F-FIN-018 (proof of reserves)
   IF the dashboard is current (within freshness_max_trusted=24h)
   and the methodology is verifiable from the public dashboard.

3. The issuer has not also published direct on-chain attestation that
   is fresher than Accountable's data — in which case prefer the
   direct on-chain source.

## When NOT to use it

- For stablecoins not on Accountable's integration list. Citing
  Accountable for stablecoins they do not monitor is a category
  error.
- For PoR claims about issuers that publish their own attestation
  reports (Circle, Tether, etc.). Those issuers' attestation
  cadence and methodology are FORMAL on their own; Accountable
  would be redundant secondary at best.
- For evidence requiring methodology audit-trail. Accountable's
  full verification methodology is not public to the same standard
  as e.g. Pharos's versioned scoring docs. Citation suffices for
  "what Accountable publishes about reserves" but does not cover
  "how Accountable verifies reserves."
- For state=E claims about historical reserve states. Accountable's
  dashboards are forward-looking continuous verification; historical
  point-in-time queries may not be available.

## Authentication and rate limits

The public dashboards (e.g. `aegis.accountable.capital`,
`yuzu.accountable.capital`) are accessible without authentication for
reading. The bulk data-feeds API at
`https://accountable.capital/data-feeds` returned 403 to anonymous
access during registration check (2026-05-06), suggesting that
programmatic access requires authentication or partner onboarding.

For VaultDiligence's purposes:
- Per-issuer dashboard reads via WebFetch / Scrapling: no auth
  required, but client-side React rendering means the actual data
  values may not be accessible via HTML scrape — the values likely
  load via JS fetch from a backend API.
- For evidence citations, screenshot URLs or specific dashboard
  routes can be cited; values must be transcribed honestly.
- If programmatic API access is needed, contact Accountable for
  partner onboarding. Operator-side decision; not a VaultDiligence
  configuration question.

## Cross-references

- `chainlink-por` — alternative source for the same evidence type
  (proof-of-reserves), with longer track record and broader
  integration list. Generally prefer Chainlink PoR where both cover
  the same issuer.
- `issuer-direct-reserves` — generic category for issuer-published
  reserve disclosures. For issuers that publish their own, prefer
  that over an aggregator.
- `sec-edgar-attestation` — for regulated issuers, SEC-filed
  attestation reports are higher source-tier than Accountable
  (records of record, third-party signed).
- `pharos-stablecoin-grades` (Fix 70 candidate) — Pharos consumes
  Accountable's data as one of its inputs, so citing both is a
  near-circular reference; prefer the upstream (Accountable) for
  reserve-specific claims.

## Notes

Status `candidate` not `active` because:
1. The full integration list is not externally verifiable without
   accessing the (gated) data-feeds page.
2. Accountable is a young verification network (first observed
   integrations in late 2025); track record is short. Maintainer-
   abandonment risk is non-trivial.
3. The methodology page accessibility is uncertain — VaultDiligence
   prefers FORMAL sources whose methodology can be read without
   gating.

Reclassify to `active` when:
- The data-feeds page or an equivalent published list confirms the
  full integration set, AND
- At least 6 months of operational history without methodology
  changes (or with documented changelog), AND
- VaultDiligence has cited Accountable as primary source on at least one
  pack and that pack's verification step (A6) confirmed the citation
  held up.

Pharos Watch (separately registered as a candidate via Fix 70)
explicitly lists Accountable as one source group in its data
pipeline. So Pharos consuming Accountable does not change
Accountable's tier — the question is what VaultDiligence uses
Accountable for, not what other aggregators do.

Specific stablecoin coverage as of 2026-05-06:
- Aegis YUSD (BTC-collateralized stablecoin) at
  https://aegis.accountable.capital/
- Yuzu Money yzUSD (DeFi-yield-wrapped stablecoin) at
  https://yuzu.accountable.capital/
- Others likely; verify via public communications or the gated
  data-feeds page before citing for additional issuers.
