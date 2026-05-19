# =========================================
# Python OOPs: Classes, Objects & self
# =========================================

# In this file, we will learn:
# - Classes
# - Objects
# - Methods
# - self keyword
# - How objects work internally


# =========================================
# Understanding Classes and Objects
# =========================================

# A class is a blueprint.

# An object is an instance of a class.

# Example:
# Class  -> Car
# Object -> BMW, Audi, Tesla


# =========================================
# Creating a Simple Class
# =========================================
class Car:

    color = "Red"

    def start(self):
        print("Car Started")


# Creating Objects
c1 = Car()
c2 = Car()


# ----- Accessing Object Variables -----

print("\n----- Accessing Object Variables -----")

print("Car 1 Color :", c1.color)
print("Car 2 Color :", c2.color)


# ----- Calling Object Methods -----

print("\n----- Calling Object Methods -----")

c1.start()
c2.start()

