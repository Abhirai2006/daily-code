# =========================================
# Python OOPs: Inheritance Basics
# =========================================

# In this file, we will learn:
# - Inheritance
# - Parent Class
# - Child Class
# - Code Reusability
# - Reusing Methods and Variables


# =========================================
# What is Inheritance?
# =========================================

# Inheritance allows one class
# to acquire the properties and
# behaviors of another class.

# In simple words:
# A child class can reuse code
# from a parent class.

# Benefits:
# - Code Reusability
# - Cleaner Programs
# - Easier Maintenance
# - Better Organization


# =========================================
# Parent and Child Class
# =========================================

# Parent Class:
# The class whose properties are inherited.

# Child Class:
# The class that inherits properties
# from another class.


# =========================================
# Simple Inheritance Example
# =========================================

class Vehicle:
    def start(self):
        print("Vehicle Started")


# Car class inherits from Vehicle class
class Car(Vehicle):
    def drive(self):
        print("Car Can Drive")


# ----- Creating Car Object -----

print("\n----- Creating Car Object -----")

c1 = Car()
# Accessing Parent Class Method
c1.start()
# Accessing Child Class Method
c1.drive()


# =========================================
# Understanding Code Reusability
# =========================================

# Because Car inherited Vehicle,
# we do not need to rewrite
# the start() method again.

# This saves time and reduces code duplication.

# =========================================
# Another Inheritance Example
# =========================================

class Animal:
    def eat(self):
        print("Animal Eats Food")


# Dog inherits from Animal
class Dog(Animal):
    def bark(self):
        print("Dog Barks")


# ----- Creating Dog Object -----

print("\n----- Creating Dog Object -----")

d1 = Dog()
# Accessing Parent Class Method
d1.eat()
# Accessing Child Class Method
d1.bark()


# =========================================
# Inheritance Flow
# =========================================

# Parent Class  --->  Child Class

# Example:
# Vehicle ---> Car
# Animal  ---> Dog

# Child class gets access to:
# - Parent methods
# - Parent variables


# =========================================
# Child Class Can Have Its Own Methods
# =========================================

class Person:
    def show_name(self):
        print("Person Name")

class Student(Person):
    def study(self):
        print("Student is Studying")


# ----- Creating Student Object -----

print("\n----- Creating Student Object -----")

s1 = Student()
# Parent Class Method
s1.show_name()
# Child Class Method
s1.study()


# =========================================
# Advantages of Inheritance
# =========================================

# 1. Code Reusability
# 2. Reduces Duplicate Code
# 3. Easier Maintenance
# 4. Better Program Structure
# 5. Easier Expansion of Programs


# =========================================
# Important Points About Inheritance
# =========================================

# 1. Child class inherits from parent class
# 2. Parent methods can be reused
# 3. Child class can add new methods
# 4. Inheritance improves code organization
# 5. Syntax:
#    class Child(Parent)

