
## CATO-CLI - mutation.policy.internetFirewall.removeRule:
[Click here](https://api.catonetworks.com/documentation/#mutation-removeRule) for documentation on this operation.

### Usage for mutation.policy.internetFirewall.removeRule:

`cato mutation policy internetFirewall removeRule -h`

`cato mutation policy internetFirewall removeRule <accountID> <json>`

`cato mutation policy internetFirewall removeRule 12345 $(cat < removeRule.json)`

`cato mutation policy internetFirewall removeRule 12345 '{"internetFirewallPolicyMutationInput": {"policyMutationRevisionInput": {"id": {"id": "ID"}}}, "internetFirewallRemoveRuleInput": {"id": {"id": "ID"}}}'`

#### Operation Arguments for mutation.policy.internetFirewall.removeRule ####
`accountId` [ID] - (required) N/A 
`internetFirewallPolicyMutationInput` [InternetFirewallPolicyMutationInput] - (optional) N/A 
`internetFirewallRemoveRuleInput` [InternetFirewallRemoveRuleInput] - (required) N/A 
