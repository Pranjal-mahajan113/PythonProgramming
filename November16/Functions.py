# 1. What is a Function?
# Function reusable code ka block hota hai jo specific task perform karta hai.
def greet():
    print("hello")
greet()

# 2. Parameters and Arguments
def greet(name):
    print("Hello", name)

greet("Pranjal")
greet("Rahul")
# Parameter: Function definition mein variable (name).
# Argument: Function call ke time actual value ("Pranjal").

# 3. Return Statement
# return function se result wapas deta hai.
def add(a,b):
    return a+b
result = add(10,2)
print(result)

# print() sirf output display karta hai.
# return value wapas deta hai, jise variable mein store ya further use kar sakte hain.


# 4. Default Arguments
# Agar argument pass nahi karte, toh default value use hoti hai.
def greet(name="Student"):
    print("Hello",name)
greet()
greet("pranjal")    

# 5. Positional Arguments
# Values position ke according assign hoti hain.
def student(name,course):
    print(name,course)
student("Pranjal","MCA")
# Order change karoge toh values bhi change ho jayengi.

# 6. Keyword Arguments
# Parameter name specify karke values pass karna.
def student(name, course):
    print(name, course)

student(course="MCA", name="Pranjal")
# Yahan order change karne par bhi correct values milti hain.

# 7. *args
# Jab function mein multiple positional arguments pass karne hon aur unki quantity fixed na ho.
def total(*numbers):
    print(numbers)
total(10,20)    
# *args arguments ko tuple mein collect karta hai.

# 8. **kwargs
# Multiple keyword arguments receive karne ke liye.
def student(**details):
    print(details)

student(name="Pranjal", course="MCA", age=23)
# **kwargs arguments ko dictionary mein collect karta hai.

# 9. Local and Global Variables
# Local variable: Function ke andar create hota hai.
def demo():
    x=10
    print(x)
demo()    

# Global variable: Function ke bahar create hota hai.
x = 100

def demo():
    print(x)

demo()