# =========================================
# Python OOPs: Introduction to OOP
# =========================================

# OOP -> Object Oriented Programming

# Object Oriented Programming is a programming paradigm
# where programs are designed using objects and classes.

# OOP helps in:
# - Better code organization
# - Easier maintenance
# - Code reusability
# - Scalability for large projects


# =========================================
# Why Do We Need OOP?
# =========================================

# Imagine building a large e-commerce application
# without proper structure.

# Problems:
# - Difficult to manage
# - Difficult to debug
# - Difficult to expand
# - Code becomes messy

# OOP helps organize code logically,
# similar to real-world objects and behavior.


# =========================================
# Real World Examples of OOP
# =========================================

# Car Object:
# - color
# - brand
# - speed

# Student Object:
# - name
# - age
# - marks

# Bank Account Object:
# - account_number
# - balance
# - deposit()
# - withdraw()


# =========================================
# What is a Class?
# =========================================

# A class is a blueprint or template.

# It defines:
# - What data an object will have
# - What actions an object can perform


# =========================================
# Simple Class Example
# =========================================

class Car:

    # Class Variable
    color = "Red"

    # Method
    def start():
        print("Car Started")


# ----- Accessing Class Variable -----

print("\n----- Accessing Class Variable -----")

print("Car Color :", Car.color)


# ----- Calling Class Method -----

print("\n----- Calling Class Method -----")

Car.start()


# =========================================
# What is an Object?
# =========================================

# An object is an instance of a class.

# If class = blueprint
# Then object = real thing created from blueprint

# Example:
# Blueprint -> Car Design
# Object -> Actual Car


# =========================================
# Creating Objects
# =========================================

class Student:

    college = "ABC College"

    def study():
        print("Student is studying")


# Creating Objects
s1 = Student()
s2 = Student()


# ----- Accessing Object Variables -----

print("\n----- Accessing Object Variables -----")

print("Student 1 College :", s1.college)
print("Student 2 College :", s2.college)


# ----- Calling Object Methods -----

print("\n----- Calling Object Methods -----")

print("\nOutput From s1.study()")
s1.study()

print("\nOutput From s2.study()")
s2.study()

