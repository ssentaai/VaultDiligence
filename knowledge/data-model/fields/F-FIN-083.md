# F-FIN-083

**Field ID**: F-FIN-083
**Category**: Financial
**Sub-Category**: Counterparty Exposure
**Field Name**: Material Counterparty Register with Sized Exposure
**What to Collect / Question to Answer**: What are all the material counterparties on which the proper functioning of the vault depends, and what is the size of the risk exposure to each, expressed at the allocator's position size?
**Data Type**: Table (counterparty name -> role -> sized exposure at position size)
**Vault Types**: ALL
**Collection Tier**: T3
**Pillar(s)**: P9
**Primary Source**: Operator DDQ response listing material counterparties with sized exposures
**Fallback Source**: On-chain counterparty mapping (custodian, prime broker, bridge, market maker addresses) plus service-provider disclosures, reconciled into a sized register
**Evidence Pathway**: Third-party-evidenced: obtain the operator's enumerated counterparty list and size each exposure from disclosed balances or on-chain holdings; where the operator does not size them, reconstruct sizing from on-chain and document the basis.
**Institutional Standard**: Every counterparty whose failure would impair vault function is named, its role stated, and the dollar exposure to it sized at the allocator's position size; the register is complete across custody, trading, settlement, bridging, and oracle counterparties rather than limited to trading venues.
**Status**: Gap with action
**If Not Found — Gap Action**: Request the complete material-counterparty register with sized exposures; if the operator lists names without sizing, size each from on-chain or disclosed balances and label any irreducible gaps G2 naming the counterparty whose exposure could not be sized. A sized counterparty map is mandatory in every D2.
**Source / Precedent**: Steakhouse Financial stablecoin-issuer DDQ v1.0, section 3.6: 'List all of the material counterparties that a proper functioning of the stablecoin relies on and provide information on the size of the respective risk exposure.'
**Criterion ID(s)**: 9.10
