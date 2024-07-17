import json

from api_call.client import APIClient
from auth.okta_auth import Auth

# REQUIRED ACTION: Set settings
prefix = "ARIUM_TEST_WEB"
auth_settings = {}

# Create new client
auth = Auth(tenant="workspace1", role="basic", settings=auth_settings, prefix=prefix)
client = APIClient(auth=auth)

# Get list of latest versions of events assets
latest_sizes_list = client.sizes().list()
for sizes in latest_sizes_list:
    print(f"sizes (latest): {json.dumps(sizes, sort_keys=True, indent=4)}")

# Get list of all versions of events assets
all_sizes_list = client.sizes().list(latest=False)
for sizes in all_sizes_list:
    print(f"sizes: {json.dumps(sizes, sort_keys=True, indent=4)}")
