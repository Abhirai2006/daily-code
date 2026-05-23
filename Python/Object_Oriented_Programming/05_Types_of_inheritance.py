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


# =========================================
# 4. Hierarchical Inheritance
# =========================================

# Multiple child classes inherit
# from the same parent class.

# One Parent -> Many Children

class Animal:
    def eat(self):
        print("Animal Eats Food")


class Dog(Animal):
    def bark(self):
        print("Dog Barks")


class Cat(Animal):
    def meow(self):
        print("Cat Meows")


# ----- Hierarchical Inheritance Example -----

print("\n----- Hierarchical Inheritance Example -----")

d2 = Dog()
c3 = Cat()

d2.eat()
d2.bark()

print()

c3.eat()
c3.meow()


# =========================================
# 5. Hybrid Inheritance
# =========================================

# Hybrid inheritance is a combination
# of two or more inheritance types.


class Person:
    def details(self):
        print("Person Details")


class Student(Person):
    def study(self):
        print("Student is Studying")


class Employee(Person):
    def work(self):
        print("Employee is Working")


class Intern(Student, Employee):
    def role(self):
        print("I am an Intern")


# ----- Hybrid Inheritance Example -----

print("\n----- Hybrid Inheritance Example -----")

i1 = Intern()

i1.details()
i1.study()
i1.work()
i1.role()


# =========================================
# super() Function
# =========================================

# super() is used to call
# methods from the parent class.

# It helps avoid directly
# using parent class names.


class Father:
    def skills(self):
        print("Driving")
        super().skills()


class Mother:
    def skills(self):
        print("Cooking")


class Child(Father, Mother):
    def skills(self):
        print("Child Skills")
        super().skills()


# ----- super() Example -----

print("\n----- super() Example -----")

c4 = Child()
c4.skills()

