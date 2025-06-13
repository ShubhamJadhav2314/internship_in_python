# print("---------------- Addition of 2 numbers program -----------------")
# a = input("Enter first number: ") # input("Prompt String: ")

# # Check type of data
# # type()
# # print(type(a))

# b = input("Enter second number: ")
# # print(type(b))

# # Explicit
# # a = int(a)
# # print("The type of a is ", type(a))

# # b = int(b)
# # print("The type of b is ", type(b))

# # print(a + b)
# # print(int(a) + int(b))
# c = int(a) + int(b)
# # print("The value of c is",c," with type", type(c))
# # print("The value of c is " + str(c))
# # Formatted Strings
# print(f"The value of c is {c} and type of c is {type(c)}")

# int, float, str, list, tuple, dict, set, complex, bool

# Convert one type into another type (Type Conversion)
# Implicit => Auto - Same category
# Explicit => int => float, int => str, str => float...


# Operators
# Used to perform certain operations of variables and values

# Arithmetic
# +, -, *, /, //, %, **

# Assignment
# =, +=, -=, *=, /=,%=, **=

# Comparision
# ==, !=, >, <, >=, <=

# Logical
# and, or, not

# Bitwise
# &, |, ~, ^, >>, <<

# Special
# Identity => is, is not
# Membership => in, not in


# ------------------ Decision Making / Conditional Statements ------------------
# Credit
# Debits
# Balance, Performance

# if, else, elif

# if => specified condition when met, execute the respective block of code
# # Number is positive, entered by user
# # Condition: It should be greater than zero (Comparing)
# num = int(input("Enter a number: "))
# print(num > 0)
# if num > 0:
#     print(f"{num} is positive number")

# # Number is positive or negative, entered by user
# num = int(input("Enter a number: "))
# print(num < 0)
# if (num < 0) == False:
#     print(f"{num} is positive number")
# else:
#     print(f"{num} is negative number")

# Number is positive or negative or zero, entered by user
# NESTED Approach
# num = int(input("Enter a number: "))
# if num > 0:
#     print(f"{num} is positive number")
# else:
#     if num == 0:
#         print(f"{num} is ZERO value")
#     else:
#         print(f"{num} is negative number")

# elif => If you have more than 2 conditions
# num = int(input("Enter a number: "))
# if num > 0:
#     print(f"{num} is positive number")
# elif num < 0:
#     print(f"{num} is negative number")
# else:
#     print(f"{num} is ZERO value")

# task :
a = int(input("Subject 1: "))
b = int(input("Subject 2: "))
c = int(input("Subject 3: "))
d = int(input("Subject 4: "))
e = int(input("Subject 5: "))

if a < 0 or a > 100 or b  < 0 or b > 100 or c < 0 or c > 100 or d < 0 or d > 100 or e < 0 or e > 100:
    print("Invalid marks!")
else:
    fails = 0
    if a < 40: fails += 1
    if b < 40: fails += 1
    if c < 40: fails += 1
    if d < 40: fails += 1
    if e < 40: fails += 1

    if fails > 2:
        print("FAILED")
    elif fails < 0:
        print("ATKT")
    else:
        total = a + b + c + d + e
        per = total / 5
        print("PASSED")
        print("Percentage :", per)
        if per >= 75:
            print("Grade : A")
        elif per >= 60:
            print("Grade : B")
        else:
            print("Grade : C")
