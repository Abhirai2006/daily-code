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



# =========================================
# 2. Multiple Inheritance
# =========================================

# One child class inherits
# from multiple parent classes.

class Father:
    def skills(self):
        print("Driving")

class Mother:
    def skills(self):
        print("Cooking")


class Child(Father, Mother):
    pass


# ----- Multiple Inheritance Example -----

print("\n----- Multiple Inheritance Example -----")

c1 = Child()
c1.skills()


# =========================================
# 3. Multilevel Inheritance
# =========================================

# A class inherits from another class,
# and another class inherits from it.

# Grandparent -> Parent -> Child

class Grandparent:
    def show_grandparent(self):
        print("I am Grandparent")

class Parent(Grandparent):
    def show_parent(self):
        print("I am Parent")

class Child(Parent):
    def show_child(self):
        print("I am Child")


# ----- Multilevel Inheritance Example -----

print("\n----- Multilevel Inheritance Example -----")

c2 = Child()

c2.show_grandparent()
c2.show_parent()
c2.show_child()

