import requests

iss_url = 'http://api.open-notify.org/iss-now.json'
sunrise_sunset_url = 'http://api.sunrise-sunset.org/json'

# response = requests.get(url)
# response.raise_for_status()
# data = response.json()
# data_pos = data['iss_position']
# lat_long = (data_pos['latitude'], data_pos['longitude'])
#
# print(data)
# print(lat_long)

MY_LAT = 22.611500
MY_LONG = 75.677696

parameters = {
    'lat': MY_LAT,
    'lng': MY_LONG,
    'formatted':0
}

response = requests.get(sunrise_sunset_url, params=parameters)
response.raise_for_status()
data = response.json()
# data_pos = data['iss_position']
# lat_long = (data_pos['latitude'], data_pos['longitude'])

print(data)