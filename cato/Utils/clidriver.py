
import os
import argparse
import json
import cato
from graphql_client import Configuration
from graphql_client.api_client import ApiException
from ..parsers.parserApiClient import get_help
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
if "CATO_TOKEN" not in os.environ:
	print("Missing authentication, please set the CATO_TOKEN environment variable with your api key.")
	exit()
CATO_TOKEN = os.getenv("CATO_TOKEN")
CATO_DEBUG = bool(os.getenv("CATO_DEBUG", False))
from ..parsers.raw import raw_parse
from ..parsers.mutation_admin import mutation_admin_parse
from ..parsers.mutation_policy import mutation_policy_parse
from ..parsers.mutation_site import mutation_site_parse
from ..parsers.query_accountBySubdomain import query_accountBySubdomain_parse
from ..parsers.query_accountMetrics import query_accountMetrics_parse
from ..parsers.query_accountRoles import query_accountRoles_parse
from ..parsers.query_accountSnapshot import query_accountSnapshot_parse
from ..parsers.query_admin import query_admin_parse
from ..parsers.query_admins import query_admins_parse
from ..parsers.query_appStats import query_appStats_parse
from ..parsers.query_appStatsTimeSeries import query_appStatsTimeSeries_parse
from ..parsers.query_auditFeed import query_auditFeed_parse
from ..parsers.query_entityLookup import query_entityLookup_parse
from ..parsers.query_events import query_events_parse
from ..parsers.query_eventsFeed import query_eventsFeed_parse
from ..parsers.query_eventsTimeSeries import query_eventsTimeSeries_parse
from ..parsers.query_licensing import query_licensing_parse
from ..parsers.query_policy import query_policy_parse
from ..parsers.query_subDomains import query_subDomains_parse
from ..parsers.query_xdr import query_xdr_parse

configuration = Configuration()
configuration.verify_ssl = False
configuration.api_key["x-api-key"] = CATO_TOKEN
configuration.host = "{}".format(cato.__cato_host__)
configuration.debug = CATO_DEBUG

parser = argparse.ArgumentParser(prog='cato', usage='%(prog)s <operationType> <operationName> [options]', description="CLI for query on CATO via API.")
parser.add_argument('--version', action='version', version=cato.__version__)
subparsers = parser.add_subparsers()
raw_parsers = subparsers.add_parser('raw', help='Raw GraphQL', usage=get_help("raw"))
raw_parser = raw_parse(raw_parsers)
query_parser = subparsers.add_parser('query', help='Query', usage='cato query <operationName> [options]')
query_subparsers = query_parser.add_subparsers(description='valid subcommands', help='additional help')
mutation_parser = subparsers.add_parser('mutation', help='Mutation', usage='cato mutation <operationName> [options]')
mutation_subparsers = mutation_parser.add_subparsers(description='valid subcommands', help='additional help')

mutation_admin_parser = mutation_admin_parse(mutation_subparsers)
mutation_policy_parser = mutation_policy_parse(mutation_subparsers)
mutation_site_parser = mutation_site_parse(mutation_subparsers)
query_accountBySubdomain_parser = query_accountBySubdomain_parse(query_subparsers)
query_accountMetrics_parser = query_accountMetrics_parse(query_subparsers)
query_accountRoles_parser = query_accountRoles_parse(query_subparsers)
query_accountSnapshot_parser = query_accountSnapshot_parse(query_subparsers)
query_admin_parser = query_admin_parse(query_subparsers)
query_admins_parser = query_admins_parse(query_subparsers)
query_appStats_parser = query_appStats_parse(query_subparsers)
query_appStatsTimeSeries_parser = query_appStatsTimeSeries_parse(query_subparsers)
query_auditFeed_parser = query_auditFeed_parse(query_subparsers)
query_entityLookup_parser = query_entityLookup_parse(query_subparsers)
query_events_parser = query_events_parse(query_subparsers)
query_eventsFeed_parser = query_eventsFeed_parse(query_subparsers)
query_eventsTimeSeries_parser = query_eventsTimeSeries_parse(query_subparsers)
query_licensing_parser = query_licensing_parse(query_subparsers)
query_policy_parser = query_policy_parse(query_subparsers)
query_subDomains_parser = query_subDomains_parse(query_subparsers)
query_xdr_parser = query_xdr_parse(query_subparsers)


def main(args=None):
	args = parser.parse_args(args=args)
	try:
		response = args.func(args, configuration)

		if type(response) == ApiException:
			print("ERROR! Status code: {}".format(response.status))
			print(response)
		else:
			if response!=None:
				print(json.dumps(response[0], sort_keys=True, indent=4))
	except AttributeError:
		print('Missing arguments. Usage: cato <operation> -h')
