# OOPs (Object Oriented Programming ) Classes & Objects

'''
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
'''

# Create student class that takes name & marks of 3 subjects as arguments in constructor. Then create a method to print the average

class Student:
    def __init__(self, name, marks, subjects):
        self.name = name
        self.marks = marks
        self.subjects = subjects
        print("Adding new data of students in the DB...")

    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("HEY", self.name, "your avg score is:", sum/3)

    @staticmethod
    def hello():
        print("Hello!")

s1 = Student("John Cena", [99,77,32,56], "Computer Science")
# print(s1.name,"|",s1.marks,"|",s1.subjects)
s1.get_avg()

s1.hello()
