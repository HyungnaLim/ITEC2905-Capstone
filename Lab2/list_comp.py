# List Comprehension

classes_registered = ['ITEC 1150', 'ITEC 1100', 'ITEC 1340', 'MATH 1100']
# make a new list of only ITEC classes
only_itec = [ c for c in classes_registered if c.startswith('ITEC') ]   # add filter with if
print(only_itec)

numbers = [2, 4, 6]
# make a new list with each number increased by one
numbers_plus_one = [ n+1 for n in numbers]
print(numbers_plus_one)

include_zero = [0, 3, 4, 0, 22, 1]
# filter 0 out from the list
exclude_zero = [ n for n in include_zero if n != 0 ]
print(exclude_zero)

another_list = [0, 10, 4, 0, 32]
# all number doubled & filter 0 out
new_list = [ n*2 for n in another_list if n != 0 ]
print(new_list)
