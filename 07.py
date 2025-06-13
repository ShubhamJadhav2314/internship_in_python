# Sets
# Multilpe values in a single variable
# Unique data
# {}
# Mutable
# Unordered => Do not have any index positioning

# a = [1,2,3,4,1,4,5,1,2,1,3,4,5,6,7,8]
# print(a)

# a = {1,2,3,4,1,4,5,1,2,1,3,4,5,6,7,8}
# print(a)
# print(type(a))

# Create an empty set
# b = set()
# print(b)
# print(type(b))

# Add or update set items
# add() => Only one element
# a = {100,200,300}
# print(a)
# a.add(400)
# print(a)

# update => add a collection object to set
# a = {'Apple', "Google"}
# print(a)
# b = ("Microsoft", "Oracle", "Meta", "Amazon")
# a.update(b)
# print(a)


# Remove an element
# discard()
# b = {"Microsoft", "Oracle", "Meta", "Amazon"}
# print(b)
# b.discard("Oracle")
# print(b)

# Loops to iterate over set
# b = {"Microsoft", "Oracle", "Meta", "Amazon"}
# for i in b:
#     print(i)


# Set Operations
# Union => includes all elements from both sets
# setA = {100,300,500}
# setB = {200,400,600}
# print(f"Union of {setA} and {setB} is {setA | setB}")
# print(f"Union of {setA} and {setB} is {setA.union(setB)}")

# Intersection => includes common elements from both sets
# setA = {100,300,500,200}
# setB = {200,400,600,500}
# print(f"Intersection of {setA} and {setB} is {setA & setB}")
# print(f"Intersection of {setA} and {setB} is {setA.intersection(setB)}")

# Difference => excludes common elements from both sets and elements from one of the other set too
# setA = {100,300,500,200}
# setB = {200,400,600,500}
# print(f"Difference of {setA} and {setB} is {setA - setB}")
# print(f"Difference of {setB} and {setA} is {setB.difference(setA)}")

# # Symmetric Difference => excludes common elements from both sets
# # setA = {100,300,500,200}
# # setB = {200,400,600,500}
# # print(f"Symmetric Difference of {setA} and {setB} is {setA ^ setB}")
# # print(f"Symmetric Difference of {setA} and {setB} is {setA.symmetric_difference(setB)}")



# # --------------------------------------------------------------------------------------------
# # Functions

# # Create a function
# # def nameOfTheFunction(arguments):
# #     Statements

# # def greet():
# #     print("Hello World")

# # # Call the function
# # greet()


# # Addition of 2 numbers
# # def add2Nos():
# #     a = int(input("Enter number for a: "))
# #     b = int(input("Enter number for b: "))
# #     print(f"Addition of {a} and {b} is {a + b}")

# # add2Nos()
# # add2Nos()
# # add2Nos()



# # Arguments => inputs given to the function
# # def greet(user):
# #     print(f"Hello! {user}")

# # users = ['Aakash', "Shyam", "Raju"]
# # for u in users:
# #     greet(u)

# # def add2Numbers(num1, num2):
# #     print(f"Addition of {num1} and {num2} is {num1 + num2}")

# # numbers = [(1,3),(3,6),(7,5)]
# # for n in numbers:
# #     add2Numbers(n[0], n[1])
# setB = {200,400,600,500}
# print(sum(setB))
# print(max(setB))
# print(min(setB))
# print(len(setB))
# setB.add(10)
# print(setB)
# setB.remove(10)
# print(setB)
# setB.discard(200)
# print(setB)
# a={23,3,44}
# setB.update(a)
# print(setB)
# s=setB.copy()
# print(s)
# print(s.difference(a))
# print(s.symmetric_difference(a))
# print(s.issubset(a))
# print(s.difference_update(a))
# print(s.isdisjoint(a))
# print(s.issuperset(a))
# s.clear()
# print(s)
