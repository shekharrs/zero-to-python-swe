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





# Del Keyword - delete

class SchoolData:
    def __init__(self, fname):
        self.first_name = fname

s1 = SchoolData("John")
print(s1.first_name)
del s1.first_name
print(s1.first_name)