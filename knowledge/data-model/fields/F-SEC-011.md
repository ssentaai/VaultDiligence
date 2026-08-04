# F-SEC-011

**Field ID**: F-SEC-011
**Category**: Security
**Sub-Category**: Infrastructure
**Field Name**: Cloud IAM Access Documentation
**What to Collect / Question to Answer**: Who has IAM/cloud access to key management environment? Is access documented? When was access last audited? Real-time monitoring of access logs?
**Data Type**: Text
**Vault Types**: ALL
**Collection Tier**: T4
**Primary Source**: Operator infrastructure documentation / SOC-2 report
**Fallback Source**: Pentest findings
**Pillar(s)**: P7
**D1**: Y
**D2**: Y
**D3**: Y
**D4**: Y
**D5**: Y
**Required?**: Y
**If Not Found — Gap Action**: Request cloud access documentation. If no documentation: flag. SOC-2 access control section if available.
**Criterion ID(s)**: 7.16
**Red Flag ID(s)**: RF41