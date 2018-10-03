#!/usr/bin/python3

import requests

GOOGLE_MAPS_API_URL = 'http://maps.googleapis.com/maps/api/geocode/json'

params = {
    'address': 'The Green Park Pendik Hotel, İstanbul, Turkey',
    'sensor': 'false',
    'region': 'tr'
}

req = requests.get(GOOGLE_MAPS_API_URL, params=params)
res = req.json()

print(res)
result = res['results'][0]

geodata = dict()
geodata['lat'] = result['geometry']['location']['lat']
geodata['lng'] = result['geometry']['location']['lng']
geodata['address'] = result['formatted_address']

print('{address}. (lat, lng) = ({lat}, {lng})'.format(**geodata))
