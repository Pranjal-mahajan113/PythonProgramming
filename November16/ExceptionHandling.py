# 1. What is an Exception?
# Program execute hote time koi error aata hai aur normal execution ruk jata hai, toh use exception kehte hain.
# a=10
# b=0
# print(a/b)
# Output: ZeroDivisionError
# Python zero se divide nahi kar sakta.

# 2. try and except
# Error handle karne ke liye try aur except use karte hain
try:
    a=10
    b=0
    print(a/b)
except:
    print("Something went wrong")    


# 3. Specific Exception Handling
# Har error ke liye specific exception handle kar sakte hain.    
# try:
#     num=int(input("Enter number:"))
#     print(num)
# except ValueError:    
#     print("enter valid number")

# Exception	Meaning
# ValueError	Invalid value
# TypeError	Wrong data type operation
# ZeroDivisionError	Division by zero
# IndexError	Invalid list index
# KeyError	Dictionary key missing
# NameError	Variable not defined
# FileNotFoundError	File not found

# 4. Multiple except Blocks
# Ek try ke saath multiple except blocks use kar sakte hain.
# try:
#     a=int(input("Enter first number"))
#     b=int(input("Enter second number"))
# except ValueError:try



#1
try:
    a=10
    b=0
    print(a/b)
except:
    print("Not valid")

#2
try:
    a=int(input("Enter valid number"))
except ValueError:
    print("enter number only")    

#3 Two numbers division + error handling
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print(a/b)
except ValueError:
    print("Enter numbers only")    
except ZeroDivisionError:
    print("cannot divisible by zero")    


#4. List mein invalid index handle karo
try:
    numbers=[1,2,3]
    print(numbers[5])
except IndexError:
    print("Index does not exist")    

#5Dictionary mein missing key handle karo
try:
    students={"name":"Pranjal","age":23}
    print(students["marks"])
except KeyError:
    print("Key is not found")    

#6. Try-Except-Else
try:
    num=int(input("Enter number is : "))
except ValueError:
    print("Ivalid input")    

else:
    print("Your number is: ",num)    


#7. Finally
try:
    num = int(input("Enter number: "))
    print(num)

except ValueError:
    print("Invalid input")

finally:
    print("Program completed")

#8. Raise Exception
age = int(input("Enter your age: "))

if age < 18:
    raise ValueError("Age must be 18 or above")

print("You are eligible")

#9. Exception message using as e
try:
    num = int("hello")

except ValueError as e:
    print("Error:", e)

