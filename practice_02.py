# Strings & Conditional Statements

'''
#WAP to input user’s first name & print its length.
firstName = input("Enter your name: ")
print("Length of your name:", len(firstName))
'''




'''
#WAP to find the occurrence of ‘$’ in a String.
str = "Hey, I am $ are you fine $!"
print(str.count("$"))
'''




'''
# voterAgeLimit = int(input("Enter your age: "))

if(voterAgeLimit >= 18):
    print("You are eligible to vote.")
else:
    print("Oops! you are not eligible to vote.")
'''



'''
marks = int(input("Enter your marks: "))

if(marks >= 90):
    print("Grade A")
elif(marks >= 80 and marks < 90):
    print("Grade B")
elif(marks >= 70 and marks < 80):
    print("Grade C")
elif(marks >= 60 and marks < 70):
    print("Grade D")
else:
    print("Padh le bhai!")
'''



'''
# WAP to check if a number entered by the user is odd or even.

num = int(input("Enter a number: "))

if(num % 2 == 0):
    print("Even")
else:
    print("Odd")
'''



'''
#WAP to find the greatest of 3 numbers entered by the user.
num1 = int(input("Enter a first number: "))
num2 = int(input("Enter a second number: "))
num3 = int(input("Enter a third number: "))
num4 = int(input("Enter a fourth number: "))

if(num1 >= num2):
    print(num1, "is greater")
elif(num2 >= num3):
    print(num2, "is greater")
elif(num3 >= num4):
    print(num3, "is greater")
else:
    print(num4, "is greater")
'''




'''
#WAP to check if a number is a multiple of 7 or not
num = int(input("Enter a number: "))

if(num% 7 == 0):
    print(num, "is a multiple of 7")
else:
    print(num, "is not a multiple of 7")
'''