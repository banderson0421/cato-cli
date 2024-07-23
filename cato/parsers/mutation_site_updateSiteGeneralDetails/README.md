
## CATO-CLI - mutation.site.updateSiteGeneralDetails:
[Click here](https://api.catonetworks.com/documentation/#mutation-updateSiteGeneralDetails) for documentation on this operation.

### Usage for mutation.site.updateSiteGeneralDetails:

`cato mutation site updateSiteGeneralDetails -h`

`cato mutation site updateSiteGeneralDetails <accountID> <json>`

`cato mutation site updateSiteGeneralDetails 12345 $(cat < updateSiteGeneralDetails.json)`

`cato mutation site updateSiteGeneralDetails 12345 '{"siteId": "ID", "updateSiteGeneralDetailsInput": {"description": {"description": "String"}, "name": {"name": "String"}, "siteType": {"siteType": "enum(SiteType)"}, "updateSiteLocationInput": {"address": {"address": "String"}, "countryCode": {"countryCode": "String"}, "stateCode": {"stateCode": "String"}, "timezone": {"timezone": "String"}}}}'`

#### Operation Arguments for mutation.site.updateSiteGeneralDetails ####
`accountId` [ID] - (required) N/A 
`siteId` [ID] - (required) N/A 
`updateSiteGeneralDetailsInput` [UpdateSiteGeneralDetailsInput] - (required) N/A 
