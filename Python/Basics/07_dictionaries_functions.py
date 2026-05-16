# =========================================
# Python Basics: Dictionaries & Functions
# =========================================


# -------------------------------
# 1. Iterating Through Dictionary
# -------------------------------
# items() returns both keys and values

print("1)\n")

stu = {
    "Product": "Laptop",
    "Price": 50000,
    "Brand": "Dell"
}

for key, value in stu.items():
    print(key, ":", value)


# -------------------------------
# 2. Nested Dictionaries
# -------------------------------
# A dictionary inside another dictionary

print("\n2)\n")

students = {
    "stu1": {
        "Name": "Debjit",
        "Age": 32
    },

    "stu2": {
        "Name": "Kshitij",
        "Age": 21
    }
}

print(students)

# Accessing nested dictionary values
print("\nStudent 1 Name:")
print(students["stu1"]["Name"])


# -------------------------------
# 3. Iterating Nested Dictionary
# -------------------------------

print("\n3)\n")

for student, details in students.items():

    print(student)

    for key, value in details.items():
        print(key, ":", value)


# -------------------------------
# 4. Introduction to Functions
# -------------------------------
# Function → reusable block of code

print("\n4)\n")

# Built-in Functions
numbers = [1, 2, 3, 4, 5]

print("Maximum:", max(numbers))
print("Minimum:", min(numbers))

text = "Python"

print("Length:", len(text))


# -------------------------------
# 5. User Defined Functions
# -------------------------------
# Creating our own function

print("\n5)\n")

def greet():
    print("Hello Students")


# Calling function
greet()


# -------------------------------
# 6. Functions with Parameters
# -------------------------------
# Parameters receive input values

print("\n6)\n")

def add(a, b):

    print("Addition:", a + b)


# Function calls
add(5, 3)
add(10, 20)


# -------------------------------
# 7. Non-Returning Function
# -------------------------------
# Function prints result directly

print("\n7)\n")

def square(num):

    print("Square:", num * num)


square(4)


# -------------------------------
# 8. Returning Function
# -------------------------------
# Function returns value using return

print("\n8)\n")

def square(num):

    return num * num


result = square(10)

print("Returned Value:", result)


# -----------------------------------------------
# 9. Returning Function with Multiple Parameters
# -----------------------------------------------

print("\n9)\n")

def multiply(a, b):

    return a * b


product = multiply(5, 6)

print("Product:", product)