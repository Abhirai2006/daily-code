# =========================================
# Python OOPs: Types of Inheritance
# =========================================

# In this file, we will learn:
# - Single Inheritance
# - Multiple Inheritance
# - Multilevel Inheritance
# - Hierarchical Inheritance
# - Hybrid Inheritance


#  super() Function
#  MRO (Method Resolution Order)


# =========================================
# 1. Single Inheritance
# =========================================

# One child class inherits
# from one parent class.


class Animal:
    def eat(self):
        print("Animal Eats Food")

class Dog(Animal):
    def bark(self):
        print("Dog Barks")


# ----- Single Inheritance Example -----

print("\n----- Single Inheritance Example -----")
d1 = Dog()
d1.eat()
d1.bark()
