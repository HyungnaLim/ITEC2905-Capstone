from datetime import datetime, date, time

# datetime library

today = date.today()
print(today)

tomorrow = date(2024, 9, 4)
print(tomorrow)

next_week = date.fromisoformat('2024-09-11')
print(next_week)

# readable date and time with timestamp
right_now = datetime.now()
print(right_now)

# timestamp of the date and time
print(right_now.timestamp())
print(right_now)

# convert timestamp to readable date and time
my_date = datetime.fromtimestamp(875643212)
print(my_date)



# Tuple - unmodifiable list

# list of tuples
city_state = [ ('Seattle', 'WA'), ('Portland', 'OR'), ('San Francisco', 'CA') ]

print(len(city_state))

# access individual tuple out from the list using index
first_city_state = city_state[0]
print(first_city_state)

# unpack each value in the tuple
city, state = first_city_state
print(city)

animals = ('lion', 'puma', 'tiger')
lion, puma, tiger = animals
# lion, puma = animals      # error because the number of items in tuple doesn't match
print(tiger)


# getting data from a function
def get_distance():
    miles = 1000
    km = miles * 1.6
    return miles, km    # using comma on return statement will convert data into tuple

distances = get_distance()  # output will be in tuple
print(distances)
print(distances[0])     # unpack data from tuple



# Set - unordered collection (order is not guaranteed), duplicates not allowed

cats = set()     # create empty set
cats.add('Lion')
cats.add('Tiger')
print(cats)
cats.add('Cheetah')
print(cats)

birds = { 'owl', 'robin', 'swan' }
print(birds)
birds.add('robin')  # won't duplicate robin to the set
print(birds)
birds.remove('owl')
birds.add('cardinal')
print(birds)

for bird in birds:
    print(birds)

# remove duplicates in the list by converting it into a set
bird_list = ['robin', 'swan', 'swan', 'eagle', 'cardinal', 'swan', 'robin']
bird_list_no_duplicates = list(set(bird_list))  # convert the list into a set, and then convert it back into a list
print(bird_list_no_duplicates)  # the result will be a list without any duplicate



# Exceptions with try & except

try:
    print(bird_list[10])
except:
    print('oops, that does not exist')
