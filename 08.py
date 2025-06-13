# Return statement
# Treating a function as a value

# def add2numbers(a,b):
#     return (a + b)

# def evenOdd(a):
#     if(a % 2 == 0):
#         return True
#     return False

# a = add2numbers(3,4)
# print(a)
# evenOdd(a)


# Python Files
# Directory and Files Management
# "os" module

# import os
# Get current directory
# print(os.getcwd())

# Change directory
# os.chdir("E:\\Code\\Lectures")
# print(os.getcwd())

# List directory and files
# print(os.listdir())

# # Make new directory
# os.mkdir("DEMO")
# print(os.listdir())

# Change the name of directory
# os.rename("DEMO","demo_test")

# Remove directory
# os.rmdir("demo_test")


# CSV
# import csv

# Read CSV file
# with open('demo.csv', 'r') as file:
#     data = csv.reader(file)

#     for line in data:
#         print(line)

# Write to CSV files
# with open('emp.csv', 'a', newline='\n') as file:
#     writer = csv.writer(file)
#     writer.writerow(["ID", "Name", "Email"])
#     writer.writerow([1,"Raju","raju@gmail.com"])
#     writer.writerow([2,"Raju","raju@gmail.com"])
#     writer.writerow([3,"Raju","raju@gmail.com"])


# Exceptions
# try
# except
# finally
# else

# Built-ins
# print(dir(locals()['__builtins__']))

# try:
#     a = 5
#     print(a)

#     # print(a / 0)
#     del a
#     # print(a)
# except NameError:
#     print("Variable not defined error")
# except ZeroDivisionError:
#     print("Cannot divide by zero")
# except:
#     print("Error")
# else:
#     print("Logic implemented successfully")
# finally:
#     print("Progarm Exceuted")

# print("Other codes")

# # practice  :
# import os 
# print(o.getcwd())

# o.chdir("E:\\abc")
# print(o.getcwd())


# print(o.listdir())
# o.mkdir("sonu")
# print(o.listdir())
# # o.makedirs("a/b")

# print(os.listdir())
# os.rename("somu","abc")
# print(os.listdir())

# import csv as c
# # with open ("text.csv","a",newline='\n')as file:
# #     writer=c.writer(file)
# #     writer.writerow(["mnnkl",889])   
# with open("text.csv","r") as f:
#     reader=c.reader(f)
#     for row in reader:
#         print(row)

# exception
# n=10
# try:
#     print("ans :",n/0)
# except:
#     print("error ... ")
# else:
#     print("opreation succesfull .... ")    
# finally:
#     print("end of code")    
