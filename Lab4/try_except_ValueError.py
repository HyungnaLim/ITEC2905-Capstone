from datetime import datetime

current_year = datetime.today().year

while True:
    try:
        birth_year = int(input('Enter the year you were born: '))   # expecting integer input
        break
    except ValueError:  # handle ValueError when user enter invalid input
        print('Please enter a number.')

age = current_year - birth_year

print(f'Thank you, you were born in {birth_year} which makes you about {age}.')