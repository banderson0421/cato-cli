
## CATO-CLI - query.xdr.stories:
[Click here](https://api.catonetworks.com/documentation/#query-stories) for documentation on this operation.

### Usage for query.xdr.stories:

`cato query xdr stories -h`

`cato query xdr stories <accountID> <json>`

`cato query xdr stories 12345 $(cat < stories.json)`

`cato query xdr stories 12345 '{"perSecond": "Boolean", "storyInput": {"pagingInput": {"limit": {"limit": "Int"}, "from": {"from": "Int"}}, "storySortInput": {"fieldName": {"fieldName": "enum(StorySortFieldName)"}, "order": {"order": "enum(SortDirectionEnum)"}}, "storyFilterInput": {"timeFrame": {"time": {"time": "TimeFrame"}, "timeFrameModifier": {"timeFrameModifier": "enum(TimeFrameModifier)"}}, "producer": {"in": {"in": "enum(StoryProducerEnum)"}, "not_in": {"not_in": "enum(StoryProducerEnum)"}}, "status": {"in": {"in": "enum(StoryStatusEnum)"}, "not_in": {"not_in": "enum(StoryStatusEnum)"}}, "criticality": {"gt": {"gt": "Int"}, "gte": {"gte": "Int"}, "lt": {"lt": "Int"}, "lte": {"lte": "Int"}, "eq": {"eq": "Int"}, "in": {"in": ["Int"]}, "not_in": {"not_in": ["Int"]}}, "source": {"in": {"in": ["String"]}, "not_in": {"not_in": ["String"]}, "contains": {"contains": "String"}}, "severity": {"in": {"in": "enum(SeverityEnum)"}, "not_in": {"not_in": "enum(SeverityEnum)"}}, "incidentId": {"in": {"in": ["String"]}, "not_in": {"not_in": ["String"]}, "contains": {"contains": "String"}}, "ioa": {"in": {"in": ["String"]}, "not_in": {"not_in": ["String"]}, "contains": {"contains": "String"}}, "accountId": {"in": {"in": ["ID"]}, "not_in": {"not_in": ["ID"]}}, "storyId": {"in": {"in": ["ID"]}, "not_in": {"not_in": ["ID"]}}, "queryName": {"in": {"in": ["String"]}, "not_in": {"not_in": ["String"]}, "contains": {"contains": "String"}}, "verdict": {"in": {"in": "enum(StoryVerdictEnum)"}, "not_in": {"not_in": "enum(StoryVerdictEnum)"}}, "engineType": {"in": {"in": "enum(StoryEngineTypeEnum)"}, "not_in": {"not_in": "enum(StoryEngineTypeEnum)"}}, "vendor": {"in": {"in": "enum(VendorEnum)"}, "not_in": {"not_in": "enum(VendorEnum)"}}, "sourceIp": {"in": {"in": ["String"]}, "not_in": {"not_in": ["String"]}, "contains": {"contains": "String"}}, "muted": {"is": {"is": "String"}}}}}'`

#### Operation Arguments for query.xdr.stories ####
`perSecond` [Boolean] - (optional) whether to normalize the data into per second (i.e. divide by granularity) 
`storyInput` [StoryInput] - (required) N/A 
`accountID` [ID] - (required) N/A 
