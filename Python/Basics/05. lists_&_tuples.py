# =========================================
# Python Basics: Lists & Tuples
# =========================================


# -------------------------------
# 1. Mutable vs Immutable
# -------------------------------
# Mutable   → can be changed
# Immutable → cannot be changed

print("\n===== Mutable vs Immutable =====")

print("Lists are mutable.")
print("Tuples are immutable.")


# -------------------------------
# 2. Sequential Datatypes
# -------------------------------
# Sequential datatypes store multiple
# values in a specific order

print("\n===== Sequential Datatypes =====")

print("Examples: List, Tuple, String")


# -------------------------------
# 3. Lists
# -------------------------------
# Lists are:
# - Ordered
# - Mutable
# - Allow duplicate values
# - Allow multiple datatypes

print("\n===== Lists =====")

numbers = [1, 2, 3, 4, 5, 1, 1]

print(f"Integer List: {numbers}")

mixed_list = ["apple", "banana", 12, 30, 3 + 4j, 1.0, True]

print(f"Mixed Datatype List: {mixed_list}")
print(f"Data Type: {type(mixed_list)}")


# -------------------------------
# 4. List Indexing
# -------------------------------
# Positive indexing starts from 0
# Negative indexing starts from -1

print("\n===== List Indexing =====")

sports = [
    "Football",
    "Badminton",
    "Cricket",
    "Hockey",
    "Basketball",
    "Kabaddi"
]

print(f"Element at index 5 → {sports[5]}")
print(f"Element at index -4 → {sports[-4]}")


# -------------------------------
# 5. Mutable Nature of Lists
# -------------------------------
# Lists can be modified

print("\n===== Mutable Nature of Lists =====")

sports[2] = "Baseball"

print(f"Updated List: {sports}")


# -------------------------------
# 6. Updating List Values
# -------------------------------

print("\n===== Updating List Values =====")

numbers = [1, 2, 3, 4, 5, 1, 1]

print(f"Original List: {numbers}")

numbers[4] = "yes"

print(f"Updated List: {numbers}")


# -------------------------------
# 7. List Slicing
# -------------------------------
# Syntax:
# list[start:end]

print("\n===== List Slicing =====")

sports = [
    "Football",
    "Badminton",
    "Cricket",
    "Hockey",
    "Basketball",
    "Kabaddi"
]

print(f"sports[0:4] → {sports[0:4]}")


# -------------------------------
# 8. More Slicing Examples
# -------------------------------

print("\n===== More Slicing Examples =====")

print(f"sports[:5] → {sports[:5]}")
print(f"sports[1:] → {sports[1:]}")
print(f"sports[-5:] → {sports[-5:]}")
print(f"sports[:] → {sports[:]}")
print(f"sports[::-1] → {sports[::-1]}")


# -------------------------------
# 9. Slicing with Step
# -------------------------------
# Syntax:
# list[start:end:step]

print("\n===== Slicing with Step =====")

print(f"sports[1::2] → {sports[1::2]}")


# -------------------------------
# 10. Length of List
# -------------------------------
# len() returns total elements

print("\n===== Length of List =====")

print(f"Total Elements: {len(sports)}")


# -------------------------------
# 11. append() Method
# -------------------------------
# Adds element at the end

print("\n===== append() Method =====")

li1 = [10, 20, 30, 40, 50]

print(f"Original List: {li1}")

li1.append(100)

print(f"After append(100): {li1}")

li1.append("Python")

print(f"After append('Python'): {li1}")


# -------------------------------
# 12. insert(), remove(), pop()
# -------------------------------

print("\n===== insert(), remove(), pop() =====")

# insert(index, value)
li1.insert(0, 123)

print(f"After insert(0, 123): {li1}")

# remove(value)
li1.remove(123)

print(f"After remove(123): {li1}")

# pop() removes last element
li1.pop()

print(f"After pop(): {li1}")

# pop(index)
li1.pop(1)

print(f"After pop(1): {li1}")


# -------------------------------
# 13. Tuples
# -------------------------------
# Tuples are:
# - Ordered
# - Immutable
# - Allow duplicates
# - Allow multiple datatypes

print("\n===== Tuples =====")

tup = (1, 2, 3, 4, 5, 5, 5)

print(f"Tuple: {tup}")
print(f"Data Type: {type(tup)}")


# -------------------------------
# 14. Tuple with Multiple Datatypes
# -------------------------------

print("\n===== Tuple with Multiple Datatypes =====")

tup = (1, 2, 3 + 4j, "Python")

print(f"Tuple: {tup}")
print(f"Data Type: {type(tup)}")


# -------------------------------
# 15. Single Element Tuple
# -------------------------------
# Comma is compulsory

print("\n===== Single Element Tuple =====")

t = (5,)

print(f"Tuple: {t}")
print(f"Data Type: {type(t)}")


# -------------------------------
# 16. Tuple Indexing
# -------------------------------

print("\n===== Tuple Indexing =====")

t = (1, 2, 3, 4, 5, 6, 7, 100)

print(f"Element at index 5 → {t[5]}")
print(f"Element at index -1 → {t[-1]}")

print(f"Length of Tuple → {len(t)}")

# Tuples are immutable
# t[2] = "Python" ❌


# -------------------------------
# 17. Tuple to List Conversion
# -------------------------------

print("\n===== Tuple to List Conversion =====")

print(f"Original Tuple: {t}")

lst = list(t)

print(f"Converted List: {lst}")


# -------------------------------
# 18. List to Tuple Conversion
# -------------------------------

print("\n===== List to Tuple Conversion =====")

lst = tuple(lst)

print(f"Converted Tuple: {lst}")