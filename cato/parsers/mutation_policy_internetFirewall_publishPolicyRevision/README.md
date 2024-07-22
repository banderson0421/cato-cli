
## CATO-CLI - mutation.policy.internetFirewall.publishPolicyRevision:
[Click here](https://api.catonetworks.com/documentation/#mutation-publishPolicyRevision) for documentation on this operation.

### Usage for mutation.policy.internetFirewall.publishPolicyRevision:

`cato mutation policy internetFirewall publishPolicyRevision -h`

`cato mutation policy internetFirewall publishPolicyRevision <accountID> <json>`

`cato mutation policy internetFirewall publishPolicyRevision 12345 $(cat < publishPolicyRevision.json)`

`cato mutation policy internetFirewall publishPolicyRevision 12345 '{"policyPublishRevisionInput": {"name": {"name": "String"}, "description": {"description": "String"}}, "internetFirewallPolicyMutationInput": {"policyMutationRevisionInput": {"id": {"id": "ID"}}}}'`

#### Operation Arguments for mutation.policy.internetFirewall.publishPolicyRevision ####
`policyPublishRevisionInput` [PolicyPublishRevisionInput] - (optional) N/A 
`internetFirewallPolicyMutationInput` [InternetFirewallPolicyMutationInput] - (optional) N/A 
`accountId` [ID] - (required) N/A 
