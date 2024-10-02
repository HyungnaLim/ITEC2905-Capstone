import requests, os
from datetime import datetime

key = os.environ.get('WEATHER_KEY')
url = 'https://api.openweathermap.org/data/2.5/forecast'

city = input('Enter the city: ').upper().strip()
country = input('Enter the 2-letter country code: ').upper().strip()
q = f'{city},{country}'
units = input('Choose units - Enter "m" for metric, "i" for imperial: ').lower()

if units == 'm':
    units = 'metric'
    unit_temperature = 'C'
    unit_speed = 'meter/sec'
elif units == 'i':
    units = 'imperial'
    unit_temperature = 'F'
    unit_speed = 'miles/hour'
else:
    units = 'standard'
    unit_temperature = 'Kelvin'
    unit_speed = 'meter/sec'

query = {'q':q, 'units':units, 'appid':key}

data = requests.get(url, params=query).json()
# print(data)

list_of_forecasts = data['list']

print(f'\nWeather Forcast - {q}')
for forecast in list_of_forecasts:
    timestamp = forecast['dt']
    date = datetime.fromtimestamp(timestamp)
    temp = forecast['main']['temp']
    description = forecast['weather'][0]['description']
    wind_speed = forecast['wind']['speed']
    print(f'{date} | Weather: {description}, Temperature: {temp} {unit_temperature}, Wind Speed: {wind_speed} {unit_speed}')
