# 7. Important String Methods
# A. upper()
# Text ko uppercase mein convert karta hai.
name="Pranjal"
print(name.upper())
print(name)
# B. lower()
# Text ko lowercase mein convert karta hai.
name = "PYTHON"
print(name.lower())
# C. strip()
# Starting aur ending ke extra whitespace remove karta hai.
name=" Pranjal "
print(name.strip())
# D. replace()
# Ek text ko doosre text se replace karta hai.
message="Hello Python"
print(message.replace("Python","Odoo"))
# E. split()
# String ko list mein convert karta hai, separator ke basis par.
skills = "Python,JavaScript,React"

print(skills.split(","))
# Important concept: Python strings immutable hoti hain. Matlab existing string ko directly change nahi kar sakte. 
# Methods generally modified string return karte hain.

# 8. String Concatenation
# Concatenation ka matlab two or more strings ko combine karna.

# + operator use hota hai.
first_name = "Pranjal"
last_name = "Mahajan"

full_name = first_name + " " + last_name

print(full_name)
# Important: String aur integer ko directly concatenate nahi kar sakte.

age = 23
print("Age: " + str(age))
# ! str() integer ko string mein convert karta hai.

# ? 9. String Formatting – f-strings
# f-string Python mein dynamic values ko string ke andar 
# insert karne ka easy aur readable method hai.
name="Pranjal"
age=23
print(f"my name is{name} and my age is {age}")