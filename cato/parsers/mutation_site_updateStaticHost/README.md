
## CATO-CLI - mutation.site.updateStaticHost:
[Click here](https://api.catonetworks.com/documentation/#mutation-updateStaticHost) for documentation on this operation.

### Usage for mutation.site.updateStaticHost:

`cato mutation site updateStaticHost -h`

`cato mutation site updateStaticHost <accountID> <json>`

`cato mutation site updateStaticHost 12345 $(cat < updateStaticHost.json)`

`cato mutation site updateStaticHost 12345 '{"hostId": "ID", "updateStaticHostInput": {"ip": {"ip": "IPAddress"}, "macAddress": {"macAddress": "String"}, "name": {"name": "String"}}}'`

#### Operation Arguments for mutation.site.updateStaticHost ####
`accountId` [ID] - (required) N/A 
`hostId` [ID] - (required) N/A 
`updateStaticHostInput` [UpdateStaticHostInput] - (required) N/A 
