
## CATO-CLI - mutation.site.addIpsecIkeV2Site:
[Click here](https://api.catonetworks.com/documentation/#mutation-addIpsecIkeV2Site) for documentation on this operation.

### Usage for mutation.site.addIpsecIkeV2Site:

`cato mutation site addIpsecIkeV2Site -h`

`cato mutation site addIpsecIkeV2Site <accountID> <json>`

`cato mutation site addIpsecIkeV2Site 12345 $(cat < addIpsecIkeV2Site.json)`

`cato mutation site addIpsecIkeV2Site 12345 '{"addIpsecIkeV2SiteInput": {"name": {"name": "String"}, "siteType": {"siteType": "enum(SiteType)"}, "description": {"description": "String"}, "nativeNetworkRange": {"nativeNetworkRange": "IPSubnet"}, "addSiteLocationInput": {"countryCode": {"countryCode": "String"}, "stateCode": {"stateCode": "String"}, "timezone": {"timezone": "String"}, "address": {"address": "String"}, "city": {"city": "String"}}}}'`

#### Operation Arguments for mutation.site.addIpsecIkeV2Site ####
`addIpsecIkeV2SiteInput` [AddIpsecIkeV2SiteInput] - (required) N/A 
`accountId` [ID] - (required) N/A 
