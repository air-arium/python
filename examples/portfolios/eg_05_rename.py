import json

from api_call.client import APIClient
from auth.okta_auth import Auth

# REQUIRED ACTION: Set settings
prefix = "ARIUM_TEST_WEB"
auth_settings = {}

# Create new client
auth = Auth(tenant="workspace1", role="basic", settings=auth_settings, prefix=prefix)
client = APIClient(auth=auth)

# REQUIRED ACTION: Set ref ids
# Select portfolio id
portfolio_id = "example-portfolio-reference"

# Rename portfolio
portfolio = client.portfolios().rename(portfolio_id, "renamed_portfolio")
print(f"portfolio: {json.dumps(portfolio, sort_keys=True, indent=4)}")
