
## CATO-CLI - mutation.policy.wanFirewall.publishPolicyRevision:
[Click here](https://api.catonetworks.com/documentation/#mutation-publishPolicyRevision) for documentation on this operation.

### Usage for mutation.policy.wanFirewall.publishPolicyRevision:

`cato mutation policy wanFirewall publishPolicyRevision -h`

`cato mutation policy wanFirewall publishPolicyRevision <accountID> <json>`

`cato mutation policy wanFirewall publishPolicyRevision 12345 "$(cat < publishPolicyRevision.json)"`

`cato mutation policy wanFirewall publishPolicyRevision 12345 '{"PolicyPublishRevisionInput": {"description": {"description": "String"}, "name": {"name": "String"}}, "WanFirewallPolicyMutationInput": {"PolicyMutationRevisionInput": {"id": {"id": "ID"}}}}'`

#### Operation Arguments for mutation.policy.wanFirewall.publishPolicyRevision ####
`PolicyPublishRevisionInput` [PolicyPublishRevisionInput] - (optional) N/A 
`WanFirewallPolicyMutationInput` [WanFirewallPolicyMutationInput] - (optional) N/A 
`accountId` [ID] - (required) N/A 
