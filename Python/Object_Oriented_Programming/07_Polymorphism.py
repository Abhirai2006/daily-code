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


# =========================================
# Runtime Polymorphism
# =========================================

# Method behavior changes
# at runtime depending
# on the object.


class Vehicle:
    def start(self):
        print("Vehicle Starting...")


class Bike(Vehicle):
    def start(self):
        print("Bike Starting...")


class Car(Vehicle):
    def start(self):
        print("Car Starting...")


class ElectricCar(Vehicle):
    def start(self):
        print("Electric Car Starting...")


# ----- Runtime Polymorphism Example -----

print("\n----- Runtime Polymorphism Example -----")

vehicles = [Bike(), Car(), ElectricCar()]
for v in vehicles:
    v.start()


# =========================================
# Why Polymorphism is Useful
# =========================================

# Without polymorphism,
# programs become difficult
# to manage.


# ----- Without Polymorphism -----

print("\n----- Without Polymorphism -----")

vehicle_type = "car"
if vehicle_type == "car":
    print("Car Starting...")
elif vehicle_type == "bike":
    print("Bike Starting...")


# Problems:
# - Difficult to scale
# - Hard to maintain
# - Repetitive code


# ----- With Polymorphism -----

print("\n----- With Polymorphism -----")

obj = Car()
obj.start()


# =========================================
# Notification System Example
# =========================================

class Notification:
    def send(self, recipient, message):
        pass


class Email(Notification):
    def send(self, recipient, message):
        print("Notification Type : Email")
        print(f"Email Sent To {recipient} : {message}")


class SMS(Notification):
    def send(self, recipient, message):
        print("Notification Type : SMS")
        print(f"SMS Sent To {recipient} : {message}")


class PushNotification(Notification):
    def send(self, recipient, message):
        print("Notification Type : Push Notification")
        print(f"Push Notification Sent To {recipient} : {message}")


# ----- Notification System Example -----

print("\n----- Notification System Example -----")

notifications = [
    Email(),
    SMS(),
    PushNotification()
]

recipient = "Rahul"
message = "Welcome To Python OOPs"

for n in notifications:
    n.send(recipient, message)
    print("-" * 40)

# =========================================
# Advantages of Polymorphism
# =========================================

# 1. Cleaner Code
# 2. Better Flexibility
# 3. Easier Maintenance
# 4. Better Scalability
# 5. Reduces Repetitive Code


# =========================================
# Important Points About Polymorphism
# =========================================

# 1. Same method can behave differently
# 2. Improves code flexibility
# 3. Runtime polymorphism uses method overriding
# 4. Common in real-world applications
# 5. Makes programs easier to expand

