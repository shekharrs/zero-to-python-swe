# File Input/Output

'''
# Create a new file "practice.txt" using python. Add the following data in it
'''
'''
Hi everyone
we are learning File I/O
using Java
I like programming in Java
'''
'''
with open("practice.txt", "w") as f:
    f.write("Hi everyone\nwe are learning File I/O\nusing Java\nI like programming in Java")
    f.close()
'''





'''
# replace Java with Python from practice.txt file

# here the word Java is replace with Python
with open("practice.txt", "r") as f:
    data = f.read()
    new_data = data.replace("Java", "Python")
    print(new_data)

# here the Python is overwrite in the practice.txt file
with open("practice.txt", "w") as f:
    f.write(new_data)
'''




'''
# Search if the word "learning" exists in the file or not

# wrote in a proper Python Function
def check_for_word():
    with open("practice.txt", "r") as f:
        data = f.read()
        if("learning" in data):
            print("Found")
        else:
            print("Not Found")

check_for_word()
'''




'''
# WAF to find in which line of the file does the word "learning" occur first
# Print -1 if word not found

def check_for_line():
    with open("practice.txt", "r") as f:
        word = "learning"
        data = True
        line_no = 1
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
                break
            line_no += 1
        else:
            print(-1)

check_for_line()
'''





'''
# From a file containing numbers separated by comma, print the count of even numbers

count = 0
with open("practice.txt", "r") as f:
    data = f.read()

    nums = data.split(",")
    for val in nums:
        if(int(val) % 2 == 0):
            count += 1
print(count)
'''





'''
# Deleting a File
'''
'''
using the os module

os.remove( filename )
import os
Module (like a code library) is a file written by another programmer that generally has
a functions we can use.
'''
'''

import os
os.remove("tempCodeRunnerFile.py")
'''