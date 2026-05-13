# =========================================
# Python Basics: Introduction & Variables
# =========================================


# -------------------------------
# 1. Introduction to Python
# -------------------------------
# Python is a high-level interpreted programming language.

# Why Python?
# - Easy to learn and understand
# - Used in AI, ML, web development, and automation
# - Has many powerful libraries
# - Beginner-friendly and open-source

print("\n===== Introduction to Python =====")

print("Hello World")   # Prints text inside quotes


# -------------------------------
# 2. Strings vs Numbers
# -------------------------------
# Strings are written inside quotes
# Numbers are used for calculations

print("\n===== Strings vs Numbers =====")

print("10-20")      # Printed as text
print(10 - 20)      # Performs subtraction

print("Addition Result:", 10 + 20 + 30 + 40 + 50)

print("Single Number:", 10)


# -------------------------------
# 3. Printing Different Values
# -------------------------------

print("\n===== Printing Different Values =====")

print("Apple")
print("Banana")

print("Number:", 30)

print("20 + 100 =", 20 + 100)


# -------------------------------
# 4. String Concatenation
# -------------------------------
# Joining two strings together

print("\n===== String Concatenation =====")

print("10" + "20")   # Result: 1020


# -------------------------------
# 5. Printing Multiple Values
# -------------------------------

print("\n===== Printing Multiple Values =====")

print(10, 20, 30, 40, "apple", "banana")


# -------------------------------
# 6. Printing Labels with Values
# -------------------------------

print("\n===== User Information =====")

print("Name:", "Abc")
print("Age:", 45)
print("Email:", "abc@gmail.com")
print("Gender:", "M")


# -------------------------------
# 7. print() and end=""
# -------------------------------
# print() moves to a new line by default
# end="" keeps output on same line

print("\n===== Using end Parameter =====")

print(10)
print(20)

print(10, end=" ")
print(20)


# =========================================
# Variables
# =========================================

# -------------------------------
# 8. Introduction to Variables
# -------------------------------
# Variables are containers used to store data

print("\n===== Variables =====")

name = "Vishal"

print("Stored Name:", name)


# -------------------------------
# 9. Using Variables in Calculations
# -------------------------------

print("\n===== Variables in Calculations =====")

a = 20
b = 30

print("Sum =", a + b)


# -------------------------------
# 10. Storing Multiple Details
# -------------------------------

print("\n===== Student Details =====")

Name = "Daksh"
Age = 24
YOG = 2020
Email = "abc@gmail.com"
Gender = "Male"

print("Name:", Name)
print("Age:", Age)
print("Year of Graduation:", YOG)
print("Email:", Email)
print("Gender:", Gender)


# -------------------------------
# 11. Rules for Variable Names
# -------------------------------
# 1. Can start with a letter or underscore
# 2. Cannot start with a number
# 3. Special characters are not allowed
# 4. Spaces are not allowed
# 5. Variable names are case-sensitive
# 6. Keywords cannot be used

print("\n===== Variable Naming Rules =====")

# Valid Examples:
# age = 12
# _salary = 120000
# marks2 = 100
# Roll_No = 12

# Invalid Examples:
# 2marks = 90
# total marks = 70
# price$ = 30
# for = 10

print("Check comments for valid and invalid examples.")


# -------------------------------
# 12. Case Sensitivity
# -------------------------------
# name and Name are treated differently

print("\n===== Case Sensitivity =====")

name = "Aadi"
Name = "Tanya"

print("name =", name)
print("Name =", Name)


# -------------------------------
# 13. Printing Without Space
# -------------------------------

print("\n===== Printing Without Space =====")

print("Hello", end="")
print("World")