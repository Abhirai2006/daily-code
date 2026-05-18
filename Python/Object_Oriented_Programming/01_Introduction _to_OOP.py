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

