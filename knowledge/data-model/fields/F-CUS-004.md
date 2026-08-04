# F-CUS-004

**Field ID**: F-CUS-004
**Category**: Financial
**Sub-Category**: TradFi Custody
**Field Name**: Prime Broker Financial Health & Regulatory Standing
**What to Collect / Question to Answer**: Prime broker capital adequacy, recent audited financials, FINRA regulatory standing, any enforcement actions. the prime broker founded 2018 — limited stress-event track record.
**Data Type**: Text
**Vault Types**: Exposure in {private-credit,structured-credit} OR Structure=tranched OR (Exposure in {equities,corporate-fixed-income,sovereign-fixed-income} AND venue=tradfi-primary)  (derived from VT-N; original "Vault Types" value: VT-3,VT-4,VT-8)
**Collection Tier**: T1
**Primary Source**: FINRA BrokerCheck: brokercheck.finra.org / SEC EDGAR broker-dealer filings / prime broker annual report
**Fallback Source**: Operator disclosure
**Pillar(s)**: P2
**D1**: N
**D2**: N
**D3**: Y
**D4**: Y
**D5**: N
**Required?**: Y
**If Not Found — Gap Action**: Search FINRA BrokerCheck for prime broker. Check for any regulatory actions. Review most recent audited financials if available.
**Criterion ID(s)**: 2.11
**Registered Sources (Fix 70)**: finra-brokercheck
