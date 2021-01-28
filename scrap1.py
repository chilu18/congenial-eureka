import requests
from pprint import pprint

# Structure payload.
payload = {
    'source': 'universal',
    'url': 'https://www.offshore-mag.com/rigs-vessels',
    'callback_url': 'https://your.callback.url',
    'storage_type': 's3',
    'storage_url': 'http://vdata-s.s3-ap-southeast-2.amazonaws.com/'
}

# Get response.
response = requests.request(
    'POST',
    'https://data.oxylabs.io/v1/queries',
    auth=('uhellosafe', 'm5qjr2NMZh'),
    json=payload,
)

# Print prettified response to stdout.
pprint(response.json())