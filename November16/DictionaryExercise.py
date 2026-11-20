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
    