
from ..parserApiClient import createRequest, get_help

def query_eventsFeed_parse(query_subparsers):
	query_eventsFeed_parser = query_subparsers.add_parser('eventsFeed', 
			help='eventsFeed', 
			usage=get_help("query_eventsFeed"))

	query_eventsFeed_parser.add_argument('accountID', help='The Account ID.')
	query_eventsFeed_parser.add_argument('json', help='Variables in JSON format.')
	query_eventsFeed_parser.add_argument('-t', const=True, default=False, nargs='?', 
		help='Print test request preview without sending api call')
	query_eventsFeed_parser.add_argument('-v', const=True, default=False, nargs='?', 
		help='Verbose output')
	query_eventsFeed_parser.add_argument('-p', const=True, default=False, nargs='?', 
		help='Pretty print')
	query_eventsFeed_parser.set_defaults(func=createRequest,operation_name='query.eventsFeed')
