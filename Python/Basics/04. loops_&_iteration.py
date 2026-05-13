# =========================================
# Python Basics: Loops & Iteration
# =========================================


# -------------------------------
# 1. Difference between == and =
# -------------------------------
# =  → assignment operator
# == → comparison operator

print("1)\n")

a = 12
b = 16

print("a == b:", a == b)


# -------------------------------
# 2. Introduction to Loops
# -------------------------------
# Loop → repeats a block of code
# Iteration → one cycle of a loop

print("\n2)\n")

# Types of loops in Python:
# 1. while loop
# 2. for loop


# -------------------------------
# 3. While Loop
# -------------------------------
# Runs as long as condition is True

print("\n3)\n")

i = 1

while i <= 5:
    print(i)
    i += 1


# -------------------------------
# 4. While Loop Variation
# -------------------------------

print("\n4)\n")

i = 1

while i <= 5:
    i += 1
    print(i)


# -------------------------------
# 5. Infinite Loop (Common Mistake)
# -------------------------------
# Forgetting to update variable

print("\n5)\n")

# Example (DO NOT RUN)
# i = 1
# while i <= 5:
#     print(i)

# → Infinite loop because i never changes


# -------------------------------
# 6. For Loop
# -------------------------------
# Used when iteration count is known

print("\n6)\n")

# range(n) → starts from 0
for i in range(5):
    print(i)

print()

# range(start, stop)
for i in range(1, 6):
    print(i)


# -------------------------------
# 7. While vs For Loop
# -------------------------------

print("\n7)\n")

# While Loop:
# - Condition based
# - Manual update needed
# - Can become infinite

# For Loop:
# - Fixed iteration count
# - Automatic iteration
# - Cleaner for counting loops


# -------------------------------
# 8. Even Numbers (1 to 20)
# -------------------------------

print("\n8)\n")

for i in range(2, 21, 2):
    print(i)

# range(start, stop, step)


# -------------------------------
# 9. Reverse Loop
# -------------------------------

print("\n9)\n")

for i in range(10, 0, -1):
    print(i)


# -------------------------------
# 10. Repeating a Task
# -------------------------------

print("\n10)\n")

for i in range(3):
    print("Python")


# -------------------------------
# 11. Loop Control Statements
# -------------------------------
# break and continue

print("\n11)\n")

# break → immediately stops the loop

print("Break in for loop:")

for i in range(1, 10):
    if i == 5:
        break
    print(i)

print()

# break in while loop
num = 1

while num <= 10:
    if num == 6:
        break

    print(num)
    num += 1


# -------------------------------
# 12. Continue Statement
# -------------------------------
# continue → skips current iteration

print("\n12)\n")

print("Continue in for loop:")

for i in range(1, 6):
    if i == 3:
        continue

    print(i)

print()

print("Continue in while loop:")

num = 0

while num < 5:
    num += 1

    if num == 3:
        continue

    print(num)