import requests
import json
from pprint import pprint


# Get payload from file.
with open('keywords.json', 'r') as f:
    payload = json.loads(f.read())

response = requests.request(
    'POST',
    'https://data.oxylabs.io/v1/queries/batch',
    auth=('uhellosafe', 'm5qjr2NMZh'),
    json=payload,
)

# Print prettified response.
pprint(response.json())