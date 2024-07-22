
## CATO-CLI - query.entityLookup:
[Click here](https://api.catonetworks.com/documentation/#query-entityLookup) for documentation on this operation.

### Usage for query.entityLookup:

`cato query entityLookup -h`

`cato query entityLookup <accountID> <json>`

`cato query entityLookup 12345 $(cat < entityLookup.json)`

`cato query entityLookup 12345 '{"type": "enum(EntityType)", "limit": "Int", "from": "Int", "entityInput": {"id": {"id": "ID"}, "name": {"name": "String"}, "type": {"type": "enum(EntityType)"}}, "search": "String", "entityIDs": ["ID"], "sortInput": {"field": {"field": "String"}, "order": {"order": "enum(DirectionInput)"}}, "lookupFilterInput": {"filter": {"filter": "enum(LookupFilterType)"}, "value": {"value": "String"}}, "helperFields": ["String"]}'`

#### Operation Arguments for query.entityLookup ####
`accountID` [ID] - (required) The account ID (or 0 for non-authenticated requests) 
`type` [EntityType] - (required) Type of entity to lookup for Default Value: ['country', 'countryState', 'timezone', 'site', 'host', 'any', 'account', 'networkInterface', 'vpnUser', 'location', 'admin', 'localRouting', 'lanFirewall', 'allocatedIP', 'siteRange', 'simpleService', 'availableSiteUsage', 'availablePooledUsage', 'dhcpRelayGroup', 'portProtocol', 'city', 'groupSubscription', 'mailingListSubscription', 'webhookSubscription']
`limit` [Int] - (optional) Sets the maximum number of items to retrieve 
`from` [Int] - (optional) Sets the offset number of items (for paging) 
`entityInput` [EntityInput] - (optional) Return items under a parent entity (can be site, vpn user, etc),
used to filter for networks that belong to a specific site for example 
`search` [String] - (optional) Adds additional search parameters for the lookup. Available options:
country lookup: "removeExcluded" to return only allowed countries
countryState lookup: country code ("US", "CN", etc) to get country's states 
`entityIDs` [ID[]] - (optional) Adds additional search criteria to fetch by the selected list of entity IDs. This option is not
universally available, and may not be applicable specific Entity types. If used on non applicable entity
type, an error will be generated. 
`sortInput` [SortInput[]] - (optional) Adds additional sort criteria(s) for the lookup.
This option is not universally available, and may not be applicable specific Entity types. 
`lookupFilterInput` [LookupFilterInput[]] - (optional) Custom filters for entityLookup 
`helperFields` [String[]] - (optional) Additional helper fields 
