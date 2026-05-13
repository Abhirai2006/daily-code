# =========================================
# Python Basics: Data Types & Type Casting
# =========================================


# -------------------------------
# 1. Integer Data Type
# -------------------------------
# Integers are whole numbers

print("\n===== Integer Data Type =====")

positive_num = 10
negative_num = -5

print(f"Value: {positive_num}, Type: {type(positive_num)}")
print(f"Value: {negative_num}, Type: {type(negative_num)}")


# -------------------------------
# 2. Float Data Type
# -------------------------------
# Floats are decimal numbers

print("\n===== Float Data Type =====")

float_num1 = 12.5
float_num2 = -12.5
float_num3 = 0.0
float_num4 = -20.0

print(f"{float_num1} → {type(float_num1)}")
print(f"{float_num2} → {type(float_num2)}")
print(f"{float_num3} → {type(float_num3)}")
print(f"{float_num4} → {type(float_num4)}")


# -------------------------------
# 3. String Data Type
# -------------------------------
# Strings store text data

print("\n===== String Data Type =====")

first_name = "Adarsh"
second_name = 'Tanya'

print(f"First Name: {first_name}")
print(f"Second Name: {second_name}")

print(f"Type of first_name: {type(first_name)}")
print(f"Type of second_name: {type(second_name)}")


# -------------------------------
# 4. Boolean Data Type
# -------------------------------
# Boolean values are True or False

print("\n===== Boolean Data Type =====")

is_logged_in = True
is_admin = False

print(f"{is_logged_in} → {type(is_logged_in)}")
print(f"{is_admin} → {type(is_admin)}")

# String "True" is not boolean
text_value = "True"

print(f"{text_value} → {type(text_value)}")


# -------------------------------
# 5. Complex Data Type
# -------------------------------
# Complex numbers use 'j'

print("\n===== Complex Data Type =====")

complex_num1 = 2 + 5j
complex_num2 = 3 + 4j

print(f"{complex_num1} → {type(complex_num1)}")

# Accessing real and imaginary parts
print(f"Real Part: {complex_num2.real}")
print(f"Imaginary Part: {complex_num2.imag}")


# =========================================
# Type Casting
# =========================================

# -------------------------------
# 6. Integer to Float
# -------------------------------

print("\n===== Integer to Float =====")

num = 50

converted_num = float(num)

print(f"Before: {num} → {type(num)}")
print(f"After : {converted_num} → {type(converted_num)}")


# -------------------------------
# 7. Float to Integer
# -------------------------------
# Decimal part gets removed

print("\n===== Float to Integer =====")

decimal_num = 12.89

converted_num = int(decimal_num)

print(f"Before: {decimal_num} → {type(decimal_num)}")
print(f"After : {converted_num} → {type(converted_num)}")


# -------------------------------
# 8. Integer to String
# -------------------------------

print("\n===== Integer to String =====")

number = 12

string_number = str(number)

print(f"Before: {number} → {type(number)}")
print(f"After : {string_number} → {type(string_number)}")


# -------------------------------
# 9. String to Float
# -------------------------------

print("\n===== String to Float =====")

value = "10.6"

converted_value = float(value)

print(f"Before: {value} → {type(value)}")
print(f"After : {converted_value} → {type(converted_value)}")


# -------------------------------
# 10. String to Integer
# -------------------------------

print("\n===== String to Integer =====")

value = "10"

converted_value = int(value)

print(f"Before: {value} → {type(value)}")
print(f"After : {converted_value} → {type(converted_value)}")


# Invalid Conversion Example
# value = "Python"
# int(value)   ❌ ValueError


# =========================================
# Boolean Conversions
# =========================================

# -------------------------------
# 11. Boolean to Integer
# -------------------------------
# True = 1
# False = 0

print("\n===== Boolean to Integer =====")

value = True

converted_value = int(value)

print(f"Before: {value} → {type(value)}")
print(f"After : {converted_value} → {type(converted_value)}")


# -------------------------------
# 12. Integer to Boolean
# -------------------------------
# 0 → False
# Non-zero → True

print("\n===== Integer to Boolean =====")

value = 100

converted_value = bool(value)

print(f"Before: {value} → {type(value)}")
print(f"After : {converted_value} → {type(converted_value)}")


# -------------------------------
# 13. False to Integer
# -------------------------------

print("\n===== False to Integer =====")

value = False

converted_value = int(value)

print(f"Before: {value} → {type(value)}")
print(f"After : {converted_value} → {type(converted_value)}")


# -------------------------------
# 14. Boolean to String
# -------------------------------

print("\n===== Boolean to String =====")

value = True

converted_value = str(value)

print(f"Before: {value} → {type(value)}")
print(f"After : {converted_value} → {type(converted_value)}")


# -------------------------------
# 15. Boolean to Float
# -------------------------------

print("\n===== Boolean to Float =====")

value = True

converted_value = float(value)

print(f"Before: {value} → {type(value)}")
print(f"After : {converted_value} → {type(converted_value)}")


# =========================================
# User Input
# =========================================

# -------------------------------
# 16. Taking String Input
# -------------------------------
# input() stores values as string by default

print("\n===== String Input =====")

user_input = input("Enter any value: ")

print(f"You entered: {user_input}")
print(f"Data Type: {type(user_input)}")


# -------------------------------
# 17. Integer Input
# -------------------------------

print("\n===== Integer Input =====")

integer_value = int(input("Enter an integer value: "))

print(f"You entered: {integer_value}")
print(f"Data Type: {type(integer_value)}")


# -------------------------------
# 18. Float Input
# -------------------------------

print("\n===== Float Input =====")

float_value = float(input("Enter a float value: "))

print(f"You entered: {float_value}")
print(f"Data Type: {type(float_value)}")