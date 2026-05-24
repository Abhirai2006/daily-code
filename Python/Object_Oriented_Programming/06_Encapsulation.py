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


# =========================================
# Getters and Setters
# =========================================

# Getter:
# Used to read data

# Setter:
# Used to update data with validation


# =========================================
# Getter and Setter Example
# =========================================

class BankAccount:
    def __init__(self):
        self.__balance = 0

    # Getter Method
    def get_balance(self):
        return self.__balance


    # Setter Method
    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print("Invalid Amount")


# Creating Object
b1 = BankAccount()

# ----- Checking Initial Balance -----

print("\n----- Checking Initial Balance -----")

print("Account Balance :", b1.get_balance())


# ----- Updating Balance -----

print("\n----- Updating Balance -----")

b1.set_balance(5000)
print("Updated Balance :", b1.get_balance())


# ----- Trying Invalid Balance -----

print("\n----- Trying Invalid Balance -----")
b1.set_balance(-1000)



# =========================================
# Another Getter and Setter Example
# =========================================

class StudentMarks:
    def __init__(self):
        self.__marks = 0

    # Getter Method
    def get_marks(self):
        return self.__marks


    # Setter Method
    def set_marks(self, value):
        if 0 <= value <= 100:
            self.__marks = value
        else:
            print("Invalid Marks")


# Creating Object
s2 = StudentMarks()

# ----- Updating Student Marks -----

print("\n----- Updating Student Marks -----")

s2.set_marks(85)
print("Student Marks :", s2.get_marks())


# ----- Trying Invalid Marks -----

print("\n----- Trying Invalid Marks -----")
s2.set_marks(150)


# =========================================
# Advantages of Encapsulation
# =========================================

# 1. Better Data Security
# 2. Controlled Access
# 3. Data Hiding
# 4. Cleaner Code
# 5. Easier Maintenance


# =========================================
# Important Points About Encapsulation
# =========================================

# 1. Public Variables:
#    Accessible everywhere

# 2. Protected Variables:
#    Should be accessed carefully

# 3. Private Variables:
#    Cannot be directly accessed

# 4. Name Mangling:
#    Python internally renames private variables

# 5. Getters and Setters:
#    Used to safely access and update data

