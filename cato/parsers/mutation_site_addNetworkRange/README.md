
## CATO-CLI - mutation.site.addNetworkRange:
[Click here](https://api.catonetworks.com/documentation/#mutation-addNetworkRange) for documentation on this operation.

### Usage for mutation.site.addNetworkRange:

`cato mutation site addNetworkRange -h`

`cato mutation site addNetworkRange <accountID> <json>`

`cato mutation site addNetworkRange 12345 $(cat < addNetworkRange.json)`

`cato mutation site addNetworkRange 12345 '{"lanSocketInterfaceId": "ID", "addNetworkRangeInput": {"name": {"name": "String"}, "rangeType": {"rangeType": "enum(SubnetType)"}, "subnet": {"subnet": "IPSubnet"}, "translatedSubnet": {"translatedSubnet": "IPSubnet"}, "localIp": {"localIp": "IPAddress"}, "gateway": {"gateway": "IPAddress"}, "vlan": {"vlan": "Int"}, "azureFloatingIp": {"azureFloatingIp": "IPAddress"}, "networkDhcpSettingsInput": {"dhcpType": {"dhcpType": "enum(DhcpType)"}, "ipRange": {"ipRange": "IPRange"}, "relayGroupId": {"relayGroupId": "ID"}}}}'`

#### Operation Arguments for mutation.site.addNetworkRange ####
`lanSocketInterfaceId` [ID] - (required) N/A 
`addNetworkRangeInput` [AddNetworkRangeInput] - (required) N/A 
`accountId` [ID] - (required) N/A 
