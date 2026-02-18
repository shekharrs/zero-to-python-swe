# Lists & Tuples

'''
#WAP to ask the user to enter names of their 3 favorite movies & store them in a list
movies = []

user1 = input("Enter your first movie: ")
user2 = input("Enter your second movie: ")
user3 = input("Enter your third movie: ")

movies.append(user1)
movies.append(user2)
movies.append(user3)

print(movies)
'''



'''
#WAP to check if a list contains a palindrome of elements.
list1 = [1,2,1]
list2 = [1,2,3]

copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("Palidrome")
else:
    print("Not Palindrome")
'''



'''
#WAP to count the number of students with the "A" grade in the following tuple
grades = ("C", "D", "A", "A", "B", "B", "A")
print(grades.count("A"))
'''



'''
#Store the above values in a list & sort them from "A" to "D"
list = ["C", "D", "A", "A", "B", "B", "A"]
list.sort()
print(list)
'''