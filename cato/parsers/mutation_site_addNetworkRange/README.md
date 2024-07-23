
## CATO-CLI - mutation.site.addNetworkRange:
[Click here](https://api.catonetworks.com/documentation/#mutation-addNetworkRange) for documentation on this operation.

### Usage for mutation.site.addNetworkRange:

`cato mutation site addNetworkRange -h`

`cato mutation site addNetworkRange <accountID> <json>`

`cato mutation site addNetworkRange 12345 $(cat < addNetworkRange.json)`

`cato mutation site addNetworkRange 12345 '{"addNetworkRangeInput": {"azureFloatingIp": {"azureFloatingIp": "IPAddress"}, "gateway": {"gateway": "IPAddress"}, "localIp": {"localIp": "IPAddress"}, "name": {"name": "String"}, "networkDhcpSettingsInput": {"dhcpType": {"dhcpType": "enum(DhcpType)"}, "ipRange": {"ipRange": "IPRange"}, "relayGroupId": {"relayGroupId": "ID"}}, "rangeType": {"rangeType": "enum(SubnetType)"}, "subnet": {"subnet": "IPSubnet"}, "translatedSubnet": {"translatedSubnet": "IPSubnet"}, "vlan": {"vlan": "Int"}}, "lanSocketInterfaceId": "ID"}'`

#### Operation Arguments for mutation.site.addNetworkRange ####
`accountId` [ID] - (required) N/A 
`addNetworkRangeInput` [AddNetworkRangeInput] - (required) N/A 
`lanSocketInterfaceId` [ID] - (required) N/A 
