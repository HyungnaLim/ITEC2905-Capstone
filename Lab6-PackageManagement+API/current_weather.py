import requests
import os

key = os.environ.get('WEATHER_KEY')

print(key)

city = 'Minneapolis,US'

url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}'

data = requests.get(url).json()

print(data)

temp = data['main']['temp']

print(f'Current temperature in {city} is {temp}F')


# try another city
city = 'Paris,FR'
data = requests.get(url).json()
temp = data['main']['temp']
print(f'Current temperature in {city} is {temp}F')

