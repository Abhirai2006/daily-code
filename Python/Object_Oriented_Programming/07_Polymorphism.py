# =========================================
# Python OOPs: Polymorphism
# =========================================

# In this file, we will learn:
# - Polymorphism
# - Function Polymorphism
# - Method Overriding
# - Runtime Polymorphism
# - Same Method, Different Behavior


# =========================================
# What is Polymorphism?
# =========================================

# Polymorphism means:
# One thing can have many forms.

# Poly  -> Many
# Morph -> Forms

# In Python:
# Same function or method name
# can behave differently
# depending on the object or data.


# =========================================
# Real World Example
# =========================================

# Payment System:
# - UPI Payment
# - Card Payment
# - Cash Payment

# Same action:
# pay()

# Different behavior
# depending on payment type.


# =========================================
# Function Polymorphism
# =========================================

# Same function works differently
# for different data types.


# ----- Using print() Function -----

print("\n----- Using print() Function -----")

print(10)
print("Hello World")


# ----- Using len() Function -----

print("\n----- Using len() Function -----")

print(len("Python"))
print(len([1, 2, 3, 4, 5]))


# =========================================
# Operator Polymorphism
# =========================================

# Same operator behaves differently.


# ----- Using + Operator -----

print("\n----- Using + Operator -----")

print(10 + 20)
print("Hello " + "Python")


# =========================================
# Function Example
# =========================================

def add(a, b):
    return a + b


# ----- Calling add() Function -----

print("\n----- Calling add() Function -----")

print(add(5, 10))
print(add("Hello ", "World"))


# =========================================
# Method Polymorphism
# =========================================

# Same method name
# behaves differently
# in different classes.


# =========================================
# Payment System Example
# =========================================

class Payment:
    def pay(self):
        print("Processing Payment")

class UPI(Payment):
    def pay(self):
        print("Paid Using UPI")

class Card(Payment):
    def pay(self):
        print("Paid Using Card")

class Cash(Payment):
    def pay(self):
        print("Paid Using Cash")


# ----- Payment System Example -----

print("\n----- Payment System Example -----")

payments = [UPI(), Card(), Cash()]
for p in payments:
    p.pay()

