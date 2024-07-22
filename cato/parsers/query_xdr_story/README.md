
## CATO-CLI - query.xdr.story:
[Click here](https://api.catonetworks.com/documentation/#query-story) for documentation on this operation.

### Usage for query.xdr.story:

`cato query xdr story -h`

`cato query xdr story <accountID> <json>`

`cato query xdr story 12345 $(cat < story.json)`

`cato query xdr story 12345 '{"perSecond": "Boolean", "storyId": "ID", "producer": "enum(StoryProducerEnum)", "incidentId": "ID"}'`

#### Operation Arguments for query.xdr.story ####
`perSecond` [Boolean] - (optional) whether to normalize the data into per second (i.e. divide by granularity) 
`storyId` [ID] - (optional) N/A 
`producer` [StoryProducerEnum] - (optional) N/A Default Value: ['AnomalyStats', 'AnomalyEvents', 'ThreatHunt', 'ThreatPrevention', 'NetworkMonitor', 'NetworkXDR', 'MicrosoftEndpointDefender', 'CatoEndpointAlert']
`incidentId` [ID] - (optional) N/A 
`accountID` [ID] - (required) N/A 
