
## CATO-CLI - mutation.site.updateSocketInterface:
[Click here](https://api.catonetworks.com/documentation/#mutation-updateSocketInterface) for documentation on this operation.

### Usage for mutation.site.updateSocketInterface:

`cato mutation site updateSocketInterface -h`

`cato mutation site updateSocketInterface <accountID> <json>`

`cato mutation site updateSocketInterface 12345 $(cat < updateSocketInterface.json)`

`cato mutation site updateSocketInterface 12345 '{"siteId": "ID", "socketInterfaceId": "enum(SocketInterfaceIDEnum)", "updateSocketInterfaceInput": {"destType": {"destType": "enum(SocketInterfaceDestType)"}, "name": {"name": "String"}, "socketInterfaceLanInput": {"subnet": {"subnet": "IPSubnet"}, "translatedSubnet": {"translatedSubnet": "IPSubnet"}, "localIp": {"localIp": "IPAddress"}}, "socketInterfaceBandwidthInput": {"upstreamBandwidth": {"upstreamBandwidth": "Int"}, "downstreamBandwidth": {"downstreamBandwidth": "Int"}}, "socketInterfaceWanInput": {"role": {"role": "enum(SocketInterfaceRole)"}, "precedence": {"precedence": "enum(SocketInterfacePrecedenceEnum)"}}, "socketInterfaceOffCloudInput": {"enabled": {"enabled": "Boolean"}, "publicIp": {"publicIp": "IPAddress"}, "publicStaticPort": {"publicStaticPort": "Int"}}, "socketInterfaceAltWanInput": {"privateInterfaceIp": {"privateInterfaceIp": "IPAddress"}, "privateNetwork": {"privateNetwork": "IPSubnet"}, "privateGatewayIp": {"privateGatewayIp": "IPAddress"}, "privateVlanTag": {"privateVlanTag": "Int"}, "publicInterfaceIp": {"publicInterfaceIp": "IPAddress"}, "publicNetwork": {"publicNetwork": "IPSubnet"}, "publicGatewayIp": {"publicGatewayIp": "IPAddress"}, "publicVlanTag": {"publicVlanTag": "Int"}}, "socketInterfaceLagInput": {"minLinks": {"minLinks": "Int"}}, "socketInterfaceVrrpInput": {"vrrpType": {"vrrpType": "enum(VrrpType)"}}}}'`

#### Operation Arguments for mutation.site.updateSocketInterface ####
`siteId` [ID] - (required) N/A 
`socketInterfaceId` [SocketInterfaceIDEnum] - (required) N/A Default Value: ['LAN1', 'LAN2', 'WAN1', 'WAN2', 'USB1', 'USB2', 'INT_1', 'INT_2', 'INT_3', 'INT_4', 'INT_5', 'INT_6', 'INT_7', 'INT_8', 'INT_9', 'INT_10', 'INT_11', 'INT_12', 'WLAN', 'LTE']
`updateSocketInterfaceInput` [UpdateSocketInterfaceInput] - (required) N/A 
`accountId` [ID] - (required) N/A 
