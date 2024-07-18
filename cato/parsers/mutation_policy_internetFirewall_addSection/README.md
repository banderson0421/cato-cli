
## CATO-CLI - mutation.policy.internetFirewall.addSection:
[Click here](https://api.catonetworks.com/documentation/#mutation-addSection) for documentation on this operation.

### Usage for mutation.policy.internetFirewall.addSection:

`cato mutation policy internetFirewall addSection -h`

`cato mutation policy internetFirewall addSection <accountID> <json>`

`cato mutation policy internetFirewall addSection 12345 $(cat < addSection.json)`

`cato mutation policy internetFirewall addSection 12345 '{"internetFirewallPolicyMutationInput": {"policyMutationRevisionInput": {"id": {"id": "ID"}}}, "policyAddSectionInput": {"policyAddSectionInfoInput": {"name": {"name": "String"}}, "policySectionPositionInput": {"position": {"position": "enum(PolicySectionPositionEnum)"}, "ref": {"ref": "ID"}}}}'`

#### Operation Arguments for mutation.policy.internetFirewall.addSection ####
`accountId` [ID] - (required) N/A 
`internetFirewallPolicyMutationInput` [InternetFirewallPolicyMutationInput] - (optional) N/A 
`policyAddSectionInput` [PolicyAddSectionInput] - (required) N/A 
