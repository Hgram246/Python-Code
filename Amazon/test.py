import requests 
import json
from pprint import pprint 
# Structure payload.
payload = {
    'source': 'amazon_product',
    'query': 'B07FZ8S74R',
    'geo_location': '98036',
    'parse': True
    } 
# Get response. 
response = requests.request(
    'POST',
    'https://realtime.oxylabs.io/v1/queries',
    auth=('Hgramamazon_x39yd', 'Sparkyboy07+'),
    json=payload,
    )
print(response.json())

json_data = response.json

def extract_key_value(json_data, key):
    data = json.loads(json_data)
    value = data.get(key)
    return value

price = extract_key_value(json_data, "price")
print(price)