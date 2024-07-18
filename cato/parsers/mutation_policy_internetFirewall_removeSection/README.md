
## CATO-CLI - mutation.policy.internetFirewall.removeSection:
[Click here](https://api.catonetworks.com/documentation/#mutation-removeSection) for documentation on this operation.

### Usage for mutation.policy.internetFirewall.removeSection:

`cato mutation policy internetFirewall removeSection -h`

`cato mutation policy internetFirewall removeSection <accountID> <json>`

`cato mutation policy internetFirewall removeSection 12345 $(cat < removeSection.json)`

`cato mutation policy internetFirewall removeSection 12345 '{"internetFirewallPolicyMutationInput": {"policyMutationRevisionInput": {"id": {"id": "ID"}}}, "policyRemoveSectionInput": {"id": {"id": "ID"}}}'`

#### Operation Arguments for mutation.policy.internetFirewall.removeSection ####
`accountId` [ID] - (required) N/A 
`internetFirewallPolicyMutationInput` [InternetFirewallPolicyMutationInput] - (optional) N/A 
`policyRemoveSectionInput` [PolicyRemoveSectionInput] - (required) N/A 
