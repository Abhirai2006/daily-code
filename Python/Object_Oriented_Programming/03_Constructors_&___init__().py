# =========================================
# Python OOPs: Constructors & __init__()
# =========================================

# In this file, we will learn:
# - Constructors
# - __init__() method
# - Object initialization
# - Passing values to objects
# - Constructor overriding


# =========================================
# What is a Constructor?
# =========================================

# A constructor is a special method
# that runs automatically when an object
# is created.

# In Python, the constructor method is:
# __init__()

# Purpose of constructor:
# - Initialize object data
# - Assign values to objects
# - Reduce repetitive code


# =========================================
# Constructor Syntax
# =========================================

class Student:
    def __init__(self):
        print("Constructor Executed")


# ----- Creating Object -----
print("\n----- Creating Object -----")

s1 = Student()

# Constructor runs automatically
# when object is created.


# =========================================
# Initializing Object Data
# =========================================

class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# ----- Creating Employee Objects -----

print("\n----- Creating Employee Objects -----")

e1 = Employee("Rahul", 23)
e2 = Employee("Anjali", 25)

print("Employee 1 Name :", e1.name)
print("Employee 1 Age  :", e1.age)

print()

print("Employee 2 Name :", e2.name)
print("Employee 2 Age  :", e2.age)


# =========================================
# How __init__() Works Internally
# =========================================

# When we write:
# e1 = Employee("Rahul", 23)

# Python internally does:
# Employee.__init__(e1, "Rahul", 23)

# self automatically refers
# to the current object.


# =========================================
# Constructor with Methods
# =========================================

class Car:

    def __init__(self, brand, color):

        self.brand = brand
        self.color = color

    def show_details(self):

        print("Car Brand :", self.brand)
        print("Car Color :", self.color)


# ----- Displaying Car Details -----

print("\n----- Displaying Car Details -----")

c1 = Car("BMW", "Black")
c2 = Car("Audi", "White")

c1.show_details()

print()

c2.show_details()


# =========================================
# Multiple Objects Have Separate Data
# =========================================

# Every object gets its own copy
# of object variables.

# Example:
# c1 has separate data
# c2 has separate data


# =========================================
# Constructor Overriding
# =========================================

# If multiple constructors are created,
# the latest constructor overrides
# the previous one.


class Demo:

    def __init__(self):
        print("First Constructor")

    def __init__(self):
        print("Second Constructor")


# ----- Creating Demo Object -----

print("\n----- Creating Demo Object -----")
d1 = Demo()

# Only the latest constructor executes.


# =========================================
# Advantages of Constructors
# =========================================

# 1. Automatic initialization
# 2. Cleaner code
# 3. Easier object creation
# 4. Reduces repetitive code
# 5. Improves readability


# =========================================
# Important Points About __init__()
# =========================================

# 1. __init__() is called automatically
# 2. Used to initialize object data
# 3. self refers to current object
# 4. Each object gets separate data
# 5. Multiple constructors are not supported like some other languages

