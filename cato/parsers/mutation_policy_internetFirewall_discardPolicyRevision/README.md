
## CATO-CLI - mutation.policy.internetFirewall.discardPolicyRevision:
[Click here](https://api.catonetworks.com/documentation/#mutation-discardPolicyRevision) for documentation on this operation.

### Usage for mutation.policy.internetFirewall.discardPolicyRevision:

`cato mutation policy internetFirewall discardPolicyRevision -h`

`cato mutation policy internetFirewall discardPolicyRevision <accountID> <json>`

`cato mutation policy internetFirewall discardPolicyRevision 12345 $(cat < discardPolicyRevision.json)`

`cato mutation policy internetFirewall discardPolicyRevision 12345 '{"internetFirewallPolicyMutationInput": {"policyMutationRevisionInput": {"id": {"id": "ID"}}}, "policyDiscardRevisionInput": {"id": {"id": "ID"}}}'`

#### Operation Arguments for mutation.policy.internetFirewall.discardPolicyRevision ####
`accountId` [ID] - (required) N/A 
`internetFirewallPolicyMutationInput` [InternetFirewallPolicyMutationInput] - (optional) N/A 
`policyDiscardRevisionInput` [PolicyDiscardRevisionInput] - (optional) N/A 
