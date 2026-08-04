# F-CUS-001

**Field ID**: F-CUS-001
**Category**: Financial
**Sub-Category**: TradFi Custody
**Field Name**: Prime Broker Identity & SIPC Membership
**What to Collect / Question to Answer**: Name of prime broker holding underlying securities. Is it a SIPC member? SIPC covers up to $500K per account for securities. Confirm SIPC membership at sipc.org.
**Data Type**: Text / Y/N
**Vault Types**: Exposure in {private-credit,structured-credit} OR Structure=tranched OR (Exposure in {equities,corporate-fixed-income,sovereign-fixed-income} AND venue=tradfi-primary)  (derived from VT-N; original "Vault Types" value: VT-3,VT-4,VT-8)
**Collection Tier**: T1
**Primary Source**: SIPC member list: sipc.org/about-sipc/membership-list / FINRA BrokerCheck: brokercheck.finra.org
**Fallback Source**: Operator disclosure / prime brokerage agreement
**Pillar(s)**: P2
**D1**: N
**D2**: N
**D3**: Y
**D4**: Y
**D5**: N
**Required?**: Y
**If Not Found — Gap Action**: Search SIPC member list by prime broker name. Search FINRA BrokerCheck for regulatory standing. a preferred-equity-backed vault: the prime broker — confirm SIPC membership.
**Criterion ID(s)**: 2.11
**Registered Sources (Fix 70)**: finra-brokercheck, sipc-member-list (candidate)
