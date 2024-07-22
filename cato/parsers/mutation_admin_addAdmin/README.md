
## CATO-CLI - mutation.admin.addAdmin:
[Click here](https://api.catonetworks.com/documentation/#mutation-addAdmin) for documentation on this operation.

### Usage for mutation.admin.addAdmin:

`cato mutation admin addAdmin -h`

`cato mutation admin addAdmin <accountID> <json>`

`cato mutation admin addAdmin 12345 $(cat < addAdmin.json)`

`cato mutation admin addAdmin 12345 '{"addAdminInput": {"firstName": {"firstName": "String"}, "lastName": {"lastName": "String"}, "email": {"email": "String"}, "passwordNeverExpires": {"passwordNeverExpires": "Boolean"}, "mfaEnabled": {"mfaEnabled": "Boolean"}, "updateAdminRoleInput": {"role": {"id": {"id": "ID"}, "name": {"name": "String"}}, "allowedEntities": {"id": {"id": "ID"}, "name": {"name": "String"}, "type": {"type": "enum(EntityType)"}}, "allowedAccounts": {"allowedAccounts": ["ID"]}}}}'`

#### Operation Arguments for mutation.admin.addAdmin ####
`addAdminInput` [AddAdminInput] - (required) N/A 
`accountId` [ID] - (required) N/A 
