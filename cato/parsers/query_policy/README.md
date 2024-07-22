
## CATO-CLI - query.policy:
[Click here](https://api.catonetworks.com/documentation/#query-policy) for documentation on this operation.

### Usage for query.policy:

`cato query policy -h`

`cato query policy <accountID> <json>`

`cato query policy 12345 $(cat < policy.json)`

`cato query policy 12345 '{"internetFirewallPolicyInput": {"policyRevisionInput": {"type": {"type": "enum(PolicyRevisionType)"}, "id": {"id": "ID"}}}}'`

#### Operation Arguments for query.policy ####
`internetFirewallPolicyInput` [InternetFirewallPolicyInput] - (optional) N/A 
`accountId` [ID] - (required) N/A 
