import requests

try:
    response = requests.get('https://catfact.ninja/fact')
    print(response)
    print(response.status_code)
    response.raise_for_status()  # raise an exception for 400 or 500 code - useful for try-catch block

    print(response.text)

    data = response.json()
    print(data)

    fact = data['fact']
    print(f'A random cat fact is {fact}')

except Exception as e:
    print('There was an error making the request -', e)