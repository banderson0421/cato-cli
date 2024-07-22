
## CATO-CLI - mutation.site.updateIpsecIkeV2SiteTunnels:
[Click here](https://api.catonetworks.com/documentation/#mutation-updateIpsecIkeV2SiteTunnels) for documentation on this operation.

### Usage for mutation.site.updateIpsecIkeV2SiteTunnels:

`cato mutation site updateIpsecIkeV2SiteTunnels -h`

`cato mutation site updateIpsecIkeV2SiteTunnels <accountID> <json>`

`cato mutation site updateIpsecIkeV2SiteTunnels 12345 $(cat < updateIpsecIkeV2SiteTunnels.json)`

`cato mutation site updateIpsecIkeV2SiteTunnels 12345 '{"siteId": "ID", "updateIpsecIkeV2SiteTunnelsInput": {"updateIpsecIkeV2TunnelsInput": {"destinationType": {"destinationType": "enum(DestinationType)"}, "publicCatoIpId": {"publicCatoIpId": "ID"}, "popLocationId": {"popLocationId": "ID"}, "tunnels": {"tunnelId": {"tunnelId": "enum(IPSecV2InterfaceId)"}, "publicSiteIp": {"publicSiteIp": "IPAddress"}, "privateCatoIp": {"privateCatoIp": "IPAddress"}, "privateSiteIp": {"privateSiteIp": "IPAddress"}, "lastMileBw": {"downstream": {"downstream": "Int"}, "upstream": {"upstream": "Int"}, "downstreamMbpsPrecision": {"downstreamMbpsPrecision": "Float"}, "upstreamMbpsPrecision": {"upstreamMbpsPrecision": "Float"}}, "psk": {"psk": "String"}}}}}'`

#### Operation Arguments for mutation.site.updateIpsecIkeV2SiteTunnels ####
`siteId` [ID] - (required) N/A 
`updateIpsecIkeV2SiteTunnelsInput` [UpdateIpsecIkeV2SiteTunnelsInput] - (required) N/A 
`accountId` [ID] - (required) N/A 
