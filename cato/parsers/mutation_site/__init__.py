
from ..parserApiClient import createRequest, get_help

def mutation_site_parse(mutation_subparsers):
	mutation_site_parser = mutation_subparsers.add_parser('site', 
			help='site', 
			usage=get_help("mutation_site"))

	mutation_site_subparsers = mutation_site_parser.add_subparsers()

	mutation_site_addNetworkRange_parser = mutation_site_subparsers.add_parser('addNetworkRange', 
			help='addNetworkRange', 
			usage=get_help("mutation_site_addNetworkRange"))

	mutation_site_addNetworkRange_parser.add_argument('accountID', help='The Account ID.')
	mutation_site_addNetworkRange_parser.add_argument('json', help='Variables in JSON format.')
	mutation_site_addNetworkRange_parser.add_argument('-t', const=True, default=False, nargs='?', 
		help='Print test request preview without sending api call')
	mutation_site_addNetworkRange_parser.add_argument('-v', const=True, default=False, nargs='?', 
		help='Verbose output')
	mutation_site_addNetworkRange_parser.add_argument('-p', const=True, default=False, nargs='?', 
		help='Pretty print')
	mutation_site_addNetworkRange_parser.set_defaults(func=createRequest,operation_name='mutation.site.addNetworkRange')

	mutation_site_addSocketSite_parser = mutation_site_subparsers.add_parser('addSocketSite', 
			help='addSocketSite', 
			usage=get_help("mutation_site_addSocketSite"))

	mutation_site_addSocketSite_parser.add_argument('accountID', help='The Account ID.')
	mutation_site_addSocketSite_parser.add_argument('json', help='Variables in JSON format.')
	mutation_site_addSocketSite_parser.add_argument('-t', const=True, default=False, nargs='?', 
		help='Print test request preview without sending api call')
	mutation_site_addSocketSite_parser.add_argument('-v', const=True, default=False, nargs='?', 
		help='Verbose output')
	mutation_site_addSocketSite_parser.add_argument('-p', const=True, default=False, nargs='?', 
		help='Pretty print')
	mutation_site_addSocketSite_parser.set_defaults(func=createRequest,operation_name='mutation.site.addSocketSite')

	mutation_site_addStaticHost_parser = mutation_site_subparsers.add_parser('addStaticHost', 
			help='addStaticHost', 
			usage=get_help("mutation_site_addStaticHost"))

	mutation_site_addStaticHost_parser.add_argument('accountID', help='The Account ID.')
	mutation_site_addStaticHost_parser.add_argument('json', help='Variables in JSON format.')
	mutation_site_addStaticHost_parser.add_argument('-t', const=True, default=False, nargs='?', 
		help='Print test request preview without sending api call')
	mutation_site_addStaticHost_parser.add_argument('-v', const=True, default=False, nargs='?', 
		help='Verbose output')
	mutation_site_addStaticHost_parser.add_argument('-p', const=True, default=False, nargs='?', 
		help='Pretty print')
	mutation_site_addStaticHost_parser.set_defaults(func=createRequest,operation_name='mutation.site.addStaticHost')

	mutation_site_removeNetworkRange_parser = mutation_site_subparsers.add_parser('removeNetworkRange', 
			help='removeNetworkRange', 
			usage=get_help("mutation_site_removeNetworkRange"))

	mutation_site_removeNetworkRange_parser.add_argument('accountID', help='The Account ID.')
	mutation_site_removeNetworkRange_parser.add_argument('json', help='Variables in JSON format.')
	mutation_site_removeNetworkRange_parser.add_argument('-t', const=True, default=False, nargs='?', 
		help='Print test request preview without sending api call')
	mutation_site_removeNetworkRange_parser.add_argument('-v', const=True, default=False, nargs='?', 
		help='Verbose output')
	mutation_site_removeNetworkRange_parser.add_argument('-p', const=True, default=False, nargs='?', 
		help='Pretty print')
	mutation_site_removeNetworkRange_parser.set_defaults(func=createRequest,operation_name='mutation.site.removeNetworkRange')

	mutation_site_removeSite_parser = mutation_site_subparsers.add_parser('removeSite', 
			help='removeSite', 
			usage=get_help("mutation_site_removeSite"))

	mutation_site_removeSite_parser.add_argument('accountID', help='The Account ID.')
	mutation_site_removeSite_parser.add_argument('json', help='Variables in JSON format.')
	mutation_site_removeSite_parser.add_argument('-t', const=True, default=False, nargs='?', 
		help='Print test request preview without sending api call')
	mutation_site_removeSite_parser.add_argument('-v', const=True, default=False, nargs='?', 
		help='Verbose output')
	mutation_site_removeSite_parser.add_argument('-p', const=True, default=False, nargs='?', 
		help='Pretty print')
	mutation_site_removeSite_parser.set_defaults(func=createRequest,operation_name='mutation.site.removeSite')

	mutation_site_removeStaticHost_parser = mutation_site_subparsers.add_parser('removeStaticHost', 
			help='removeStaticHost', 
			usage=get_help("mutation_site_removeStaticHost"))

	mutation_site_removeStaticHost_parser.add_argument('accountID', help='The Account ID.')
	mutation_site_removeStaticHost_parser.add_argument('json', help='Variables in JSON format.')
	mutation_site_removeStaticHost_parser.add_argument('-t', const=True, default=False, nargs='?', 
		help='Print test request preview without sending api call')
	mutation_site_removeStaticHost_parser.add_argument('-v', const=True, default=False, nargs='?', 
		help='Verbose output')
	mutation_site_removeStaticHost_parser.add_argument('-p', const=True, default=False, nargs='?', 
		help='Pretty print')
	mutation_site_removeStaticHost_parser.set_defaults(func=createRequest,operation_name='mutation.site.removeStaticHost')

	mutation_site_updateHa_parser = mutation_site_subparsers.add_parser('updateHa', 
			help='updateHa', 
			usage=get_help("mutation_site_updateHa"))

	mutation_site_updateHa_parser.add_argument('accountID', help='The Account ID.')
	mutation_site_updateHa_parser.add_argument('json', help='Variables in JSON format.')
	mutation_site_updateHa_parser.add_argument('-t', const=True, default=False, nargs='?', 
		help='Print test request preview without sending api call')
	mutation_site_updateHa_parser.add_argument('-v', const=True, default=False, nargs='?', 
		help='Verbose output')
	mutation_site_updateHa_parser.add_argument('-p', const=True, default=False, nargs='?', 
		help='Pretty print')
	mutation_site_updateHa_parser.set_defaults(func=createRequest,operation_name='mutation.site.updateHa')

	mutation_site_updateNetworkRange_parser = mutation_site_subparsers.add_parser('updateNetworkRange', 
			help='updateNetworkRange', 
			usage=get_help("mutation_site_updateNetworkRange"))

	mutation_site_updateNetworkRange_parser.add_argument('accountID', help='The Account ID.')
	mutation_site_updateNetworkRange_parser.add_argument('json', help='Variables in JSON format.')
	mutation_site_updateNetworkRange_parser.add_argument('-t', const=True, default=False, nargs='?', 
		help='Print test request preview without sending api call')
	mutation_site_updateNetworkRange_parser.add_argument('-v', const=True, default=False, nargs='?', 
		help='Verbose output')
	mutation_site_updateNetworkRange_parser.add_argument('-p', const=True, default=False, nargs='?', 
		help='Pretty print')
	mutation_site_updateNetworkRange_parser.set_defaults(func=createRequest,operation_name='mutation.site.updateNetworkRange')

	mutation_site_updateSiteGeneralDetails_parser = mutation_site_subparsers.add_parser('updateSiteGeneralDetails', 
			help='updateSiteGeneralDetails', 
			usage=get_help("mutation_site_updateSiteGeneralDetails"))

	mutation_site_updateSiteGeneralDetails_parser.add_argument('accountID', help='The Account ID.')
	mutation_site_updateSiteGeneralDetails_parser.add_argument('json', help='Variables in JSON format.')
	mutation_site_updateSiteGeneralDetails_parser.add_argument('-t', const=True, default=False, nargs='?', 
		help='Print test request preview without sending api call')
	mutation_site_updateSiteGeneralDetails_parser.add_argument('-v', const=True, default=False, nargs='?', 
		help='Verbose output')
	mutation_site_updateSiteGeneralDetails_parser.add_argument('-p', const=True, default=False, nargs='?', 
		help='Pretty print')
	mutation_site_updateSiteGeneralDetails_parser.set_defaults(func=createRequest,operation_name='mutation.site.updateSiteGeneralDetails')

	mutation_site_updateSocketInterface_parser = mutation_site_subparsers.add_parser('updateSocketInterface', 
			help='updateSocketInterface', 
			usage=get_help("mutation_site_updateSocketInterface"))

	mutation_site_updateSocketInterface_parser.add_argument('accountID', help='The Account ID.')
	mutation_site_updateSocketInterface_parser.add_argument('json', help='Variables in JSON format.')
	mutation_site_updateSocketInterface_parser.add_argument('-t', const=True, default=False, nargs='?', 
		help='Print test request preview without sending api call')
	mutation_site_updateSocketInterface_parser.add_argument('-v', const=True, default=False, nargs='?', 
		help='Verbose output')
	mutation_site_updateSocketInterface_parser.add_argument('-p', const=True, default=False, nargs='?', 
		help='Pretty print')
	mutation_site_updateSocketInterface_parser.set_defaults(func=createRequest,operation_name='mutation.site.updateSocketInterface')

	mutation_site_updateStaticHost_parser = mutation_site_subparsers.add_parser('updateStaticHost', 
			help='updateStaticHost', 
			usage=get_help("mutation_site_updateStaticHost"))

	mutation_site_updateStaticHost_parser.add_argument('accountID', help='The Account ID.')
	mutation_site_updateStaticHost_parser.add_argument('json', help='Variables in JSON format.')
	mutation_site_updateStaticHost_parser.add_argument('-t', const=True, default=False, nargs='?', 
		help='Print test request preview without sending api call')
	mutation_site_updateStaticHost_parser.add_argument('-v', const=True, default=False, nargs='?', 
		help='Verbose output')
	mutation_site_updateStaticHost_parser.add_argument('-p', const=True, default=False, nargs='?', 
		help='Pretty print')
	mutation_site_updateStaticHost_parser.set_defaults(func=createRequest,operation_name='mutation.site.updateStaticHost')
