#Operators- Operators are symbols or keywords that perform operations on values or variables(operands

# operand operator operand
# 5 + 3

#Arithmetic Operators
# +,-,*,/,%,**,//
a=5
b=3
print(a+b)
print(a-b)
print(a*b)
print(a/b) #quotient
print(a%b) #remainder
print(a**b) #Exponentiation
print(a//b) #Floor division- rounded quotient

# Comparison Operators - compare two values and return True or False
num1=int(input()) #100
num2=int(input()) #50
print(f"num1 > num2 {num1>num2}") #greater than
print(f"num1 < num2 {num1<num2}") #lesser than
print(f"num1 == num2 {num1==num2}") #equals to
print(f"num1 != num2 {num1!=num2}") #not equal to
print(f"num1 >= num2 {num1>=num2}") #greater than or equal to
print(f"num1 <= num2 {num1<=num2}") #less than or equal to


print()
#Logical Operators - combine multiple conditions
#and - both conditions must be true
#or - at least one condition must be true
#not - reverses result
# A    B    A and B      A or B
# T    T       T           T
# F    T       F           T
# T    F       F           T
# F    F       F           F


# =========================================
# Python Basics: Operators & Conditionals
# =========================================


# -------------------------------
# Arithmetic Operators
# -------------------------------
# +, -, *, /, %, **, //

a = 5
b = 3

print("Arithmetic Operations:")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division (Quotient):", a / b)
print("Modulus (Remainder):", a % b)
print("Exponentiation:", a ** b)
print("Floor Division:", a // b)


# -------------------------------
# Comparison Operators
# -------------------------------
# Compare two values → returns True or False

num1 = int(input("\nEnter first number: "))
num2 = int(input("Enter second number: "))

print("\nComparison Results:")
print(f"num1 > num2: {num1 > num2}")
print(f"num1 < num2: {num1 < num2}")
print(f"num1 == num2: {num1 == num2}")
print(f"num1 != num2: {num1 != num2}")
print(f"num1 >= num2: {num1 >= num2}")
print(f"num1 <= num2: {num1 <= num2}")


# -------------------------------
# Logical Operators
# -------------------------------
# and → both conditions must be True
# or  → at least one condition must be True
# not → reverses the result

print("\nLogical Operations:")
print("True OR False:", True or False)
print("NOT True:", not True)

age = 20
citizen = True

# Check voting eligibility using logical AND
print("Eligible to vote:", age > 18 and citizen)

print("10 > 20 OR 10 > 100:", 10 > 20 or 10 > 100)
print("10 < 20 OR 10 > 100:", 10 < 20 or 10 > 100)

num = int(input("\nEnter a number (10-50 check): "))
print("Between 10 and 50:", num > 10 and num < 50)


# -------------------------------
# Assignment Operators
# -------------------------------
# Used to update variable values

x = 30
print("\nInitial value of x:", x)

x += 20  # same as x = x + 20
print("After x += 20:", x)

x = 50
x -= 25
print("After x -= 25:", x)

x = 4
x *= 40
print("After x *= 40:", x)

x /= 4
print("After x /= 4:", x)


# -------------------------------
# Membership Operators
# -------------------------------
# Check if a value exists in a sequence

text = "python"

print("\nMembership Operations:")
print("'p' in text:", "p" in text)
print("'x' in text:", "x" in text)
print("'l' not in text:", "l" not in text)


# -------------------------------
# Identity Operators
# -------------------------------
# is → checks if both variables refer to same object
# == → checks if values are equal

print("\nIdentity Operations:")

x = 10
y = 10
print("x is y:", x is y)

a = b = c = d = 6
print("All variables refer to same object:", a is b is c is d)

x = 1000
b = x
print("x is b:", x is b)

x = 1000
y = 1000
print("x == y (value check):", x == y)
print("x is y (memory check):", x is y)


# -------------------------------
# Conditional Statements
# -------------------------------

# Simple if condition
age = 20
if age >= 18:
    print("\nEligible to vote")


# if-else example
num = int(input("\nEnter a number: "))
if num > 0:
    print("Positive number")
else:
    print("Negative number")


# Even or Odd check
num = int(input("\nEnter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")


# if-elif-else (grading system)
marks = int(input("\nEnter marks: "))
if marks >= 90:
    print("Grade: A")
elif marks >= 70:
    print("Grade: B")
elif marks >= 50:
    print("Grade: C")
else:
    print("Fail")


# -------------------------------
# Nested if statements
# -------------------------------

age = 20
citizen = True

if age >= 18:
    if citizen:
        print("\nEligible to vote (Nested If)")


# Simple login system
username = input("\nUsername: ")
password = input("Password: ")

if username == 'admin':
    if password == '1234':
        print("Login successful")
    else:
        print("Wrong password")
else:
    print("Wrong username")


# A  not A
# T    F
# F    T

print()
print(True or False)
print(not True)

print()
age = 20
citizen = True
print(age>18 and citizen)

print()
print(10>20 or 10>100)
print(10<20 or 10>100)

print()
print(10>20 or 10>100)
print(10<20 or 10>100)

num=int(input())
print(num>10 and num<50)

#Assignment Operator -
x=30
print(x)

print()
x=10
x+=20 #(X+= is treated as x=x+something)
print(x)

x=50
x-=25
print(x)

x=4
x*=40
print(x)


x/=4
print(x)

print()
print(40)
#  print(100)

print()
#Membership Operators- used to check if something exists in a sequence
#in
#not in
text="python"
print("p" in text)
print('x' in text)
print('l' not in text)

# text = input()
# check for if z is present or not

print()
#Identity Operators - check whether two variables refer to the same object
# is
# is not
#-5 to 256
x=10
y=10
print(x is y)

print()
a=6
b=6
c=6
d=6
print(a is b)
print(b is c)
print(c is d)
print(a is b is c is d) # (a is b) and (b is c) and (c is d)

x=1000
b=x
print( x is b)

print()
x=1000
y=1000
print(x==y) # checks for the values
print(x is y) # checks for the location these variables are stored at



print()
#Traffic light is red -> Stop

# If light is red
        # stop
  #Else
      # go

print()
#Conditionals
# if condition:
      #statement

age=20
if age>=18:
  print("Eligible to vote")



print()
num=int(input())
if num>0:
  print("Positive number")
else:
  print("Negative number")

print()
num=int(input("Enter num: "))
if num%2==0:
  print("Even")
else:
  print("Odd")

print()
#if-elif-else
marks=int(input("Enter marks: "))
if marks>=90:
  print("A")
elif marks>=70:
  print("B")
elif marks>=50:
  print("C")
else:
  print("Fail")

print()
#Nested if - if statement inside another if statement
#used when a second condition should only be checked after the first condition is true

age=20
citizen=True
if age>=18:
  if citizen:
    print("Eligible to vote")


print()
username=input("Username: ")
password=input("Password: ")
if username=='admin':
  if password=='1234':
    print("Login successful")
  else:
    print("wrong password")
else:
  print('Wrong username')
