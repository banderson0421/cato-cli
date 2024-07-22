
## CATO-CLI - mutation.site.updateSiteGeneralDetails:
[Click here](https://api.catonetworks.com/documentation/#mutation-updateSiteGeneralDetails) for documentation on this operation.

### Usage for mutation.site.updateSiteGeneralDetails:

`cato mutation site updateSiteGeneralDetails -h`

`cato mutation site updateSiteGeneralDetails <accountID> <json>`

`cato mutation site updateSiteGeneralDetails 12345 $(cat < updateSiteGeneralDetails.json)`

`cato mutation site updateSiteGeneralDetails 12345 '{"siteId": "ID", "updateSiteGeneralDetailsInput": {"name": {"name": "String"}, "siteType": {"siteType": "enum(SiteType)"}, "description": {"description": "String"}, "updateSiteLocationInput": {"countryCode": {"countryCode": "String"}, "stateCode": {"stateCode": "String"}, "timezone": {"timezone": "String"}, "address": {"address": "String"}}}}'`

#### Operation Arguments for mutation.site.updateSiteGeneralDetails ####
`siteId` [ID] - (required) N/A 
`updateSiteGeneralDetailsInput` [UpdateSiteGeneralDetailsInput] - (required) N/A 
`accountId` [ID] - (required) N/A 
