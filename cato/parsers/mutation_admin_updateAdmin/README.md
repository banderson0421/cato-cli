
## CATO-CLI - mutation.admin.updateAdmin:
[Click here](https://api.catonetworks.com/documentation/#mutation-updateAdmin) for documentation on this operation.

### Usage for mutation.admin.updateAdmin:

`cato mutation admin updateAdmin -h`

`cato mutation admin updateAdmin <accountID> <json>`

`cato mutation admin updateAdmin 12345 $(cat < updateAdmin.json)`

`cato mutation admin updateAdmin 12345 '{"adminID": "ID", "updateAdminInput": {"firstName": {"firstName": "String"}, "lastName": {"lastName": "String"}, "passwordNeverExpires": {"passwordNeverExpires": "Boolean"}, "mfaEnabled": {"mfaEnabled": "Boolean"}, "updateAdminRoleInput": {"role": {"id": {"id": "ID"}, "name": {"name": "String"}}, "allowedEntities": {"id": {"id": "ID"}, "name": {"name": "String"}, "type": {"type": "enum(EntityType)"}}, "allowedAccounts": {"allowedAccounts": ["ID"]}}}}'`

#### Operation Arguments for mutation.admin.updateAdmin ####
`adminID` [ID] - (required) N/A 
`updateAdminInput` [UpdateAdminInput] - (required) N/A 
`accountId` [ID] - (required) N/A 
