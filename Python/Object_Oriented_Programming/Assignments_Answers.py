# =========================================
# Python OOPs: Assignment Answers
# =========================================

# This file contains solutions for
# OOPs assignment questions.

# Topics Covered:
# - Classes & Objects
# - Constructors
# - Inheritance
# - Encapsulation
# - Polymorphism
# - Abstraction


# =========================================
# Answer 01
# Abstract Class - Remote Control
# =========================================

from abc import ABC, abstractmethod


class RemoteControl(ABC):
    @abstractmethod
    def power_on(self):
        pass

    @abstractmethod
    def power_off(self):
        pass


class TVRemote(RemoteControl):
    def power_on(self):
        print("TV is ON")

    def power_off(self):
        print("TV is OFF")


# ----- Remote Control Example -----

print("\n----- Remote Control Example -----")

remote = TVRemote()

remote.power_on()
remote.power_off()


# =========================================
# Answer 02
# Bank Account System
# =========================================

class BankAccount:
    def __init__(self, holder, balance):
        self.__account_holder = holder
        self.__balance = balance


    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Successfully Deposited : Rs {amount}")
        else:
            print("Invalid Deposit Amount")


    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Successfully Withdrawn : Rs {amount}")
        else:
            print("Insufficient Balance")


    def get_balance(self):
        return self.__balance


# ----- Bank Account Example -----

print("\n----- Bank Account Example -----")

acc = BankAccount("Rahul", 1000)
print("Initial Balance :", acc.get_balance())
acc.deposit(500)
print("Balance After Deposit :", acc.get_balance())
acc.withdraw(300)
print("Balance After Withdrawal :", acc.get_balance())

