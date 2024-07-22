
## CATO-CLI - query.auditFeed:
[Click here](https://api.catonetworks.com/documentation/#query-auditFeed) for documentation on this operation.

### Usage for query.auditFeed:

`cato query auditFeed -h`

`cato query auditFeed <accountID> <json>`

`cato query auditFeed 12345 $(cat < auditFeed.json)`

`cato query auditFeed 12345 '{"fieldNames": "enum(AuditFieldName)", "accountIDs": ["ID"], "timeFrame": "TimeFrame", "auditFieldFilterInput": {"fieldNameInput": {"EventFieldName": {"EventFieldName": "enum(EventFieldName)"}, "AuditFieldName": {"AuditFieldName": "enum(AuditFieldName)"}}, "operator": {"operator": "enum(ElasticOperator)"}, "values": {"values": ["String"]}}, "marker": "String"}'`

#### Operation Arguments for query.auditFeed ####
`fieldNames` [AuditFieldName[]] - (optional) N/A Default Value: ['admin', 'apiKey', 'model_name', 'admin_id', 'module', 'audit_creation_type', 'insertion_date', 'change_type', 'creation_date', 'model_type', 'account', 'account_id']
`accountIDs` [ID[]] - (optional) List of Unique Account Identifiers. 
`timeFrame` [TimeFrame] - (required) N/A 
`auditFieldFilterInput` [AuditFieldFilterInput[]] - (optional) N/A 
`marker` [String] - (optional) Marker to use to get results from 
