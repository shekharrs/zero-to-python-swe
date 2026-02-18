# Dictionary & Set


'''
# Store following word meanings in a python dictionary
table : “a piece of furniture”, “list of facts & figures”
cat : “a small animal”

dict = {
    "cat": "a small animal",
    "table": ["a piece of furniture", "list of facts & figures"]
}
print(dict)
'''



'''
# You are given a list of subjects for students. Assume one classroom is required for 1 subject. How many classrooms are needed by all students.
subj = {
    "python", "java", "C++", "python", "javascript", "java", "python", "java", "C++", "C"
}
print(len(subj))
'''



'''
#WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with
# an empty dictionary & add one by one. Use subject name as key & marks as value. 

marks = {}

x = int(input("Enter Science: "))
marks.update({"Science": x})

y = int(input("Enter Maths: "))
marks.update({"Maths": y})

z = int(input("Enter English: "))
marks.update({"English": z})

print(marks)
'''



'''
#Figure out a way to store 9 & 9.0 as separate values in the set.
# (You can take help of built-in data types)

values = {
    ("int", 9),
    ("float", 9.0)
}
print(values)
'''