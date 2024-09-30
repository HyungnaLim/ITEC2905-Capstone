import requests
from pprint import pprint

url = 'https://claraj.github.io/mock-bitcoin/currentprice.json'

res = requests.get(url)
json_res = res.json()
pprint(json_res)  # pretty print the json data

dollars_exchange_rate = json_res['bpi']['USD']['rate_float']
print(dollars_exchange_rate)

bitcoin = float(input('Enter the number of bitcoin: '))

bitcoin_to_dollars = bitcoin * dollars_exchange_rate

print(f'{bitcoin} bitcoin is equivalent to {bitcoin_to_dollars} dollars.')