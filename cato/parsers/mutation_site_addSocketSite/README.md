
## CATO-CLI - mutation.site.addSocketSite:
[Click here](https://api.catonetworks.com/documentation/#mutation-addSocketSite) for documentation on this operation.

### Usage for mutation.site.addSocketSite:

`cato mutation site addSocketSite -h`

`cato mutation site addSocketSite <accountID> <json>`

`cato mutation site addSocketSite 12345 $(cat < addSocketSite.json)`

`cato mutation site addSocketSite 12345 '{"addSocketSiteInput": {"name": {"name": "String"}, "connectionType": {"connectionType": "enum(SiteConnectionTypeEnum)"}, "siteType": {"siteType": "enum(SiteType)"}, "description": {"description": "String"}, "nativeNetworkRange": {"nativeNetworkRange": "IPSubnet"}, "translatedSubnet": {"translatedSubnet": "IPSubnet"}, "addSiteLocationInput": {"countryCode": {"countryCode": "String"}, "stateCode": {"stateCode": "String"}, "timezone": {"timezone": "String"}, "address": {"address": "String"}, "city": {"city": "String"}}}}'`

#### Operation Arguments for mutation.site.addSocketSite ####
`addSocketSiteInput` [AddSocketSiteInput] - (required) N/A 
`accountId` [ID] - (required) N/A 
