

---

## Yield Dependency Chain (required diagram for VT-8)

For any VT-8 vault, the investigation must map the complete yield
dependency chain as a directed graph. Each node is a counterparty or
mechanism. Each edge is confirmed or gap-classified.

Standard VT-8 chain:

  Depositor
    → Vault contract (ERC-4626 or equivalent)
    → Tokenisation platform / custody partner
    → Underlying instrument (preferred equity, bond, treasury, etc.)
    → Issuer (corporate or sovereign)
    → Collateral (Bitcoin, real estate, receivables, etc.)
    → Macro anchor (SOFR, Fed funds rate, BTC price, etc.)

At each node the investigation must confirm:
  1. Named entity (not assumed)
  2. Legal relationship to adjacent nodes
  3. Failure mode if this node breaks
  4. Evidence state for each of the above

For a preferred-equity-backed vault specifically:
  Depositor → a preferred-equity-backed token vault → a listed preferred instrument custody (the execution broker + Securitize + the prime broker)
  → a listed preferred instrument preferred equity (a corporate issuer.) → Bitcoin collateral
  → SOFR + credit spread (yield anchor)

Failure modes per node:
  a preferred-equity-backed token vault: redemption queue if utilisation > threshold
  a listed preferred instrument custody: counterparty concentration — 3 named entities
  a listed preferred instrument preferred equity: dividend deferral at the issuer's discretion
  Bitcoin collateral: LTV breach triggers vault rebalancing to Treasuries
  SOFR anchor: rate cut compresses yield floor but not credit spread

This diagram renders in the web output as a vertical flow chart
with evidence state chips at each node and failure mode tooltip on hover.
