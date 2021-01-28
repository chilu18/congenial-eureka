import requests
from pprint import pprint


# Structure payload.
payload = {
    'source': 'universal',
    'url': 'https://www.offshore-mag.com/rigs-vessels',
}

# Get response.
response = requests.request(
    'POST',
    'https://realtime.oxylabs.io/v1/queries',
    auth=('uhellosafe', 'm5qjr2NMZh'),
    json=payload,
)

# Instead of response with job status and results url, this will return the
# JSON response with results.
pprint(response.json())