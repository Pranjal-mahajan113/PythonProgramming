# #1. Module kya hota hai?
# Python ki ek .py file jisme functions, variables aur classes hote hain, use Module kehte hain. 
#calculator.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
# main.py
import calculator

print(calculator.add(10, 5))
print(calculator.subtract(10, 5))


# 2. Import ke different methods
# Method 1 – Complete module import