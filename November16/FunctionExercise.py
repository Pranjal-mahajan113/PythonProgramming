#1
def greet():
    print("Hello")
greet()    

#2
def add(a,b):
    return a+b
print(add(10,2))

#3
def is_even(num):
    if(num%2==0):
        print("Even")
    else:
        print("Odd")   

print(is_even(6))
  

#4
def greeting(name="Student"):
    print("Hello",name)
greeting()
greeting("kl")

#5
def student(name, course):
    print(name, course)

student("Pranjal", "MCA")

def student(name, course):
    print(name, course)

student(course="MCA", name="Pranjal")

#6
def sqare(*numbers):
    print(numbers)
sqare(10,20,30)   

#7
def detaisls(**student):
    print(student)
detaisls(name="LO",age=23)    

#8
def variable():
    x=90
    print(x)
variable()

#9

#10
def square(num):
    return num *num
print(square(10))
