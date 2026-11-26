# #1. Module kya hota hai?
# Python ki ek .py file jisme functions, variables aur classes hote hain, use Module kehte hain. 
#calculator.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
# main.py
# import calculator

# print(calculator.add(10, 5))
# print(calculator.subtract(10, 5))


# 2. Import ke different methods
# Method 1 – Complete module import
import math

print(math.sqrt(25))

# Method 2 – Specific function import
from math import sqrt

print(sqrt(25))

# Method 3 – Alias
import math as m

print(m.sqrt(25))

# Method 4 – Import everything
from math import *

print(sqrt(25))
print(pi)

# 3. Built-in Modules
# Python mein already bahut saare modules available hain.
# A. Math Module
# Mathematical operations ke liye.
import math

print(math.sqrt(64))
print(math.ceil(4.2))
print(math.floor(4.8))
print(math.factorial(5))
print(math.pi)

# B. Random Module
# Random values generate karne ke liye.
import random
print(random.randint(1,10))
print(random.random())
print(random.choice(["Apple","Mango","Banana"]))

# C. Datetime Module
# Date aur time ke liye. Odoo mein dates, deadlines, orders aur appointments handle karne mein useful hai
import datetime

today = datetime.date.today()
print(today)

current_time = datetime.datetime.now()
print(current_time)

# D. OS Module Operating system ke saath kaam karne ke liye.
import os
print(os.getcwd())
# getcwd() current working directory batata hai.


import os
print(os.listdir())
# listdir() current folder ke files aur folders dikhata hai.

# E. JSON Module
# JSON ka use data exchange karne ke liye hota hai. APIs aur Odoo integrations mein bahut useful hai.
# Python dictionary ko JSON string mein convert karna


import json
student={
    "name":"Pranjal",
    "age":23
}
data=json.dumps(student)
print(data)
print(type(data))

import json

data = '{"name": "Pranjal", "age": 22}'

student = json.loads(data)

print(student["name"])
print(type(student))

# json.dumps() → Python object to JSON string.
# json.loads() → JSON string to Python object.

# 4. Package kya hota hai?
# Package ek folder hota hai jisme multiple Python modules organize hote hain.
#! Example
# my_package/
#     __init__.py
#     calculator.py
#     greetings.py
# main.py

#! calculator.py
# def add(a, b):
#     return a + b

# !greetings.py
# def hello():
#     print("Hello!")

#! main.py
# from my_package import calculator
# from my_package import greetings

# print(calculator.add(10, 20))
# greetings.hello()
