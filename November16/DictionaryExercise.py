student ={
    "name":"pranjal",
    "age":23,
    "course":"MCA",
    "college":"KDK"
}
print(student)

#2
print(student["name"])
print(student["course"])

#3
print(student.get("age"))

#4
student["city"]="Hariyana"

#5
student["course"]="B.tech"

#6
# student.pop()

#7
print(student.keys())
print(student.values())
print(student.items())

#8
for keys in student:
    print(keys)

students ={
    "student1":{
        "name":"pranjal",
        "course":"MCA"
    },
    "student2":{
        "name":"Rahul",
        "course":"BCA"
    }
}    
print(students["student2"]["name"])
# Dictionary comprehension short syntax se dictionary create karne ka method hai.
numbers=[1,2,3,4,5]
squares={num:num*num for num in numbers}
print(squares)