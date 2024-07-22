
## CATO-CLI - query.appStatsTimeSeries:
[Click here](https://api.catonetworks.com/documentation/#query-appStatsTimeSeries) for documentation on this operation.

### Usage for query.appStatsTimeSeries:

`cato query appStatsTimeSeries -h`

`cato query appStatsTimeSeries <accountID> <json>`

`cato query appStatsTimeSeries 12345 $(cat < appStatsTimeSeries.json)`

`cato query appStatsTimeSeries 12345 '{"perSecond": "Boolean", "withMissingData": "Boolean", "buckets": "Int", "timeFrame": "TimeFrame", "measure": {"fieldName": {"fieldName": "enum(AppStatsFieldName)"}, "aggType": {"aggType": "enum(AggregationType)"}, "trend": {"trend": "Boolean"}}, "dimension": {"fieldName": {"fieldName": "enum(AppStatsFieldName)"}}, "appStatsFilter": {"fieldName": {"fieldName": "enum(AppStatsFieldName)"}, "operator": {"operator": "enum(FilterOperator)"}, "values": {"values": ["String"]}}}'`

#### Operation Arguments for query.appStatsTimeSeries ####
`perSecond` [Boolean] - (optional) whether to normalize the data into per second (i.e. divide by granularity) 
`withMissingData` [Boolean] - (optional) If false, the data field will be set to '0' for buckets with no reported data. Otherwise it will be set to -1 
`buckets` [Int] - (required) N/A 
`accountID` [ID] - (required) Account ID 
`timeFrame` [TimeFrame] - (required) N/A 
`measure` [Measure[]] - (optional) N/A 
`dimension` [Dimension[]] - (optional) N/A 
`appStatsFilter` [AppStatsFilter[]] - (optional) N/A 
