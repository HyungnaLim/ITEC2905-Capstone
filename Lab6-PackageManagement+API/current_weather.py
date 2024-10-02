from itertools import count

import requests
import os

key = os.environ.get('WEATHER_KEY')
url = f'https://api.openweathermap.org/data/2.5/weather'

# query = {'q' : 'Tokyo,JP', 'units' : 'metric', 'appid' : key}
#
# data = requests.get(url, params=query).json()
# print(data)
# temp = data['main']['temp']
#
# print(f'Current temperature in {query.get('q')} is {temp}C')
#
#
# # try another city
# query2 = {'q' : 'Paris,FR', 'units' : 'metric', 'appid' : key}
# data = requests.get(url, params=query2).json()
# temp = data['main']['temp']
# print(f'Current temperature in {query2.get('q')} is {temp}C')


# try with user input
city = input('Enter the city: ').strip().upper()
country = input('Enter the 2-letter country code: ').strip().upper()

q = f'{city},{country}'
query_with_user_input = {'q':q, 'units':'metric', 'appid':key}

data = requests.get(url, params=query_with_user_input).json()
temp = data['main']['temp']

print(f'Current temperature in {q} is {temp}C')
