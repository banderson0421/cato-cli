
## CATO-CLI - mutation.policy.internetFirewall.publishPolicyRevision:
[Click here](https://api.catonetworks.com/documentation/#mutation-publishPolicyRevision) for documentation on this operation.

### Usage for mutation.policy.internetFirewall.publishPolicyRevision:

`cato mutation policy internetFirewall publishPolicyRevision -h`

`cato mutation policy internetFirewall publishPolicyRevision <accountID> <json>`

`cato mutation policy internetFirewall publishPolicyRevision 12345 $(cat < publishPolicyRevision.json)`

`cato mutation policy internetFirewall publishPolicyRevision 12345 '{"internetFirewallPolicyMutationInput": {"policyMutationRevisionInput": {"id": {"id": "ID"}}}, "policyPublishRevisionInput": {"description": {"description": "String"}, "name": {"name": "String"}}}'`

#### Operation Arguments for mutation.policy.internetFirewall.publishPolicyRevision ####
`accountId` [ID] - (required) N/A 
`internetFirewallPolicyMutationInput` [InternetFirewallPolicyMutationInput] - (optional) N/A 
`policyPublishRevisionInput` [PolicyPublishRevisionInput] - (optional) N/A 
