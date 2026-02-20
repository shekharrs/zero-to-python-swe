# OOPs (Object Oriented Programming ) Classes & Objects

class Student:

    # default constructors
    def __init__(self):
        pass

    # parameterized constructors
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("adding new data of students in the database...")

s1 = Student("John Cena", 99)
print(s1.name, s1.marks)

s2 = Student("Roman", 76)
print(s2.name, s2.marks)