# =========================================
# Python OOPs: Encapsulation
# =========================================

# In this file, we will learn:
# - Encapsulation
# - Public Variables
# - Protected Variables
# - Private Variables
# - Name Mangling
# - Getters and Setters
# - Data Hiding


# =========================================
# What is Encapsulation?
# =========================================

# Encapsulation means wrapping
# data (variables) and methods
# (functions) together inside a class.

# It also helps restrict direct
# access to important data.

# Main Goals:
# - Protect Data
# - Control Access
# - Hide Internal Details


# =========================================
# Real World Example
# =========================================

# ATM Machine:
# We interact using buttons.

# We cannot directly access:
# - Bank server
# - Account database
# - Internal transaction logic

# This is encapsulation.


# =========================================
# Types of Access in Python
# =========================================

# 1. Public Variables
# 2. Protected Variables
# 3. Private Variables


# =========================================
# Public, Protected & Private Variables
# =========================================

class Student:
    def __init__(self):
        # Public Variable
        self.name = "Rahul"
        # Protected Variable
        self._age = 20
        # Private Variable
        self.__marks = 95


# Creating Object
s1 = Student()

# ----- Accessing Public Variable -----

print("\n----- Accessing Public Variable -----")

print("Student Name :", s1.name)


# ----- Accessing Protected Variable -----

print("\n----- Accessing Protected Variable -----")

print("Student Age :", s1._age)

# Protected variables can still be accessed,
# but it is not recommended outside the class.


# ----- Accessing Private Variable -----

print("\n----- Accessing Private Variable -----")

# This will generate an error
# because private variables
# cannot be accessed directly.

# print(s1.__marks)

# =========================================
# Understanding Name Mangling
# =========================================

# Python internally changes:

# self.__marks

# into:

# self._Student__marks

# This process is called:
# Name Mangling


# ----- Accessing Private Variable Using Name Mangling -----

print("\n----- Accessing Private Variable Using Name Mangling -----")

print("Student Marks :", s1._Student__marks)


# =========================================
# Modifying Private Variables Incorrectly
# =========================================

class Demo:
    def __init__(self):

        self.__value = 100


d1 = Demo()

# This creates a new variable,
# not modify the original private variable.
d1.__value = 500

# ----- Checking Variable Values -----

print("\n----- Checking Variable Values -----")

print("New Variable Value :", d1.__value)
print("Original Private Value :", d1._Demo__value)


