# can you detect if the month entered is the same as the current month, no matter when you run the program?
import datetime
current_time = datetime.datetime.now()
current_month = current_time.month

# Ask for user's name
name = input('What is your name? ')

# Ask for birthday month
# validation for number, letter, and so on
birth_month = input('What month were you born in? Answer in number: ')

# print a hello message using format string
print(f'Hello, {name}!')

# print the number of letters in user name
letters_in_name = len(name)
print(f'There is {letters_in_name} letters in your name')

# if their birthday month is this month or not
if birth_month == current_month:
    print('Happy birthday month!')
else:
    print('Your birthday is not this month')
