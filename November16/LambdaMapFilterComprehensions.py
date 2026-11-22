# 1. Lambda Function
# Lambda ek small anonymous function hota hai, jisme def use nahi karna padta.
square=lambda num :num *num
print(square(5))

# ! lambda arguments: expression

# 2. Lambda with Multiple Arguments
add =lambda a,b:a+b
print(add(10,20))

#3 map() Function
# map() kisi function ko iterable ke har element par apply karta hai.
numbers = [1, 2, 3, 4, 5]

squares = list(map(lambda x: x * x, numbers))

print(squares)

# map() transformed values deta hai. Python 3 mein result ko list dekhne ke liye list() use karte hain.


# 4. filter() Function
# filter() condition ke according elements select karta hai.
numbers=[1,2,3,4,5,6]
even=list(filter(lambda x:x%2==0,numbers))
print(even)

# 5. List Comprehension
# List create karne ka short syntax.

numbers=[1,3,5,8,9]
squares2=[num * num for num in numbers]
print(squares2)

# 6. List Comprehension with Condition
numbers=[1,2,3,5,6,8]
even=[num for num in numbers if num %2==0]
print(even)

# 7. Dictionary Comprehension
numbers = [1, 2, 3, 4]

squares = {num: num * num for num in numbers}

print(squares)

# 8. Set Comprehension
numbers = [1, 2, 2, 3, 3, 4]

unique = {num for num in numbers}

print(unique)