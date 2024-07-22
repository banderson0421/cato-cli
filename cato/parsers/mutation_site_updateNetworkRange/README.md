
## CATO-CLI - mutation.site.updateNetworkRange:
[Click here](https://api.catonetworks.com/documentation/#mutation-updateNetworkRange) for documentation on this operation.

### Usage for mutation.site.updateNetworkRange:

`cato mutation site updateNetworkRange -h`

`cato mutation site updateNetworkRange <accountID> <json>`

`cato mutation site updateNetworkRange 12345 $(cat < updateNetworkRange.json)`

`cato mutation site updateNetworkRange 12345 '{"networkRangeId": "ID", "updateNetworkRangeInput": {"name": {"name": "String"}, "rangeType": {"rangeType": "enum(SubnetType)"}, "subnet": {"subnet": "IPSubnet"}, "translatedSubnet": {"translatedSubnet": "IPSubnet"}, "localIp": {"localIp": "IPAddress"}, "gateway": {"gateway": "IPAddress"}, "vlan": {"vlan": "Int"}, "azureFloatingIp": {"azureFloatingIp": "IPAddress"}, "networkDhcpSettingsInput": {"dhcpType": {"dhcpType": "enum(DhcpType)"}, "ipRange": {"ipRange": "IPRange"}, "relayGroupId": {"relayGroupId": "ID"}}}}'`

#### Operation Arguments for mutation.site.updateNetworkRange ####
`networkRangeId` [ID] - (required) N/A 
`updateNetworkRangeInput` [UpdateNetworkRangeInput] - (required) N/A 
`accountId` [ID] - (required) N/A 
