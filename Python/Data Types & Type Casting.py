# Data Types & Type Casting in Python

# ----------------------------------------
# Data Types in Python
# ----------------------------------------

# Integer: whole numbers (positive or negative)
a = 10
b = -5
print(a, type(a))
print(b, type(b))

# Float: decimal numbers
a = 12.5
b = -12.5
x = 0.0
z = -20.
print(type(a), type(b), type(x), type(z))

# String: sequence of characters (text)
abc = "Adarsh"
xyz = 'Tanya'
print(abc, xyz)
print(type(abc), type(xyz))

# Note:
# Every data type in Python is internally treated as a class
# Example output: <class 'int'>

# Boolean: True or False
var1 = True
var2 = False
print(var1, type(var1))
print(var2, type(var2))

# String "True" is NOT boolean
w = "True"
print(type(w))

# Complex Numbers: real + imaginary (j is used)
x = 2 + 5j
z = 3 + 4j
print(x, type(x))

# Access real and imaginary parts
print(z.real)
print(z.imag)

# ----------------------------------------
# Type Casting (Type Conversion)
# ----------------------------------------

# int → float
a = 50
a = float(a)
print(a, type(a))

# float → int (decimal part removed)
a = 12.89
a = int(a)
print(a, type(a))

# int → string
num = 12
t = str(num)
print(t, type(t))

# string → float
a = "10.6"
a = float(a)
print(a, type(a))

# string → int (must contain integer value)
a = "10"
a = int(a)
print(a, type(a))

# Invalid conversion example
# a = "tanya"
# a = int(a)  # This will cause ValueError

# ----------------------------------------
# Boolean Conversions
# ----------------------------------------

# bool → int
# True = 1, False = 0
a = True
print(a, type(a))
a = int(a)
print(a, type(a))

# int → bool
# 0 → False, any non-zero → True
a = 100
a = bool(a)
print(a, type(a))

b = False
b = int(b)
print(b, type(b))

# bool → string
x = True
x = str(x)
print(x, type(x))

# bool → float
a = True
a = float(a)
print(a, type(a))

# ----------------------------------------
# User Input
# ----------------------------------------

# By default, input() takes string
x = input("Enter value: ")
print(x, type(x))

# Convert input to integer
x = int(input("Enter integer value: "))
print(x, type(x))

# Convert input to float
z = float(input("Enter float value: "))
print(z, type(z))