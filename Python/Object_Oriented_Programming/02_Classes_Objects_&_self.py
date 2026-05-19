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


# =========================================
# Understanding the self Keyword
# =========================================

# self represents the current object.

# When we call:
# c1.start()

# Python internally converts it into:
# Car.start(c1)

# Similarly:
# c2.start()

# becomes:
# Car.start(c2)

# This is how Python identifies
# which object is calling the method.


# =========================================
# Example of self Keyword
# =========================================

class Student:

    college = "ABC College"

    def introduce(self):
        print("I study at", self.college)


# Creating Objects
s1 = Student()
s2 = Student()


# ----- Using self Keyword -----

print("\n----- Using self Keyword -----")

s1.introduce()
s2.introduce()


# =========================================
# Object-Specific Data
# =========================================

# Each object can store its own data.

# self helps Python work with
# the correct object data.


# =========================================
# Setting Object Data
# =========================================

class Employee:

    def set_name(self, name):
        self.name = name

    def show_name(self):
        print("Employee Name :", self.name)


# Creating Objects
e1 = Employee()
e2 = Employee()


# Setting Different Names
e1.set_name("Rahul")
e2.set_name("Anjali")


# ----- Displaying Object Data -----

print("\n----- Displaying Object Data -----")

e1.show_name()
e2.show_name()

