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

