# Python OOP

# Objects & Classes
# Inheritance
# Polymorphism

# Class
# Blueprint of objects
# User defined data type

# class ClassName:
#     # Class Definition

# class Mobile:
#     brand = ""
#     model = ""
#     # variables inside the class are called as attributes

# # Objects
# # Instance of class
# mobile1 = Mobile()
# mobile1.brand = "Samsung"
# mobile1.model = "S25"
# print(f"Brand: {mobile1.brand}. Model: {mobile1.model}")

# mobile2 = Mobile()
# mobile2.brand = "Apple"
# mobile2.model = "iPhone 16"
# print(f"Brand: {mobile2.brand}. Model: {mobile2.model}")


# Python Methods
# function defined inside the class

# class Room:
#     length = 0.0
#     breadth = 0.0

#     # create a function to calculate the area
#     def area(self):
#         print(f"Area of room is {self.length * self.breadth}")


# study_room = Room()
# study_room.length = 10
# study_room.breadth = 8
# print(f"Study room has length of {study_room.length} and breadth of {study_room.breadth}")
# study_room.area()

# main_room = Room()
# main_room.length = 20
# main_room.breadth = 14
# print(f"Main room has length of {main_room.length} and breadth of {main_room.breadth}")
# main_room.area()


# Constructor
# function in a class that is triggered whenever an object in init.
# class Employee:
#     name = ""
#     # def greetEmp(self):
#     #     print(f"Hello {self.name}")

#     # Contructor
#     def __init__(self, name=""):
#         self.name = name
#         print(f"Hello {self.name}")

# emp1 = Employee("John Doe")


# Inheritance
# 2 classes => Parent Class => Child Class

# class ParentClass:
#     pass

# class ChildClass(ParentClass):
#     pass


# class Animal:
#     name = ""
#     def eat(self):
#         print("I can eat")

# class Dog(Animal):
#     def display(self):
#         print(f"My name is {self.name}")

# class Cat(Animal):
#     def display(self):
#         print(f"My name is {self.name}")

# dog1 = Dog()
# dog1.name = "Tyson"
# dog1.display()
# dog1.eat()

# cat1 = Cat()
# cat1.name = "Tom"
# cat1.display()
# cat1.eat()

# Method Overriding
# class Animal:
#     name = ""
#     def eat(self):
#         print("I can eat")

# class Dog(Animal):
#     def display(self):
#         print(f"My name is {self.name}")

#     # override method
#     # def eat(self):
#     #     print(f"{self.name} can eat")

# dog1 = Dog()
# dog1.name = "Tyson"
# dog1.display()
# dog1.eat()

# # Multiple Inheritance
# class Mammal:
#     def mammal_info(self):
#         print("Mammals can give direct birth")

# class WingedMamal:
#     def winged_info(self):
#         print("Winged mammals can fly")

# class Bat(Mammal, WingedMamal):
#     def bat_info(self):
#         print("This is bat class")

# bat = Bat()
# bat.bat_info()
# bat.winged_info()
# bat.mammal_info()

# Multilevel Inheritance
# class Mammal:
#     def mammal_info(self):
#         print("Mammals can give direct birth")

# class WingedMamal(Mammal):
#     def winged_info(self):
#         print("Winged mammals can fly")

# class Bat(WingedMamal):
#     def bat_info(self):
#         print("This is bat class")

# bat = Bat()
# bat.bat_info()
# bat.winged_info()
# bat.mammal_info()

# practice
# class abd object
# class A:
#     n=""
#     g=0
# a=A()
# a.n="shub"    
# a.g=20
# print(a.n)
# print(a.g)

# contructor
# class A:
    # def __init__(self):
    #     print("default constructor")
    # def __init__(self,a,b):
    #     self.a=a
    #     self.b=b
    #     print(f"sum  : {self.a+self.b}")
        
# s=A(20,40)
# v=A()

# inheritence
# class A:
#     def a(self):
#         print("class A")

# class B(A):
#     def b(self):
#         print("class B")  
# class C(B):
#     def c(self):
#         print("class C") 
# z=C()
# z.a()
# z.b()
# z.c()        

# class A:
#     def a(self):
#         print("class A")

# class B:
#     def b(self):
#         print("class B")  
# class C(A,B):
#     def c(self):
#         # print("class C") 
#         print(self)    

# z=C()
# print(z)
# z.a()
# z.b()
# z.c()

# class A:
#     def area(self,side):
#         self.side=side
#         return self.side*self.side
#     def area(self,len,bri):
#         self.len=len
#         self.bri=bri
#         return self.bri*self.len
    
# a=A()    
# print(f"area of square  :{a.area(5,6)}")

# overloading
# class rect:
#     def area(self,l,w):
#         self.l=l
#         self.w=w
#         return self.l*self.w
# class sqr(rect):
#     def area(self, s):
#         self.s=s
#         return self.s*self.s
    
# a=sqr()
# print(f"area of rectangle :{a.area(5)}")
# b=rect()    
# print(f"area of rectangle :{b.area(5,6)}")         

# overriding
# class A:
#     def show(self):
#         print("class A")
# class B(A):
#     def show(self):
#        print("class B")
#        super().show()

# a=B()
# a.show() 
      
