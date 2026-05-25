# =========================================
# Python OOPs: Abstraction
# =========================================

# In this file, we will learn:
# - Abstraction
# - Abstract Classes
# - Abstract Methods
# - ABC Module
# - Hiding Internal Implementation


# =========================================
# What is Abstraction?
# =========================================

# Abstraction means:
# Hiding internal implementation details
# and showing only the essential features
# to the user.

# The user only knows:
# - What to do

# The user does not need to know:
# - How it works internally


# =========================================
# Real World Example
# =========================================

# ATM Machine:
# We only:
# - Insert card
# - Enter PIN
# - Withdraw money

# We do not know:
# - Server communication
# - Database operations
# - Security checks

# This is abstraction.


# =========================================
# Simple Example Without Abstraction
# =========================================

def send_email():
    print("Connecting To Server...")
    print("Authenticating User...")
    print("Sending Email...")


# ----- Sending Email -----

print("\n----- Sending Email -----")
send_email()

# User only calls:
# send_email()

# Internal implementation is hidden.


# =========================================
# Abstract Classes in Python
# =========================================

# Python provides abstraction
# using the abc module.

# abc -> Abstract Base Class

# Important Components:
# - ABC
# - abstractmethod

# =========================================
# Importing ABC Module
# =========================================

from abc import ABC, abstractmethod

# =========================================
# Creating an Abstract Class
# =========================================

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

# We cannot create objects
# of abstract classes.

# Example:
# p1 = Payment()   //Error//


# =========================================
# Child Classes Must Implement Methods
# =========================================

class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f"Paid {amount} Using Credit Card")


class UPI(Payment):
    def pay(self, amount):
        print(f"Paid {amount} Using UPI")


# ----- Payment System Example -----

print("\n----- Payment System Example -----")

p1 = CreditCardPayment()
p1.pay(5000)

p2 = UPI()
p2.pay(2000)


# =========================================
# Why Use Abstract Classes?
# =========================================

# Abstract classes help:
# - Define rules
# - Enforce structure
# - Improve consistency

# Every child class must
# implement abstract methods.

# =========================================
# Car System Example
# =========================================

class Car(ABC):
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def accelerate(self):
        pass

    @abstractmethod
    def brake(self):
        pass

# =========================================
# Implementing Abstract Methods
# =========================================

class SUV(Car):
    def start_engine(self):
        print("Engine Started")

    def accelerate(self):
        print("Car Accelerating")

    def brake(self):
        print("Brakes Applied")


# ----- Car System Example -----

print("\n----- Car System Example -----")

car = SUV()

car.start_engine()
car.accelerate()
car.brake()


# =========================================
# Abstraction vs Polymorphism
# =========================================

# Abstraction:
# Focuses on design and rules.

# Polymorphism:
# Focuses on different behaviors.

