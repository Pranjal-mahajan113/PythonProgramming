# 1. Dictionary kya hai?
# Dictionary data ko key:value pairs mein store karti hai.
student = {
    "name": "Pranjal",
    "course": "MCA",
    "college": "GTU",
    "age": 23
}

print(student)
print(type(student))
# 2. Accessing Dictionary Values
student = {
    "name": "Pranjal",
    "course": "MCA"
}

print(student["name"])
print(student["course"])

# Another method: get()
print(student.get("name"))
print(student.get("age"))

#get() missing key par default None deta hai, jabki student["age"] error dega.
 
#3. Adding and Updating Elements
