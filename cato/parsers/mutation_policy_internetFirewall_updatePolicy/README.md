
## CATO-CLI - mutation.policy.internetFirewall.updatePolicy:
[Click here](https://api.catonetworks.com/documentation/#mutation-updatePolicy) for documentation on this operation.

### Usage for mutation.policy.internetFirewall.updatePolicy:

`cato mutation policy internetFirewall updatePolicy -h`

`cato mutation policy internetFirewall updatePolicy <accountID> <json>`

`cato mutation policy internetFirewall updatePolicy 12345 $(cat < updatePolicy.json)`

`cato mutation policy internetFirewall updatePolicy 12345 '{"internetFirewallPolicyUpdateInput": {"state": {"state": "enum(PolicyToggleState)"}}, "internetFirewallPolicyMutationInput": {"policyMutationRevisionInput": {"id": {"id": "ID"}}}}'`

#### Operation Arguments for mutation.policy.internetFirewall.updatePolicy ####
`internetFirewallPolicyUpdateInput` [InternetFirewallPolicyUpdateInput] - (required) N/A 
`internetFirewallPolicyMutationInput` [InternetFirewallPolicyMutationInput] - (optional) N/A 
`accountId` [ID] - (required) N/A 
