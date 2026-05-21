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

