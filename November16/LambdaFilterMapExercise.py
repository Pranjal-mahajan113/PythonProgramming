square =lambda x:x*x
print(square(3))

#2
add=lambda a,b:a+b
print(add(10,20))

#3
numbers=[1,2,3,4,5,6]
result=list(map(lambda num:num*num,numbers))
print(result)

#4
numbers=[1,2,3,4]
double=list(map(lambda x:x*2,numbers))
print(double)

#5
numbers=[1,2,3,4]
even=list(filter(lambda x:x%2==0,numbers))
print(even)

#6
numbers=[1,2,3,4,11]
even=list(filter(lambda x:x>10,numbers))
print(even)

#7
numbers = [1, 2, 3, 4, 5]

squares = [num * num for num in numbers]

print(squares)

#8
even=[num for num in range(1,21) if num %2==0]
print(even)

#9
numberscube=[1,2,3,4]
cubes={num:num ** 3 for num in numberscube}
print(cubes)

#10
numbersset=[1,1,1,3,4,4,6]
unique={num for num in numbersset}
print(unique)



numberslist=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
squarelist=[num*num for num in numberslist]
print(squarelist)

odd=[num for num in range(1,31) if num%2!=0]
print(odd)

numbersc=[2,3,4,5]

cubes={num:num ** 3 for num in numbersc}
print(cubes)