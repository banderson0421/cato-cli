
from ..parserApiClient import createRequest, get_help

def mutation_policy_parse(mutation_subparsers):
	mutation_policy_parser = mutation_subparsers.add_parser('policy', 
			help='policy', 
			usage=get_help("mutation_policy"))

	mutation_policy_subparsers = mutation_policy_parser.add_subparsers()

	mutation_policy_internetFirewall_parser = mutation_policy_subparsers.add_parser('internetFirewall', 
			help='internetFirewall', 
			usage=get_help("mutation_policy_internetFirewall"))

	mutation_policy_internetFirewall_subparsers = mutation_policy_internetFirewall_parser.add_subparsers()

	mutation_policy_internetFirewall_addRule_parser = mutation_policy_internetFirewall_subparsers.add_parser('addRule', 
			help='addRule', 
			usage=get_help("mutation_policy_internetFirewall_addRule"))

	mutation_policy_internetFirewall_addRule_parser.add_argument('accountID', help='The Account ID.')
	mutation_policy_internetFirewall_addRule_parser.add_argument('json', help='Variables in JSON format.')
	mutation_policy_internetFirewall_addRule_parser.add_argument('-t', const=True, default=False, nargs='?', 
		help='Print test request preview without sending api call')
	mutation_policy_internetFirewall_addRule_parser.add_argument('-v', const=True, default=False, nargs='?', 
		help='Verbose output')
	mutation_policy_internetFirewall_addRule_parser.add_argument('-p', const=True, default=False, nargs='?', 
		help='Pretty print')
	mutation_policy_internetFirewall_addRule_parser.set_defaults(func=createRequest,operation_name='mutation.policy.internetFirewall.addRule')

	mutation_policy_internetFirewall_updateRule_parser = mutation_policy_internetFirewall_subparsers.add_parser('updateRule', 
			help='updateRule', 
			usage=get_help("mutation_policy_internetFirewall_updateRule"))

	mutation_policy_internetFirewall_updateRule_parser.add_argument('accountID', help='The Account ID.')
	mutation_policy_internetFirewall_updateRule_parser.add_argument('json', help='Variables in JSON format.')
	mutation_policy_internetFirewall_updateRule_parser.add_argument('-t', const=True, default=False, nargs='?', 
		help='Print test request preview without sending api call')
	mutation_policy_internetFirewall_updateRule_parser.add_argument('-v', const=True, default=False, nargs='?', 
		help='Verbose output')
	mutation_policy_internetFirewall_updateRule_parser.add_argument('-p', const=True, default=False, nargs='?', 
		help='Pretty print')
	mutation_policy_internetFirewall_updateRule_parser.set_defaults(func=createRequest,operation_name='mutation.policy.internetFirewall.updateRule')

	mutation_policy_internetFirewall_removeRule_parser = mutation_policy_internetFirewall_subparsers.add_parser('removeRule', 
			help='removeRule', 
			usage=get_help("mutation_policy_internetFirewall_removeRule"))

	mutation_policy_internetFirewall_removeRule_parser.add_argument('accountID', help='The Account ID.')
	mutation_policy_internetFirewall_removeRule_parser.add_argument('json', help='Variables in JSON format.')
	mutation_policy_internetFirewall_removeRule_parser.add_argument('-t', const=True, default=False, nargs='?', 
		help='Print test request preview without sending api call')
	mutation_policy_internetFirewall_removeRule_parser.add_argument('-v', const=True, default=False, nargs='?', 
		help='Verbose output')
	mutation_policy_internetFirewall_removeRule_parser.add_argument('-p', const=True, default=False, nargs='?', 
		help='Pretty print')
	mutation_policy_internetFirewall_removeRule_parser.set_defaults(func=createRequest,operation_name='mutation.policy.internetFirewall.removeRule')

	mutation_policy_internetFirewall_moveRule_parser = mutation_policy_internetFirewall_subparsers.add_parser('moveRule', 
			help='moveRule', 
			usage=get_help("mutation_policy_internetFirewall_moveRule"))

	mutation_policy_internetFirewall_moveRule_parser.add_argument('accountID', help='The Account ID.')
	mutation_policy_internetFirewall_moveRule_parser.add_argument('json', help='Variables in JSON format.')
	mutation_policy_internetFirewall_moveRule_parser.add_argument('-t', const=True, default=False, nargs='?', 
		help='Print test request preview without sending api call')
	mutation_policy_internetFirewall_moveRule_parser.add_argument('-v', const=True, default=False, nargs='?', 
		help='Verbose output')
	mutation_policy_internetFirewall_moveRule_parser.add_argument('-p', const=True, default=False, nargs='?', 
		help='Pretty print')
	mutation_policy_internetFirewall_moveRule_parser.set_defaults(func=createRequest,operation_name='mutation.policy.internetFirewall.moveRule')

	mutation_policy_internetFirewall_addSection_parser = mutation_policy_internetFirewall_subparsers.add_parser('addSection', 
			help='addSection', 
			usage=get_help("mutation_policy_internetFirewall_addSection"))

	mutation_policy_internetFirewall_addSection_parser.add_argument('accountID', help='The Account ID.')
	mutation_policy_internetFirewall_addSection_parser.add_argument('json', help='Variables in JSON format.')
	mutation_policy_internetFirewall_addSection_parser.add_argument('-t', const=True, default=False, nargs='?', 
		help='Print test request preview without sending api call')
	mutation_policy_internetFirewall_addSection_parser.add_argument('-v', const=True, default=False, nargs='?', 
		help='Verbose output')
	mutation_policy_internetFirewall_addSection_parser.add_argument('-p', const=True, default=False, nargs='?', 
		help='Pretty print')
	mutation_policy_internetFirewall_addSection_parser.set_defaults(func=createRequest,operation_name='mutation.policy.internetFirewall.addSection')

	mutation_policy_internetFirewall_updateSection_parser = mutation_policy_internetFirewall_subparsers.add_parser('updateSection', 
			help='updateSection', 
			usage=get_help("mutation_policy_internetFirewall_updateSection"))

	mutation_policy_internetFirewall_updateSection_parser.add_argument('accountID', help='The Account ID.')
	mutation_policy_internetFirewall_updateSection_parser.add_argument('json', help='Variables in JSON format.')
	mutation_policy_internetFirewall_updateSection_parser.add_argument('-t', const=True, default=False, nargs='?', 
		help='Print test request preview without sending api call')
	mutation_policy_internetFirewall_updateSection_parser.add_argument('-v', const=True, default=False, nargs='?', 
		help='Verbose output')
	mutation_policy_internetFirewall_updateSection_parser.add_argument('-p', const=True, default=False, nargs='?', 
		help='Pretty print')
	mutation_policy_internetFirewall_updateSection_parser.set_defaults(func=createRequest,operation_name='mutation.policy.internetFirewall.updateSection')

	mutation_policy_internetFirewall_removeSection_parser = mutation_policy_internetFirewall_subparsers.add_parser('removeSection', 
			help='removeSection', 
			usage=get_help("mutation_policy_internetFirewall_removeSection"))

	mutation_policy_internetFirewall_removeSection_parser.add_argument('accountID', help='The Account ID.')
	mutation_policy_internetFirewall_removeSection_parser.add_argument('json', help='Variables in JSON format.')
	mutation_policy_internetFirewall_removeSection_parser.add_argument('-t', const=True, default=False, nargs='?', 
		help='Print test request preview without sending api call')
	mutation_policy_internetFirewall_removeSection_parser.add_argument('-v', const=True, default=False, nargs='?', 
		help='Verbose output')
	mutation_policy_internetFirewall_removeSection_parser.add_argument('-p', const=True, default=False, nargs='?', 
		help='Pretty print')
	mutation_policy_internetFirewall_removeSection_parser.set_defaults(func=createRequest,operation_name='mutation.policy.internetFirewall.removeSection')

	mutation_policy_internetFirewall_moveSection_parser = mutation_policy_internetFirewall_subparsers.add_parser('moveSection', 
			help='moveSection', 
			usage=get_help("mutation_policy_internetFirewall_moveSection"))

	mutation_policy_internetFirewall_moveSection_parser.add_argument('accountID', help='The Account ID.')
	mutation_policy_internetFirewall_moveSection_parser.add_argument('json', help='Variables in JSON format.')
	mutation_policy_internetFirewall_moveSection_parser.add_argument('-t', const=True, default=False, nargs='?', 
		help='Print test request preview without sending api call')
	mutation_policy_internetFirewall_moveSection_parser.add_argument('-v', const=True, default=False, nargs='?', 
		help='Verbose output')
	mutation_policy_internetFirewall_moveSection_parser.add_argument('-p', const=True, default=False, nargs='?', 
		help='Pretty print')
	mutation_policy_internetFirewall_moveSection_parser.set_defaults(func=createRequest,operation_name='mutation.policy.internetFirewall.moveSection')

	mutation_policy_internetFirewall_createPolicyRevision_parser = mutation_policy_internetFirewall_subparsers.add_parser('createPolicyRevision', 
			help='createPolicyRevision', 
			usage=get_help("mutation_policy_internetFirewall_createPolicyRevision"))

	mutation_policy_internetFirewall_createPolicyRevision_parser.add_argument('accountID', help='The Account ID.')
	mutation_policy_internetFirewall_createPolicyRevision_parser.add_argument('json', help='Variables in JSON format.')
	mutation_policy_internetFirewall_createPolicyRevision_parser.add_argument('-t', const=True, default=False, nargs='?', 
		help='Print test request preview without sending api call')
	mutation_policy_internetFirewall_createPolicyRevision_parser.add_argument('-v', const=True, default=False, nargs='?', 
		help='Verbose output')
	mutation_policy_internetFirewall_createPolicyRevision_parser.add_argument('-p', const=True, default=False, nargs='?', 
		help='Pretty print')
	mutation_policy_internetFirewall_createPolicyRevision_parser.set_defaults(func=createRequest,operation_name='mutation.policy.internetFirewall.createPolicyRevision')

	mutation_policy_internetFirewall_publishPolicyRevision_parser = mutation_policy_internetFirewall_subparsers.add_parser('publishPolicyRevision', 
			help='publishPolicyRevision', 
			usage=get_help("mutation_policy_internetFirewall_publishPolicyRevision"))

	mutation_policy_internetFirewall_publishPolicyRevision_parser.add_argument('accountID', help='The Account ID.')
	mutation_policy_internetFirewall_publishPolicyRevision_parser.add_argument('json', help='Variables in JSON format.')
	mutation_policy_internetFirewall_publishPolicyRevision_parser.add_argument('-t', const=True, default=False, nargs='?', 
		help='Print test request preview without sending api call')
	mutation_policy_internetFirewall_publishPolicyRevision_parser.add_argument('-v', const=True, default=False, nargs='?', 
		help='Verbose output')
	mutation_policy_internetFirewall_publishPolicyRevision_parser.add_argument('-p', const=True, default=False, nargs='?', 
		help='Pretty print')
	mutation_policy_internetFirewall_publishPolicyRevision_parser.set_defaults(func=createRequest,operation_name='mutation.policy.internetFirewall.publishPolicyRevision')

	mutation_policy_internetFirewall_discardPolicyRevision_parser = mutation_policy_internetFirewall_subparsers.add_parser('discardPolicyRevision', 
			help='discardPolicyRevision', 
			usage=get_help("mutation_policy_internetFirewall_discardPolicyRevision"))

	mutation_policy_internetFirewall_discardPolicyRevision_parser.add_argument('accountID', help='The Account ID.')
	mutation_policy_internetFirewall_discardPolicyRevision_parser.add_argument('json', help='Variables in JSON format.')
	mutation_policy_internetFirewall_discardPolicyRevision_parser.add_argument('-t', const=True, default=False, nargs='?', 
		help='Print test request preview without sending api call')
	mutation_policy_internetFirewall_discardPolicyRevision_parser.add_argument('-v', const=True, default=False, nargs='?', 
		help='Verbose output')
	mutation_policy_internetFirewall_discardPolicyRevision_parser.add_argument('-p', const=True, default=False, nargs='?', 
		help='Pretty print')
	mutation_policy_internetFirewall_discardPolicyRevision_parser.set_defaults(func=createRequest,operation_name='mutation.policy.internetFirewall.discardPolicyRevision')

	mutation_policy_internetFirewall_updatePolicy_parser = mutation_policy_internetFirewall_subparsers.add_parser('updatePolicy', 
			help='updatePolicy', 
			usage=get_help("mutation_policy_internetFirewall_updatePolicy"))

	mutation_policy_internetFirewall_updatePolicy_parser.add_argument('accountID', help='The Account ID.')
	mutation_policy_internetFirewall_updatePolicy_parser.add_argument('json', help='Variables in JSON format.')
	mutation_policy_internetFirewall_updatePolicy_parser.add_argument('-t', const=True, default=False, nargs='?', 
		help='Print test request preview without sending api call')
	mutation_policy_internetFirewall_updatePolicy_parser.add_argument('-v', const=True, default=False, nargs='?', 
		help='Verbose output')
	mutation_policy_internetFirewall_updatePolicy_parser.add_argument('-p', const=True, default=False, nargs='?', 
		help='Pretty print')
	mutation_policy_internetFirewall_updatePolicy_parser.set_defaults(func=createRequest,operation_name='mutation.policy.internetFirewall.updatePolicy')
