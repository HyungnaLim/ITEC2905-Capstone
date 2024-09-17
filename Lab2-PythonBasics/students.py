# create class to define Student object
# __init__ is an initializer method, used in similar ways to a Java/C# constructor
class Student:
    def __init__(self, name, school_id, gpa):   # "self" is like "this" in Java, refers to the object that's being initialized
        self.name = name
        self.school_id = school_id
        self.gpa = gpa

    def __str__(self):  # returning string representation of an object
        return f'Student name: {self.name}, ID: {self.school_id}, GPA: {self.gpa}'

# create a Student object
alex = Student('Alex', '1234', '3.5')

# print each variable
print(alex.name)
print(alex.school_id)
print(alex.gpa)

# print the object
print(alex)
