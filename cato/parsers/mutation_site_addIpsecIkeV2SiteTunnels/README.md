
## CATO-CLI - mutation.site.addIpsecIkeV2SiteTunnels:
[Click here](https://api.catonetworks.com/documentation/#mutation-addIpsecIkeV2SiteTunnels) for documentation on this operation.

### Usage for mutation.site.addIpsecIkeV2SiteTunnels:

`cato mutation site addIpsecIkeV2SiteTunnels -h`

`cato mutation site addIpsecIkeV2SiteTunnels <accountID> <json>`

`cato mutation site addIpsecIkeV2SiteTunnels 12345 $(cat < addIpsecIkeV2SiteTunnels.json)`

`cato mutation site addIpsecIkeV2SiteTunnels 12345 '{"siteId": "ID", "addIpsecIkeV2SiteTunnelsInput": {"addIpsecIkeV2TunnelsInput": {"destinationType": {"destinationType": "enum(DestinationType)"}, "publicCatoIpId": {"publicCatoIpId": "ID"}, "popLocationId": {"popLocationId": "ID"}, "tunnels": {"publicSiteIp": {"publicSiteIp": "IPAddress"}, "privateCatoIp": {"privateCatoIp": "IPAddress"}, "privateSiteIp": {"privateSiteIp": "IPAddress"}, "lastMileBw": {"downstream": {"downstream": "Int"}, "upstream": {"upstream": "Int"}, "downstreamMbpsPrecision": {"downstreamMbpsPrecision": "Float"}, "upstreamMbpsPrecision": {"upstreamMbpsPrecision": "Float"}}, "psk": {"psk": "String"}}}}}'`

#### Operation Arguments for mutation.site.addIpsecIkeV2SiteTunnels ####
`siteId` [ID] - (required) N/A 
`addIpsecIkeV2SiteTunnelsInput` [AddIpsecIkeV2SiteTunnelsInput] - (required) N/A 
`accountId` [ID] - (required) N/A 
