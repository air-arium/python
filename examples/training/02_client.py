from api_call.client import APIClient
from auth.okta_auth import Auth

# REQUIRED ACTION: Set settings
# Define okta auth parameters
# Note: please set <PREFIX>_CLIENT_ID, <PREFIX>_CLIENT_SECRET
prefix = "ARIUM_TEST_WEB"
auth_settings = {}


# Create new Auth
auth = Auth(tenant="workspace1", role="basic", settings=auth_settings, prefix=prefix)

# Create new client
client = APIClient(auth=auth)

# Display client data
print(client)

# Access dedicated clients
calculations_client = client.service()
portfolios_client = client.portfolios()
events_client = client.events()
