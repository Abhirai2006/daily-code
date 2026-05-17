# =========================================
# Python Basics: Lambda Functions
# =========================================


# -------------------------------
# 1. Introduction to Lambda
# -------------------------------
# Lambda → small anonymous function
# Written in a single line

# Syntax:
# lambda parameters : expression

example = lambda a, b: a + b

print(example(5, 3))


# -------------------------------
# 2. Normal Function vs Lambda
# -------------------------------

# Normal Function
def square(x):

    return x * x


print("Normal Function:", square(5))


# Lambda Version
square = lambda x: x * x

print("Lambda Function:", square(5))


# -------------------------------
# 3. Lambda with Multiple Inputs
# -------------------------------

add = lambda a, b: a + b

print("Addition:", add(10, 30))


# -------------------------------
# 4. Lambda for Even Numbers
# -------------------------------
# Returns True if number is even

even = lambda x: x % 2 == 0

print("Is 100 Even?", even(100))


# -------------------------------
# 5. map() Function
# -------------------------------
# map() applies operation to every element

list1 = [1, 2, 3, 4, 5]


# Normal Way
squares = []

for i in list1:

    squares.append(i * i)

print("Squares using loop:", squares)


# Using map() + lambda
squares = list(map(lambda x: x * x, list1))

print("Squares using map:", squares)


# -------------------------------
# 6. filter() Function
# -------------------------------
# filter() keeps values
# that satisfy a condition

numbers = [1,2,3,4,5,6,7,8,9,10]


# Normal Way
evens = []

for i in numbers:

    if i % 2 == 0:

        evens.append(i)

print("Even numbers using loop:", evens)


# Using filter() + lambda
evens = list(filter(lambda x: x % 2 == 0, numbers))

print("Even numbers using filter:", evens)


# -------------------------------
# 7. sorted() Function
# -------------------------------
# sorted() arranges elements in order

li = [12, 4, 56, 32, 3, 4, 5]

print("Ascending Order:", sorted(li))

print("Descending Order:", sorted(li, reverse=True))


# -------------------------------
# 8. Sorting using Lambda
# -------------------------------
# key → decides sorting rule

words = [
    "apple",
    "Lion",
    "Fish",
    "Banana",
    "rhinoceros",
    "sorting"
]


# Sorting based on word length
result = sorted(words, key=lambda x: len(x))

print("Sorted by Length:", result)


# -------------------------------
# 9. Sorting based on Last Digit
# -------------------------------

nums = [23, 45, 63, 78, 30, 129]

result = sorted(nums, key=lambda x: x % 10)

print("Sorted by Last Digit:", result)