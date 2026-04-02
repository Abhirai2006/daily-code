# Python is a high-level, interpreted programming language.

# Why Python?
# 1. Easy to understand, learn, and write.
# 2. Used in many areas like data science, AI, ML, web development, and automation.
# 3. Has many useful libraries such as pandas, numpy, matplotlib, and scikit-learn.
# 4. Open-source and beginner-friendly.

# Printing text
print("Hello World")  # Prints the exact text inside quotes

# Printing strings and numbers
print("10-20")        # Prints as text
print(10 - 20)        # Performs subtraction and prints the result

print(10 + 20 + 30 + 40 + 50)
print(10)

# This will give an error because text must be written inside quotes
# print(Apple is a fruit).

print("Apple")
print("Banana")
print(30)
print(20 + 100)

# String concatenation
print("10" + "20")    # Joins the strings, result: 1020

# Printing multiple values
print(10, 20, 30, 40, "apple", "banana")

# Printing email as text
print("abc@gmail.com")

# Printing labels with values
print("Name:", "Abc")
print("Age:", 45)
print("Email:", "abc@gmail.com")
print("Gender:", "M")

# print() adds a new line by default
print(10)
print(20)

# end=" " keeps the output on the same line
print(10, end=" ")
print(20)


# ----------------------------------------
# Variables
# ----------------------------------------

# A variable is a container used to store data.
# Example: name = "Rahul"
# name -> variable name
# =    -> assignment operator
# "Rahul" -> value

name = "Vishal"
print(name)

a = 20
b = 30
print(a + b)

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

# ----------------------------------------
# Rules for creating variable names
# ----------------------------------------
# 1. A variable can start with a letter or underscore (_).
# 2. A variable cannot start with a number.
# 3. Special characters like $, @, #, % are not allowed.
# 4. Spaces are not allowed in variable names.
# 5. Variable names are case-sensitive.
#    Example: name and Name are different.
# 6. Keywords cannot be used as variable names.
#    Example: for, while, if, else, not, etc.

# Valid examples:
# age = 12
# _salary = 120000
# marks2 = 100
# Roll_No = 12

# Invalid examples:
# 2marks = 90
# total marks = 70
# price$ = 30
# for = 10

# Case sensitivity example
name = "Aadi"
Name = "Tanya"
print(name, Name)

# If we want to print on the same line without space
print("Hello", end="")
print("World")