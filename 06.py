# tuple
# tuple=(2,3,4,5,6)
# print("tuple :",tuple)
# v=tuple.count(3)
# print(v)
# s=tuple.index(2)
# print(s)
# task

# # dictionry
# dict={"a":10,"b":40}
# print(dict)
# dict.update({"c":67})
# print(dict)
# print(dict.values())
# print(dict.items())
# print(dict.keys())
# x=dict.copy()
# print(x)
# dict.pop("a",10)
# print(dict)
# dict.clear()
# print(dict)
# Tuple
# Data Structure
# Multilpe values in a single variable
# Similar to array (dynamic array) => supports multiple datatype value assignment

# Denoted by ()
# numbers = (10,20,30,40,50,60)
# print(numbers)
# print(type(numbers))

# emp = ("John", 32, "Software Developer", True)
# print(emp)

# Ordered => They maintain the order of elements
# Immutable => Items cannot be changed after creation
# Duplication

# Access an item from tuple
# #           0           1           2       3           4
# brands = ("Apple", "Microsoft", "Google", "Amazon", "Oracle")
# #           -5          -4          -3          -2      -1
# print(brands[2])
# print(brands[-3])

# # Slicing => accesing a portion of tuple
# print(brands[1:4])
# print(brands[:3])
# print(brands[2:])

# Add a new item to tuple
#           0           1           2       3           4
# brands = ("Apple", "Microsoft", "Google", "Amazon", "Oracle")
#           -5          -4          -3          -2      -1

# Concatinating tuple with tuple
# brands += ("Meta",)
# print(brands)

# Changing existing elements in tuple
# brands[2] = "Alphabet"
# print(brands)

# Iterate over a tuple
# numbers = (1,2,3,4,5,6,7,8,9,10)
# sum = 0
# for num in numbers:
#     sum += num
# print(sum)

# Tuple to List
# numbers = (1,2,3,4,5,6,7,8,9,10)
# print(numbers)
# numbers = list(numbers)
# print(numbers)
# numbers.append(1000)
# print(numbers)
# numbers = tuple(numbers)
# print(numbers)


# Dictionary
# Collection of items or elements
# key: value pair (mapping type)
# {}

# emp = ("John", 32, "Software Developer", True)
# emp = {
#     "name": "John",
#     "age": 32,
#     "position": "Software Developer",
#     "isTeamLead": True
# }
# print(emp)

# Accessing a value from dictionary
# Does not supports indexing
# Values are accessed with the help of keys
# print(emp["position"])

# # Add new data to a dictionary
# emp = {
#     "name": "John",
#     "age": 32,
#     "position": "Software Developer",
#     "isTeamLead": True
# }
# emp["salary"] = 3.5
# print(emp)
# # Update an existing value in dictionary
# emp["salary"] = 4.9
# print(emp)

# # Remove an element
# del emp['salary']
# print(emp)


# Methods
# emp = {
#     "name": "John",
#     "age": 32,
#     "position": "Software Developer",
#     "isTeamLead": True
# }
# values()
# print("------------ Values ------------")
# print(emp.values())
# for v in emp.values():
#     print(v)

# # keys()
# print("------------ Keys ------------")
# print(emp.keys())
# for k in emp.keys():
#     print(k)

# items()
# print("------------ Items ------------")
# print(emp.items())
# for i in emp.items():
#     print(f"The '{i[0]}' key has the value of '{i[1]}'")
# for k,v in emp.items():
#     print(f"The '{k}' key has the value of '{v}'")

# update()
# emp.update({'salary': 3.5})
# print(emp)
# emp.update({'salary': 6.9})
# print(emp)

# PREPARE A DATA OF EMPLOYEE => ID, NAME AND EMAIL BY USER INPUTS AND DISPLAY THEM
# List of dictionaries

# Ask the number of employees
# employees = []
# size = int(input("Enter number of employees: "))

# for i in range(1, size + 1):
#     print(f"========== Employee {i} details ==========")
#     eid = input("Enter employee id: ")
#     name = input("Enter employee name: ")
#     email = input("Enter employee email: ")
#     employees.append({
#         'id' : eid,
#         'name' : name.title(),
#         'email' : email.lower(),
#     })

# for emp in employees:
    # Each "emp" is a dictionary
    # for key, value in emp.items():
    #     print(f"{key.title()}: {value}")
    # print("---------------------------")

# Enter subject: English
# Enter marks for English: 39
# ....

# English => 39 => FAILED
# task
dict={}
n=int(input("how many subject  :"))
for i in range(0,n):
    a=input(f"enter the subject :")
    b=int(input(f"enter the mark :"))
    if b>100 or b<0:
        print("invalid marks ")
    dict.update({a:b})
print(dict)

fails=0
for m in dict.values():
    if m<40:
        fails+=1

if fails >2:
    print("failed .. ")  
elif fails >0:
    print("atkt .. ")       
else:
    print("passsed .. ")
    sum=sum(dict.values())
    print("total :",sum)  
    per=sum/n
    print("per :",per)  
    if per >75:
        print("grade :A")
    elif per >60:
        print("grade :B") 
    else:
        print("greade :C")




