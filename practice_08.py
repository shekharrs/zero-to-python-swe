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

    
# staticmethod(function) -> method
# Convert a function to be a static method.
# A static method does not receive an implicit first argument.
    @staticmethod
    def hello():
        print("Hello!")

s1 = Student("John Cena", [99,77,32,56], "Computer Science")
# print(s1.name,"|",s1.marks,"|",s1.subjects)
s1.get_avg()
s1.hello()
'''





'''
# Create Account class with 2 attributes - balance & account no.
# Create methods for debit, credit & printing the balance.

class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc

    def debit(self, amount):
        self.balance -= amount
        print("Rs.",amount, "was debited")
        print("total available balance:", self.get_balance())
    
    def credit(self, amount):
        self.balance += amount
        print("Rs.",amount, "was credited")
        print("total available balance:", self.get_balance())

    def get_balance(self):
        return self.balance
    
acc1 = Account(1000000, 12345)
# print(acc1.balance)
# print(acc1.account_no)
acc1.debit(10000)
acc1.credit(200)
'''





'''
# Del Keyword - delete

class SchoolData:
    def __init__(self, fname):
        self.first_name = fname

s1 = SchoolData("John")
print(s1.first_name)
del s1.first_name
print(s1.first_name)
'''





'''
# Private(like) attributes & methods
''''''
Conceptual Implementations in Python
Private attributes & methods are meant to be used only within the class and are not accessible from outside the class
''''''

class Car:
    wheels = 4              # CLASS attr (shared)
    
    def __init__(self, color, speed):
        self.color = color          # PUBLIC instance attr
        self.__speed = speed        # PRIVATE instance attr
    
    def display(self):          # PUBLIC method
        return f"{self.color} car, Speed: {self.__speed}kmph"
    
    def accelerate(self, add_speed):
        self.__speed += add_speed   # PRIVATE method access

# Test
c1 = Car("Red", 60)
print(c1.color)        # Red ✓
print(c1.display())    # Red car, Speed: 70kmph ✓
# print(c1.__speed)    # ERROR!

c1.accelerate(10)
print(c1.display())
print(f"Wheels: {c1.wheels}")
'''





# Inheritance: child class inherit all attributes + methods from a parent class
'''
- Three types of inheritance
1. Single inheritance (Parent --> Child)
2. Multi-level inheritance(Parent --> Child [parent] --> [child])
3. Multiple inheritance([Parent 1] --> Child <-- [Parent 2])
'''

'''
# Single inheritance
class Car:
    @staticmethod
    def start():
        print("Car started..")

    @staticmethod
    def stop():
        print("Car stopped.")

class ToyotaCar(Car):
    def __init__(self, name):
        self.name = name

car1 = ToyotaCar("fortuner")
car2 = ToyotaCar("prius")
print(car1.name)
print(car2.name)
'''

'''
# Multi-level inheritance
class Car:
    @staticmethod
    def start():
        print("Car started..")

    @staticmethod
    def stop():
        print("Car stopped.")

class ToyotaCar(Car):
    def __init__(self, brand):
        self.brand = brand

class Fortuner(ToyotaCar):
    def __init__(self, type):
        self.type = type

car1 = Fortuner("petrol")
car1.start()
print(car1.type)
'''

'''
# Multiple inheritance
class A:
    varA = "Welcome A"

class B:
    varB = "Welcome B"

class C(A, B):
    varC = "Welcome C"

c1 = C()
print(c1.varC)
print(c1.varB)
print(c1.varA)
'''





'''
# @classmethod
class Person:
    name = "anonymous"

    def changeName(self, name):
        # self.name = name
        # Person.name = name   # indirect way to change the class attribute 
        # self.__class__.name = "John Cena"   # using __class__ the class attribute name can be changed

        ''''''
        - static method: do not change class attr and instance attr in that place the @staticmethod is used
        - class method: if the class attributes or properties are used only in that the @classmethod used
        - instance method: if the instance attributes or properties are used only in that the @instancemethod used
        ''''''

p1 = Person()
p1.changeName("John Cena")
print(p1.name)
print(Person.name)
'''





'''
# @property : we use @property decorator on any method in the class to use the method in the class to use the method as a property
class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math

    @property
    def percentage(self):
        return str((self.phy + self.chem + self.math) / 3) + "%"
    
stu1 = Student(98, 97, 99)
print(stu1.percentage)

stu1.phy = 86
print(stu1.percentage)
'''





# Polymorphism: Operator Overloading(when the same operator is allowed to have different meaning according to the context)
