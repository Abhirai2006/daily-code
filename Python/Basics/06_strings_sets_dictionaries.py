# =========================================
# Python Basics: Strings, Sets & Dictionaries
# =========================================


# -------------------------------
# 1. Mutable vs Immutable
# -------------------------------
# Mutable   → can be changed after creation
# Immutable → cannot be changed after creation

print("\n===== Mutable vs Immutable =====")

print("Strings are immutable.")
print("Sets and dictionaries are mutable.")


# -------------------------------
# 2. Strings
# -------------------------------
# String → sequence of characters

print("\n===== Strings =====")

word = "Python"

print(f"Word: {word}")
print(f"First Character: {word[0]}")
print(f"Third Character: {word[2]}")


# -------------------------------
# 3. String Indexing
# -------------------------------
# Positive indexing starts from 0
# Negative indexing starts from -1

print("\n===== String Indexing =====")

text = "PythonProgramming"

print(f"Last Character: {text[-1]}")


# -------------------------------
# 4. String Slicing
# -------------------------------
# string[start:end]

print("\n===== String Slicing =====")

t = "HelloWorld"

print(f"t[0:5] → {t[0:5]}")
print(f"t[0:3] → {t[0:3]}")
print(f"t[3:] → {t[3:]}")
print(f"t[-3:] → {t[-3:]}")


# -------------------------------
# 5. len() Function
# -------------------------------
# Returns total characters

print("\n===== len() Function =====")

sample = "PythonProgramming"

print(f"Length: {len(sample)}")


# -------------------------------
# 6. String Concatenation
# -------------------------------
# Joining strings together

print("\n===== String Concatenation =====")

a = "Hello "
b = "World"

print(a + b)


# -------------------------------
# 7. count() Method
# -------------------------------
# Counts occurrences of character

print("\n===== count() Method =====")

text = "pyyyyyython"

print(f"Count of 'y': {text.count('y')}")


# -------------------------------
# 8. String Multiplication
# -------------------------------

print("\n===== String Multiplication =====")

text = "Hi "

print(text * 3)


# -------------------------------
# 9. Membership Operators
# -------------------------------
# in / not in

print("\n===== Membership Operators =====")

name = "Amrutha"

print(f"'A' in name → {'A' in name}")
print(f"'z' in name → {'z' in name}")


# -------------------------------
# 10. String Methods
# -------------------------------

print("\n===== String Methods =====")

text = "python"

print(f"Uppercase: {text.upper()}")

text = "PYTHON"

print(f"Lowercase: {text.lower()}")

text = "I like Java"

print(f"replace(): {text.replace('Java', 'Python')}")
print(f"Original String: {text}")


# -------------------------------
# 11. Sets
# -------------------------------
# Set →
# - Unordered
# - No duplicates
# - Mutable

print("\n===== Sets =====")

s = {1, 2, 3, 4, 5}

print(f"Set: {s}")
print(f"Data Type: {type(s)}")


# -------------------------------
# 12. Duplicate Removal in Sets
# -------------------------------

print("\n===== Duplicate Removal =====")

s = {1, 2, 3, 3, 3, 4, 4}

print(f"Duplicates Removed Automatically: {s}")


# -------------------------------
# 13. Set Methods
# -------------------------------

print("\n===== Set Methods =====")

s = {1, 2, 3}

print(f"Original Set: {s}")

# add()
s.add(4)

print(f"After add(4): {s}")

# remove()
s.remove(1)

print(f"After remove(1): {s}")

# discard()
s.discard(10)

print(f"After discard(10): {s}")


# -------------------------------
# 14. Set Operations
# -------------------------------

print("\n===== Set Operations =====")

a = {1, 2, 3}
b = {3, 4, 5}

# Union
print(f"Union: {a | b}")

# Intersection
print(f"Intersection: {a & b}")

# Difference
print(f"Difference (a - b): {a - b}")


# -------------------------------
# 15. Dictionaries
# -------------------------------
# Dictionary →
# Stores data in key-value pairs

print("\n===== Dictionaries =====")

student = {
    "Name": "Rahul",
    "Age": 16,
    "Course": "Python"
}

print(student)


# -------------------------------
# 16. Accessing Dictionary Values
# -------------------------------

print("\n===== Accessing Dictionary Values =====")

print(f"Name: {student['Name']}")
print(f"Age: {student['Age']}")


# -------------------------------
# 17. Updating Dictionary Values
# -------------------------------

print("\n===== Updating Dictionary Values =====")

student["Age"] = 25

print(student)


# -------------------------------
# 18. Adding New Key-Value Pair
# -------------------------------

print("\n===== Adding New Data =====")

student["City"] = "Pune"

print(student)


# -------------------------------
# 19. Removing Dictionary Values
# -------------------------------

print("\n===== Removing Dictionary Values =====")

student.pop("Age")

print(student)


# -------------------------------
# 20. Dictionary Methods
# -------------------------------

print("\n===== Dictionary Methods =====")

print(f"Keys: {student.keys()}")
print(f"Values: {student.values()}")
print(f"Items: {student.items()}")
print(f"Get Name: {student.get('Name')}")


# -------------------------------
# 21. Iterating Through Dictionary
# -------------------------------

print("\n===== Iterating Through Dictionary =====")

student = {
    "Name": "Rahul",
    "Age": 16,
    "Course": "Python"
}

print("Dictionary Keys:")

for key in student:
    print(key)

print("\nDictionary Values:")

for value in student.values():
    print(value)