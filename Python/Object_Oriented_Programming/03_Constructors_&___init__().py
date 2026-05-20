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

