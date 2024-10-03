"""
Weather Forecast

"""

import requests, os
from datetime import datetime


def get_api_key():
    try:
        key = os.environ.get('WEATHER_KEY')
        return key
    except Exception as e:
        print('Cannot find API key; ', e)


def get_user_input():
    city = get_valid_input('Enter the city: ')
    country = get_valid_input('Enter the 2-letter country code: ')
    q = f'{city},{country}'
    return q


# TODO: work on validations
def get_valid_input(msg):
    user_input = input(msg)
    return user_input.strip().upper()


def set_units():
    units_choice = get_valid_input('Choose units - Enter "M" for metric, "I" for imperial: ')
    if units_choice == 'M':
        return 'metric', 'C', 'meter/sec'
    elif units_choice == 'I':
        return 'imperial', 'F', 'miles/hour'
    else:
        return 'standard', 'Kelvin', 'meter/sec'


def get_data_from_api(query):
    url = 'https://api.openweathermap.org/data/2.5/forecast'
    json_data = requests.get(url, params=query).json()
    return json_data


def print_forecast(data, q, units_tuple):
    list_of_forecasts = data['list']

    print(f'\nWeather Forcast - {q}')
    for forecast in list_of_forecasts:
        timestamp = forecast['dt']
        date = datetime.fromtimestamp(timestamp)
        temp = forecast['main']['temp']
        description = forecast['weather'][0]['description']
        wind_speed = forecast['wind']['speed']
        print(f'{date} | Weather: {description}, Temperature: {temp} {units_tuple[1]}, Wind Speed: {wind_speed} {units_tuple[2]}')


def main():
    try:
        key = get_api_key()
        city_and_country = get_user_input()
        units_tuple = set_units()
        query = {'q':city_and_country, 'units':units_tuple[0], 'appid':key}
        forecast_data = get_data_from_api(query)
        print_forecast(forecast_data, city_and_country, units_tuple)

    except Exception as e:
        print('Error:', e)


if __name__ == "__main__":
    main()
