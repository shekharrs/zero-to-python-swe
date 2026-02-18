# Functions & Recursion


# Functions
'''
# WAF to print the length of a list. ( list is the parameter)

cities = ["Atlanta", "Baltimore", "Chicago", "Denver", "Los Angeles"]
country = ["India", "New Zealand", "Germany"]

def print_len(list):
    print(len(list))
    return

print_len(cities)
print_len(country)
'''



'''
# WAF to print the elements of a list in a single line. ( list is the parameter)
heros = ["spider-man", "thor", "hulk", "iron-man", "captain-america", "black-panther"]

def len_list(list):
    for i in list:
        print(i, end=" ")
    return

len_list(heros)
'''



'''
# WAF to find the factorial of n (n is the parameter)

def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
    print(fact)
    return

factorial(5)
'''



'''
# WAF to convert USD to INR

def usd_convt(usd):
    inr = usd * 88
    print(usd, "USD = ", inr, "INR")
    return

usd_convt(22)
usd_convt(2)
'''



'''
# WAF to check the given number is odd or even

n = int(input("Enter a number: "))

def odd_even(n):
    if n % 2 != 0:
        print(n,"is Odd")
    else:
        print(n, "is Even")
    return

odd_even(n)
'''






# Recursion
'''
# recursive function
def show(n):
    if(n == 0):
        return
    print(n)
    show(n-1) 

show(5)
'''



'''
# Write a recursive function to calculte the sum of first n natural numbers
n = int(input("Enter a number: "))

def sum_n(n):
    if(n == 0):
        return 0
    return n + sum_n(n-1)

print(sum_n(n))
'''



'''
# Write a recursive function to print all elements in a list
# Hint: use list & index as parameters

list = input("Enter a list: ").split(" ")

def print_list(list, idx=0):
    if(idx == len(list)):
        return
    print(list[idx])
    print_list(list, idx+1)
    return

print_list(list)
'''