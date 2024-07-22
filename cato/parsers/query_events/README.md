
## CATO-CLI - query.events:
[Click here](https://api.catonetworks.com/documentation/#query-events) for documentation on this operation.

### Usage for query.events:

`cato query events -h`

`cato query events <accountID> <json>`

`cato query events 12345 $(cat < events.json)`

`cato query events 12345 '{"limit": "Int", "from": "Int", "timeFrame": "TimeFrame", "eventsMeasure": {"fieldName": {"fieldName": "enum(EventFieldName)"}, "aggType": {"aggType": "enum(AggregationType)"}, "trend": {"trend": "Boolean"}}, "eventsDimension": {"fieldName": {"fieldName": "enum(EventFieldName)"}}, "eventsFilter": {"fieldName": {"fieldName": "enum(EventFieldName)"}, "operator": {"operator": "enum(FilterOperator)"}, "values": {"values": ["String"]}}, "eventsSort": {"fieldName": {"fieldName": "enum(EventFieldName)"}, "order": {"order": "enum(DirectionEnum)"}}}'`

#### Operation Arguments for query.events ####
`limit` [Int] - (optional) N/A 
`from` [Int] - (optional) N/A 
`accountID` [ID] - (required) Account ID 
`timeFrame` [TimeFrame] - (required) N/A 
`eventsMeasure` [EventsMeasure[]] - (optional) N/A 
`eventsDimension` [EventsDimension[]] - (optional) N/A 
`eventsFilter` [EventsFilter[]] - (optional) N/A 
`eventsSort` [EventsSort[]] - (optional) N/A 
