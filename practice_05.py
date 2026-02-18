# Loops


# While loop
'''
# Print numbers from 1 to 100
i = 1
while i <= 100:
    print(i)
    i += 1
'''



'''
# Print numbers from 100 to 1
i = 100
while i >= 1:
    print(i)
    i -= 1
'''



'''
# Print the multiplication table of a number n
n = int(input("Enter a number: "))
i = 1
while i <= 10:
    print(n * i)
    i += 1
'''



'''
# Print the elements of the following list using a loop
# [1,4,9,16,25,36,49,64,81,100]

list = [1,4,9,16,25,36,49,64,81,100]
i = 0
while i < len(list):
    print(list[i])
    i += 1
'''



'''
# Search for a number x in this tuple using loop:
# [1, 4, 9, 16, 25, 36, 49, 64, 81,100]

tuple = (1, 4, 9, 16, 25, 36, 49, 64, 81,100)

x = int(input("Enter a number: "))

i = 0

while i < len(tuple):
    if(tuple[i] == x):
        print("Found:", x)
    i += 1
'''



# For loop
'''
# Print the elements of the following list using a loop
# [1, 4, 9, 16, 25, 36, 49, 64, 81,100]

list = [1, 4, 9, 16, 25, 36, 49, 64, 81,100]

for i in list:
    print(i)
'''



'''
# Search for a number x in this tuple using loop:
# [1, 4, 9, 16, 25, 36, 49, 64, 81,100]

tuple = (1,4,9,16,25,36,49,64,81,100)

x = int(input("Enter a number: "))

idx = 0

for i in tuple:
    if(i == x):
        print("Number found at idx:", idx)
        break
    idx += 1
else:
    print("Number not found")
'''



# using for & range()
'''
# Print numbers from 1 to 100
for i in range(1, 101):
    print(i)
'''



'''
# Print numbers from 100 to 1
for i in range(100, 0, -1):
    print(i)
'''



'''
# Print the multiplication table of a number n
n = int(input("Enter a number: "))

for i in range(n, n * 11, n):
    print(i)
'''




'''
# WAP to find the sum of first n numbers (using while loop)

n = int(input("Enter a number: "))

sum = 0
i = 1
while i <= n:
    sum += i
    i += 1
print("total sum:", sum)
'''



'''
# WAP to find the factorial of first n number (using for loop)
n = int(input("Enter a number: "))

fact = 1
for i in range(1, n+1):
    fact *= i
print("Factorial:", fact)
'''



'''
# pass
for el in range(10):
    pass
print("hee")
'''