# Feature	List	Tuple	Set
# Brackets	[ ]	( )	{ }
# Ordered	Yes	Yes	No
# Change kar sakte?	Yes	No	Yes
# Duplicate values	Allowed	Allowed	Not Allowed
# Indexing	Yes	Yes	No
# Example	[1,2,3]	(1,2,3)	{1,2,3}

#1
programminglanguage=["Python","React","Javascript","Java"]
print(programminglanguage)

#2
print(programminglanguage[0])
print(programminglanguage[3])
#3
print(programminglanguage[0:3])
#4
programminglanguage.append("Golang")
print(programminglanguage)
programminglanguage.insert(1,"TalwindCSS")
print(programminglanguage)
programminglanguage.extend("Css")

#5
programminglanguage.remove("Golang")
print(programminglanguage)

 #6
numbers=[1,4,58,2,5]
numbers.sort()
print(numbers)

#7
number=(1,2,3,4,5)
print(number[0])
print(number[-1])

#8
check={10,10,20,30}
print(check)

#9
check.add(50)
check.discard(100)
print(check)

#10
A={1,2,3,4}
B={3,4,5,6}
print(A.union(B))
print(A.intersection(B))
print(A.difference(B))