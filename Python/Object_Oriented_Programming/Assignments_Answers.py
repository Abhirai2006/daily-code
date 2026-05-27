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


# =========================================
# Answer 03
# Rectangle Area & Perimeter
# =========================================

class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)


# ----- Rectangle Example -----

print("\n----- Rectangle Example -----")

r1 = Rectangle(10, 5)
print("Area :", r1.area())
print("Perimeter :", r1.perimeter())


# =========================================
# Answer 04
# Employee Salary Category
# =========================================

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def category(self):
        if self.salary > 50000:
            return "High"
        elif 30000 <= self.salary <= 50000:
            return "Medium"
        else:
            return "Low"


# ----- Employee Category Example -----

print("\n----- Employee Category Example -----")

employees = [
    Employee("Rahul", 60000),
    Employee("Anjali", 45000),
    Employee("Kiran", 20000)

]

for emp in employees:
    print(emp.name, "->", emp.category())


# =========================================
# Answer 05
# Library Management System
# =========================================

class Book:
    def __init__(self, title):
        self.title = title
        self.available = True

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"{book.title} Added Successfully")


    def issue_book(self, title):
        for book in self.books:
            if book.title == title and book.available:
                book.available = False
                print(f"{title} Issued Successfully")
                return
        print("Book Not Available")


    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                book.available = True
                print(f"{title} Returned Successfully")
                return


# ----- Library Management Example -----

print("\n----- Library Management Example -----")

lib = Library()

b1 = Book("Python")
b2 = Book("Java")

lib.add_book(b1)
lib.add_book(b2)

lib.issue_book("Java")
lib.return_book("Java")


# =========================================
# Answer 06
# Class Variables & Instance Variables
# =========================================

class Employee:
    company = "ABC Technologies"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


# ----- Employee Details Example -----

print("\n----- Employee Details Example -----")

e1 = Employee("Rahul", 30000)
e2 = Employee("Anjali", 50000)

print(e1.name, e1.salary, e1.company)
print(e2.name, e2.salary, e2.company)


# =========================================
# Answer 07
# Shape Area Using Polymorphism
# =========================================

class Shape:
    def area(self):
        return 0


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius


    def area(self):
        return 3.14 * self.radius * self.radius


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side


# ----- Shape Area Example -----

print("\n----- Shape Area Example -----")

c1 = Circle(7)
s1 = Square(5)

print("Circle Area :", c1.area())
print("Square Area :", s1.area())


# =========================================
# Answer 08
# Private Variable - Age
# =========================================

class Person:
    def __init__(self, age):
        self.__age = age

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Invalid Age")

    def get_age(self):
        return self.__age


# ----- Person Age Example -----

print("\n----- Person Age Example -----")

p1 = Person(20)
print("Initial Age :", p1.get_age())
p1.set_age(25)
print("Updated Age :", p1.get_age())

