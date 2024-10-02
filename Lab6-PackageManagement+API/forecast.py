"""
Part 1: Weather Forecast
Use the forecast API to create a detailed, neatly formatted 5-day forecast, for anywhere the user chooses. Ask the user for the location.
Make sure your API key is not coded into your program. Your program should read the key from an environment variable.
Use a query parameter dictionary in the request.
Your forecast should show the temperature and unit (your choice of F or C), weather description, and wind speed for every three hour interval, over the next 5 days.
Your program should handle errors. What type of errors do you anticipate? How will you deal with them?

Part 2: Time choice
Will you show the local time in Minnesota, or the UTC time? Why? Add some comments to your program explaining your choice. Reading: Unix Time

Part 3: Logging vs Print
When do you use one, when do you use the other? Replace any message that are only of interest to the developer with logging. When you run your program, it should only print user-friendly messages.
Make sure you can find the log output from your program.
Should you log sensitive information, for example, values of API keys?

To Submit: create GitHub repository for this program, with example log output. Submit repository link to the D2L dropbox.
"""

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
