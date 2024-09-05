from dataclasses import dataclass

# with dataclass, python generate __init__, __str__ method automatically
# overriding __str__ method is possible if you want to format the string differently

# create Student class
@dataclass
class Student:
    name: str
    school_id: str
    gpa: float

def main():
    alex = Student('Alex', '1234', 3.5)
    sam = Student('Sam', '5678', 4.0)
    print(alex)
    print(sam)


if __name__ == '__main__':
    main()

# Add some comments in your code to compare the dataclass version to the "traditional" version.