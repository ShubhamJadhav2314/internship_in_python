# # Mutiple conditions

# # Write a Python program that takes marks of 5 subjects from the user (as integers). Each mark must be between 0 and 100 inclusive. After validating all 5 inputs, the program should calculate the total and percentage of the marks.
# # The passing mark for each subject is 40.
# # If more than 2 subjects have marks less than 40, the student is FAILED.
# # If only 1 or 2 subjects are below 40, the result is ATKT (Allowed to Keep Term) and the percentage should not be displayed.
# # If all subjects have 40 or more, then:
# # Calculate the percentage and assign a grade:
# # A Grade: percentage ≥ 75
# # B Grade: percentage ≥ 60 and < 75
# # C Grade: percentage ≥ 40 and < 60
# # Use only if, elif, and else statements.

# sub1 = int(input("Subject 1: "))
# sub2 = int(input("Subject 2: "))
# sub3 = int(input("Subject 3: "))
# sub4 = int(input("Subject 4: "))
# sub5 = int(input("Subject 5: "))

# # Check if all marks are valid
# # validFlag = True
# # if (sub1 < 0) or (sub1 > 100):
# #     validFlag = False
# # if(sub2 < 0) or (sub2 > 100):
# #     validFlag = False

# # if (validFlag):
# #     print("The marks are valid")
# # else:
# #     print("Invalid marks.")

# if(0 <= sub1 <= 100) and (0 <= sub2 <= 100) and (0 <= sub3 <= 100) and (0 <= sub4 <= 100) and (0 <= sub5 <= 100):
#     # Calculate failed subjects
#     failedSubjects = 0
#     if sub1 < 40:
#         # failedSubjects = failedSubjects + 1
#         failedSubjects += 1
#     if sub2 < 40:
#         failedSubjects += 1
#     if sub3 < 40:
#         failedSubjects += 1
#     if sub4 < 40:
#         failedSubjects += 1
#     if sub5 < 40:
#         failedSubjects += 1

#     # Make result logic on the basis of failed subjects
#     total = sub1 + sub2 + sub3 + sub4 + sub5
#     print(f"Total: {total}")
#     if(failedSubjects > 2):
#         print("Result: FAILED")
#     elif(failedSubjects <= 2 and failedSubjects > 0):
#         print("Result: ATKT")
#     else:
#         print("Result: PASS")
#         percentage = total / 5
#         print(f"Percentage: {percentage}%")

#         if(percentage >= 75):
#             print("Grade: A")
#         elif (percentage >= 60):
#             print("Grade: B")
#         else:
#             print("Grade: C")
# else:
#     print("Invalid marks entered.")



# Strings
# String is a collection of characters
# "hello" => "h","e","l","l","o"

# '' or "" or """"""
# string1 = "Hello Python"
# string2 = 'Hello Python 2'
# string3 = """Hello Python 3"""


# Accessing string characters
# greet = "Hello" # => Here "H" is on index 0.
# print(greet[1])
# # Access using negative indexing
# # Negative indexing starts from -1
# print(greet[-1])
# print(greet[-4])


# Python strings are immutable (characters in strings are unchangeable)
# greet = "HELLO"
# # greet[1] = "e"
# greet = "HeLLO"
# print(greet)


# Multiline strings
# message = "This is the message for you." \
# "And the message goes something like this!"
# message = """This is the message for you.
# And the message goes something like this:"""
# print(message)

# Count the number of characters in string
# len()
# lenOfMessage = len(message)
# print(lenOfMessage)


# Membership (in, not in)
# greet = "Python Program"
# print("l" in greet)
# print("Python" in greet)
# print("b" not in greet)


# Methods
message = "This is the message for you."

# upper()
print(message.upper())
# lower()
print(message.lower())
# title()
print(message.title())
# replace()
print(message.replace("message", "msg"))
# isnumeric()
x = input("Enter value for x: ")
y = input("Enter value for y: ")
if(x.isnumeric() and y.isnumeric()):
    print(int(x) + int(y))
else:
    print("Invalid numeric values")