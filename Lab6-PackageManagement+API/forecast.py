import requests, os
from datetime import datetime

key = os.environ.get('WEATHER_KEY')
url = 'https://api.openweathermap.org/data/2.5/forecast'

city = input('Enter the city: ')
country = input('Enter the 2-letter country code: ')
q = f'{city},{country}'

query = {'q':q, 'units':'metric', 'appid':key}

data = requests.get(url, params=query).json()
# print(data)

list_of_forecasts = data['list']

for forecast in list_of_forecasts:
    # print(forecast)
    timestamp = forecast['dt']
    date = datetime.fromtimestamp(timestamp)
    temp = forecast['main']['temp']
    print(f'At {date}, the temperature will be {temp}C')
