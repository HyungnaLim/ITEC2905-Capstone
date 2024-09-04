# prompt to ask for the number of classes
number_of_classes = input('How many classes are you taking this semester? ')

# set a empty list to collect class names
class_list = []

# while loop to ask for class names until user wants to stop
while True:
    class_name = input('Enter the name of the class or press enter to stop: ')
    if not class_name:
        break
    else:
        class_list.append(class_name)

# another approach using for loop with range using number_of_classes, need to handle ValueError for number_of_classes
# for _ in range (0, int(number_of_classes)):
#     class_name = input('Enter the name of the class: ')

# print all class names, one per line
print('The classes you are taking are: ')
for class_name in class_list:
    print(class_name)
