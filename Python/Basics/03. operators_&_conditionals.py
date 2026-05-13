# =========================================
# Python Basics: Operators & Conditional Statements
# =========================================


# -------------------------------
# 1. Arithmetic Operators
# -------------------------------
# Arithmetic operators are used to perform
# mathematical operations

print("\n===== Arithmetic Operators =====")

a = 5
b = 3

print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b}")     # Division
print(f"{a} % {b} = {a % b}")     # Remainder
print(f"{a} ** {b} = {a ** b}")   # Exponentiation
print(f"{a} // {b} = {a // b}")   # Floor division


# -------------------------------
# 2. Comparison Operators
# -------------------------------
# Comparison operators return True or False

print("\n===== Comparison Operators =====")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print(f"{num1} > {num2}  → {num1 > num2}")
print(f"{num1} < {num2}  → {num1 < num2}")
print(f"{num1} == {num2} → {num1 == num2}")
print(f"{num1} != {num2} → {num1 != num2}")
print(f"{num1} >= {num2} → {num1 >= num2}")
print(f"{num1} <= {num2} → {num1 <= num2}")


# -------------------------------
# 3. Logical Operators
# -------------------------------
# and → both conditions must be True
# or  → at least one condition must be True
# not → reverses the result

print("\n===== Logical Operators =====")

print(f"True or False → {True or False}")
print(f"not True → {not True}")

age = 20
citizen = True

print(f"Eligible to vote → {age > 18 and citizen}")

print(f"10 > 20 or 10 > 100 → {10 > 20 or 10 > 100}")
print(f"10 < 20 or 10 > 100 → {10 < 20 or 10 > 100}")

num = int(input("\nEnter a number between 10 and 50: "))

print(f"Is number between 10 and 50? → {num > 10 and num < 50}")


# -------------------------------
# 4. Assignment Operators
# -------------------------------
# Used to update variable values

print("\n===== Assignment Operators =====")

x = 30

print(f"Initial value of x = {x}")

x += 20
print(f"After x += 20 → {x}")

x -= 25
print(f"After x -= 25 → {x}")

x *= 4
print(f"After x *= 4 → {x}")

x /= 5
print(f"After x /= 5 → {x}")


# -------------------------------
# 5. Membership Operators
# -------------------------------
# Used to check whether a value exists
# inside a sequence

print("\n===== Membership Operators =====")

text = "python"

print(f"'p' in text → {'p' in text}")
print(f"'x' in text → {'x' in text}")
print(f"'l' not in text → {'l' not in text}")


# -------------------------------
# 6. Identity Operators
# -------------------------------
# == checks value equality
# is checks memory location

print("\n===== Identity Operators =====")

x = 10
y = 10

print(f"x == y → {x == y}")
print(f"x is y → {x is y}")

a = b = c = d = 6

print(f"a is b is c is d → {a is b is c is d}")

x = 1000
y = 1000

print(f"x == y → {x == y}")
print(f"x is y → {x is y}")


# -------------------------------
# 7. Conditional Statements
# -------------------------------
# if statement executes code only
# when condition becomes True

print("\n===== Conditional Statements =====")

age = 20

if age >= 18:
    print("Eligible to vote")


# -------------------------------
# 8. Positive or Negative Number
# -------------------------------

print("\n===== Positive or Negative Check =====")

num = int(input("Enter a number: "))

if num > 0:
    print("Positive Number")
else:
    print("Negative Number")


# -------------------------------
# 9. Even or Odd Number
# -------------------------------

print("\n===== Even or Odd Check =====")

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")


# -------------------------------
# 10. Grade Calculation
# -------------------------------
# if-elif-else ladder

print("\n===== Grade Calculator =====")

marks = int(input("Enter marks: "))

if marks >= 90:
    print("Grade: A")

elif marks >= 70:
    print("Grade: B")

elif marks >= 50:
    print("Grade: C")

else:
    print("Fail")


# -------------------------------
# 11. Nested if Statement
# -------------------------------
# if statement inside another if

print("\n===== Nested If Statement =====")

age = 20
citizen = True

if age >= 18:

    if citizen:
        print("Eligible to vote")


# -------------------------------
# 12. Simple Login System
# -------------------------------

print("\n===== Login System =====")

username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin":

    if password == "1234":
        print("Login Successful")

    else:
        print("Wrong Password")

else:
    print("Wrong Username")