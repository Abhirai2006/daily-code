# =========================================
# Python Basics: Loops & Iteration
# =========================================


# -------------------------------
# 1. Difference between == and =
# -------------------------------
# =  → assignment operator (stores value)
# == → comparison operator (checks equality)

print("1)\n")

a = 12
b = 16

print("a == b:", a == b)  # Checks if values are equal


# -------------------------------
# 2. Introduction to Loops
# -------------------------------
# Loop → repeats a block of code multiple times
# Iteration → one cycle of a loop

print("\n2)\n")

# Types of loops in Python:
# 1. while loop
# 2. for loop


# -------------------------------
# 3. While Loop
# -------------------------------
# Runs as long as the condition is True

print("\n3)\n")

i = 1
while i <= 5:
    print(i)
    i = i + 1  # Important: update variable to avoid infinite loop


# -------------------------------
# 4. While Loop Variation
# -------------------------------

print("\n4)\n")

i = 1
while i <= 5:
    i = i + 1
    print(i)


# -------------------------------
# 5. Infinite Loop (Common Mistake)
# -------------------------------
# If you don't update the variable, loop runs forever

print("\n5)\n")

# Example (DO NOT RUN):
# i = 1
# while i <= 5:
#     print(i)
# → i never changes → infinite loop


# -------------------------------
# 6. For Loop
# -------------------------------
# Used when number of iterations is known

print("\n6)\n")

# range(n) → 0 to n-1
for i in range(5):
    print(i)


# range(start, stop)
for i in range(1, 6):
    print(i)


# -------------------------------
# 7. While vs For Loop
# -------------------------------

print("\n7)\n")

# While Loop:
# - Condition based
# - Manual update required
# - Risk of infinite loop

# For Loop:
# - Fixed number of iterations
# - Automatic iteration
# - Safer and cleaner


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