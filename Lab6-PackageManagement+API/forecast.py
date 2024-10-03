"""
Weather Forecast
This app makes an OpenWeather API call to display a 5-day weather forecast with data at 3-hour intervals,
based on the city name and country code entered by the user. It includes basic input validation and exception handling.
API documentation : https://openweathermap.org/forecast5
"""

import requests, os
from datetime import datetime


def get_api_key():
    try:
        key = os.environ.get('WEATHER_KEY')
        return key
    except Exception as e:
        print('Cannot get API key;', e)


def get_user_input():
    city = get_valid_city('Enter the city: ')
    country = get_valid_country('Enter the 2-letter country code: ')
    q = f'{city},{country}'
    return q


def get_valid_city(msg):
    # Validation to avoid accepting blank string
    while True:
        user_input = input(msg).strip()
        if user_input:
            return user_input.capitalize()
        print('Please enter a valid city name.')


def get_valid_country(msg):
    # Validation to only allow 2-letter input for the country code
    while True:
        user_input = input(msg).strip().upper()
        if len(user_input) == 2:
            return user_input
        print('Country code must be 2 letters.')


def set_units():
    # Asking for units choice with validation, then return the corresponding string for each unit system
    while True:
        units_choice = input('Choose units - Enter "M" for metric, "I" for imperial: ').upper()
        if units_choice == 'M':
            return 'metric', 'C', 'meter/sec'
        elif units_choice == 'I':
            return 'imperial', 'F', 'miles/hour'
        else:
            print('Please enter a valid choice.')


def get_data_from_api(query):
    try:
        url = 'https://api.openweathermap.org/data/2.5/forecast'
        json_data = requests.get(url, params=query).json()
        return json_data
    except Exception as e:
        print('Sorry, we could not get data from API server;', e)


def print_forecast(data, q, units_tuple):
    # If API call was successful with code 200, loop over the forecast list and print each forecast using formatting.
    # Otherwise, print the error code and message from API response.
    try:
        if data['cod'] == '200':
            list_of_forecasts = data['list']

            print(f'\n[ Weather Forcast - {q} ]')
            print(f'{'Date/Time':<25}{'Weather':<25}{f'Temperature ({units_tuple[1]})':<25}{f'Wind Speed ({units_tuple[2]})':<20}')

            for forecast in list_of_forecasts:
                timestamp = forecast['dt']
                date = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
                temp = forecast['main']['temp']
                description = forecast['weather'][0]['description']
                wind_speed = forecast['wind']['speed']
                print(f'{date:<25}{description:<25}{temp:<25}{wind_speed:<20}')

        else:
            print(f'Sorry, we could not get data from API server. (Error Code {data['cod']}: {data['message']})')

    except Exception as e:
        print('Error:', e)



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
