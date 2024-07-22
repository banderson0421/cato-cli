
## CATO-CLI - mutation.policy.internetFirewall.createPolicyRevision:
[Click here](https://api.catonetworks.com/documentation/#mutation-createPolicyRevision) for documentation on this operation.

### Usage for mutation.policy.internetFirewall.createPolicyRevision:

`cato mutation policy internetFirewall createPolicyRevision -h`

`cato mutation policy internetFirewall createPolicyRevision <accountID> <json>`

`cato mutation policy internetFirewall createPolicyRevision 12345 $(cat < createPolicyRevision.json)`

`cato mutation policy internetFirewall createPolicyRevision 12345 '{"policyCreateRevisionInput": {"name": {"name": "String"}, "description": {"description": "String"}}, "internetFirewallPolicyMutationInput": {"policyMutationRevisionInput": {"id": {"id": "ID"}}}}'`

#### Operation Arguments for mutation.policy.internetFirewall.createPolicyRevision ####
`policyCreateRevisionInput` [PolicyCreateRevisionInput] - (required) N/A 
`internetFirewallPolicyMutationInput` [InternetFirewallPolicyMutationInput] - (optional) N/A 
`accountId` [ID] - (required) N/A 
