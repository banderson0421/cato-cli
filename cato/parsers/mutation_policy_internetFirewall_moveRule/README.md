
## CATO-CLI - mutation.policy.internetFirewall.moveRule:
[Click here](https://api.catonetworks.com/documentation/#mutation-moveRule) for documentation on this operation.

### Usage for mutation.policy.internetFirewall.moveRule:

`cato mutation policy internetFirewall moveRule -h`

`cato mutation policy internetFirewall moveRule <accountID> <json>`

`cato mutation policy internetFirewall moveRule 12345 $(cat < moveRule.json)`

`cato mutation policy internetFirewall moveRule 12345 '{"policyMoveRuleInput": {"id": {"id": "ID"}, "policyRulePositionInput": {"position": {"position": "enum(PolicyRulePositionEnum)"}, "ref": {"ref": "ID"}}}, "internetFirewallPolicyMutationInput": {"policyMutationRevisionInput": {"id": {"id": "ID"}}}}'`

#### Operation Arguments for mutation.policy.internetFirewall.moveRule ####
`policyMoveRuleInput` [PolicyMoveRuleInput] - (required) N/A 
`internetFirewallPolicyMutationInput` [InternetFirewallPolicyMutationInput] - (optional) N/A 
`accountId` [ID] - (required) N/A 
