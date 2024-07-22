
## CATO-CLI - query.eventsTimeSeries:
[Click here](https://api.catonetworks.com/documentation/#query-eventsTimeSeries) for documentation on this operation.

### Usage for query.eventsTimeSeries:

`cato query eventsTimeSeries -h`

`cato query eventsTimeSeries <accountID> <json>`

`cato query eventsTimeSeries 12345 $(cat < eventsTimeSeries.json)`

`cato query eventsTimeSeries 12345 '{"perSecond": "Boolean", "withMissingData": "Boolean", "buckets": "Int", "timeFrame": "TimeFrame", "eventsMeasure": {"fieldName": {"fieldName": "enum(EventFieldName)"}, "aggType": {"aggType": "enum(AggregationType)"}, "trend": {"trend": "Boolean"}}, "eventsDimension": {"fieldName": {"fieldName": "enum(EventFieldName)"}}, "eventsFilter": {"fieldName": {"fieldName": "enum(EventFieldName)"}, "operator": {"operator": "enum(FilterOperator)"}, "values": {"values": ["String"]}}}'`

#### Operation Arguments for query.eventsTimeSeries ####
`perSecond` [Boolean] - (optional) whether to normalize the data into per second (i.e. divide by granularity) 
`withMissingData` [Boolean] - (optional) If false, the data field will be set to '0' for buckets with no reported data. Otherwise it will be set to -1 
`buckets` [Int] - (required) N/A 
`accountID` [ID] - (required) Account ID 
`timeFrame` [TimeFrame] - (required) N/A 
`eventsMeasure` [EventsMeasure[]] - (optional) N/A 
`eventsDimension` [EventsDimension[]] - (optional) N/A 
`eventsFilter` [EventsFilter[]] - (optional) N/A 
