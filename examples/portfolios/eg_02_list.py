import json

from api_call.client import APIClient
from auth.okta_auth import Auth

# REQUIRED ACTION: Set settings
prefix = "ARIUM_TEST_WEB"
auth_settings = {}

# Create new client
auth = Auth(tenant="workspace1", role="basic", settings=auth_settings, prefix=prefix)
client = APIClient(auth=auth)

# Get list of latest versions of portfolio assets
latest_portfolios_list = client.portfolios().list()
for portfolio in latest_portfolios_list:
    print(f"portfolio (latest): {json.dumps(portfolio, sort_keys=True, indent=4)}")

# Get list of ALL portfolio assets
all_portfolios_list = client.portfolios().list(latest=False)
for portfolio in all_portfolios_list:
    print(f"portfolio: {json.dumps(portfolio, sort_keys=True, indent=4)}")
