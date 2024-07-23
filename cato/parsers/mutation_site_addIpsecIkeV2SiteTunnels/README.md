
## CATO-CLI - mutation.site.addIpsecIkeV2SiteTunnels:
[Click here](https://api.catonetworks.com/documentation/#mutation-addIpsecIkeV2SiteTunnels) for documentation on this operation.

### Usage for mutation.site.addIpsecIkeV2SiteTunnels:

`cato mutation site addIpsecIkeV2SiteTunnels -h`

`cato mutation site addIpsecIkeV2SiteTunnels <accountID> <json>`

`cato mutation site addIpsecIkeV2SiteTunnels 12345 $(cat < addIpsecIkeV2SiteTunnels.json)`

`cato mutation site addIpsecIkeV2SiteTunnels 12345 '{"addIpsecIkeV2SiteTunnelsInput": {"addIpsecIkeV2TunnelsInput": {"destinationType": {"destinationType": "enum(DestinationType)"}, "popLocationId": {"popLocationId": "ID"}, "publicCatoIpId": {"publicCatoIpId": "ID"}, "tunnels": {"lastMileBw": {"downstream": {"downstream": "Int"}, "downstreamMbpsPrecision": {"downstreamMbpsPrecision": "Float"}, "upstream": {"upstream": "Int"}, "upstreamMbpsPrecision": {"upstreamMbpsPrecision": "Float"}}, "privateCatoIp": {"privateCatoIp": "IPAddress"}, "privateSiteIp": {"privateSiteIp": "IPAddress"}, "psk": {"psk": "String"}, "publicSiteIp": {"publicSiteIp": "IPAddress"}}}}, "siteId": "ID"}'`

#### Operation Arguments for mutation.site.addIpsecIkeV2SiteTunnels ####
`accountId` [ID] - (required) N/A 
`addIpsecIkeV2SiteTunnelsInput` [AddIpsecIkeV2SiteTunnelsInput] - (required) N/A 
`siteId` [ID] - (required) N/A 
