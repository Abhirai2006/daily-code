# =========================================
# Python Basics: Lists & Tuples
# =========================================


# -------------------------------
# 1. Mutable vs Immutable
# -------------------------------
# Mutable   → can be changed after creation
# Immutable → cannot be changed after creation

print("1)\n")

# Lists are mutable
# Tuples are immutable


# -------------------------------
# 2. Sequential Datatypes
# -------------------------------
# Sequential datatypes store multiple
# values in a specific order

print("2)\n")


# -------------------------------
# 3. Lists
# -------------------------------
# List → ordered and mutable collection
# - Allows duplicate values
# - Can store multiple datatypes

print("3)\n")

li = [1, 2, 3, 4, 5, 1, 1]

print(li)

li = ["apple", "banana", 12, 30, 3 + 4j, 1.0, True]

print(li)
print(type(li))


# -------------------------------
# 4. List Indexing
# -------------------------------
# Indexing starts from 0
# Negative indexing starts from -1

print("\n4)\n")

sports = [
    "Football",
    "Badminton",
    "Cricket",
    "Hockey",
    "Basketball",
    "Kabaddi"
]

print(sports[5])      # Positive indexing
print(sports[-4])     # Negative indexing


# -------------------------------
# 5. Mutable Nature of Lists
# -------------------------------
# Lists can be modified after creation

print("\n5)\n")

sports[2] = "Baseball"

print(sports)


# -------------------------------
# 6. Updating List Values
# -------------------------------

print("\n6)\n")

numbers = [1, 2, 3, 4, 5, 1, 1]

numbers[4] = "yes"

print(numbers)


# -------------------------------
# 7. List Slicing
# -------------------------------
# Syntax:
# list[start:end]
# start → included
# end → excluded

print("\n7)\n")

sports = [
    "Football",
    "Badminton",
    "Cricket",
    "Hockey",
    "Basketball",
    "Kabaddi"
]

print(sports[0:4])


# -------------------------------
# 8. More Slicing Examples
# -------------------------------

print("\n8)\n")

print(sports[:5])      # Starts from index 0
print(sports[1:])      # Goes till end

print(sports[-5:])
print(sports[:])

print(sports[::-1])    # Reverse the list


# -------------------------------
# 9. Slicing with Step
# -------------------------------
# Syntax:
# list[start:end:step]

print("\n9)\n")

print(sports[1::2])


# -------------------------------
# 10. Length of List
# -------------------------------
# len() returns total elements

print("\n10)\n")

print(len(sports))


# -------------------------------
# 11. append() Method
# -------------------------------
# Adds element at the end

print("\n11)\n")

li1 = [10, 20, 30, 40, 50]

print(li1)

li1.append(100)

print(li1)

li1.append("Python")

print(li1)


# -------------------------------
# 12. insert(), remove(), pop()
# -------------------------------

print("\n12)\n")

# insert(index, value)
li1.insert(0, 123)

print(li1)

# remove(value)
li1.remove(123)

print(li1)

# pop() removes last element
li1.pop()

print(li1)

# pop(index)
li1.pop(1)

print(li1)


# -------------------------------
# 13. Tuples
# -------------------------------
# Tuple →
# - Ordered
# - Immutable
# - Allows duplicates
# - Allows multiple datatypes

print("\n13)\n")

tup = (1, 2, 3, 4, 5, 5, 5)

print(tup)
print(type(tup))


# -------------------------------
# 14. Tuple with Multiple Datatypes
# -------------------------------

print("\n14)\n")

tup = (1, 2, 3 + 4j, "Python")

print(tup)
print(type(tup))


# -------------------------------
# 15. Single Element Tuple
# -------------------------------
# Comma is compulsory

print("\n15)\n")

t = (5,)

print(t)
print(type(t))


# -------------------------------
# 16. Tuple Indexing
# -------------------------------

print("\n16)\n")

t = (1, 2, 3, 4, 5, 6, 7, 100)

print(t[5])
print(t[-1])

print(len(t))

# Tuples are immutable
# t[2] = "Python" ❌


# -------------------------------
# 17. Tuple to List Conversion
# -------------------------------

print("\n17)\n")

print(t)

lst = list(t)

print(lst)


# -------------------------------
# 18. List to Tuple Conversion
# -------------------------------

print("\n18)\n")

lst = tuple(lst)

print(lst)