
## CATO-CLI - query.appStats:
[Click here](https://api.catonetworks.com/documentation/#query-appStats) for documentation on this operation.

### Usage for query.appStats:

`cato query appStats -h`

`cato query appStats <accountID> <json>`

`cato query appStats 12345 $(cat < appStats.json)`

`cato query appStats 12345 '{"limit": "Int", "from": "Int", "timeFrame": "TimeFrame", "measure": {"fieldName": {"fieldName": "enum(AppStatsFieldName)"}, "aggType": {"aggType": "enum(AggregationType)"}, "trend": {"trend": "Boolean"}}, "dimension": {"fieldName": {"fieldName": "enum(AppStatsFieldName)"}}, "appStatsFilter": {"fieldName": {"fieldName": "enum(AppStatsFieldName)"}, "operator": {"operator": "enum(FilterOperator)"}, "values": {"values": ["String"]}}, "appStatsSort": {"fieldName": {"fieldName": "enum(AppStatsFieldName)"}, "order": {"order": "enum(DirectionEnum)"}}}'`

#### Operation Arguments for query.appStats ####
`limit` [Int] - (optional) N/A 
`from` [Int] - (optional) N/A 
`accountID` [ID] - (required) Account ID 
`timeFrame` [TimeFrame] - (required) N/A 
`measure` [Measure[]] - (optional) N/A 
`dimension` [Dimension[]] - (optional) N/A 
`appStatsFilter` [AppStatsFilter[]] - (optional) N/A 
`appStatsSort` [AppStatsSort[]] - (optional) N/A 
