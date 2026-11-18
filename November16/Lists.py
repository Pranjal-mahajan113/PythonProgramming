# 1. List in Python
# List ek collection hai jisme multiple values store kar sakte hain.
skills = ["Python", "JavaScript", "React", "SQL"]

print(skills)
print(type(skills))
# List ki properties:
# - Ordered: elements ka order maintain hota hai.
# - Mutable: elements change kar sakte hain.
# - Duplicates allowed hain.
# - Different data types store kar sakte hain.

# 2. List Accessing and Indexing
skills = ["Python", "JavaScript", "React", "SQL"]

print(skills[0])   # Python
print(skills[1])   # JavaScript
print(skills[-1])  # 

# 3. List Slicing

numbers = [10, 20, 30, 40, 50]

print(numbers[0:3])
print(numbers[2:])
print(numbers[::-1])

# 4. Adding Elements
skills=["python","sql"]
# print(skills.append("react"))

skills.append("React")
print(skills)
# append() – end mein ek element add karta hai.

skills.insert(1, "SQL")
print(skills)
# insert() – specified index par element add karta hai.

# extend() – multiple elements add karta hai.
skills.extend(["HTML", "CSS"])
print(skills)

# 5. Removing Elements
skills = ["Python", "JavaScript", "React", "SQL"]

skills.remove("React")
print(skills)
# remove() – value remove karta hai.



# pop() – index se element remove karta hai; default last element.



# clear() – saare elements remove karta hai.
# 6. Updating and Other List Methods
numbers = [10, 20, 30]

numbers[1] = 100
print(numbers)

# sort() – ascending order mein sort karta hai.



# reverse() – current order reverse karta hai.



# len() – elements count karta hai