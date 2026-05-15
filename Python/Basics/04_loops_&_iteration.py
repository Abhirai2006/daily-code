# =========================================
# Python Basics: Loops & Iteration
# =========================================


# -------------------------------
# 1. Difference Between = and ==
# -------------------------------
# =  → assignment operator
# == → comparison operator

print("\n===== Assignment vs Comparison Operator =====")

a = 12
b = 16

print(f"a = {a}")
print(f"b = {b}")

print(f"a == b → {a == b}")


# -------------------------------
# 2. Introduction to Loops
# -------------------------------
# Loop → repeats a block of code
# Iteration → one cycle of a loop

print("\n===== Introduction to Loops =====")

print("Python mainly has two loops:")
print("1. while loop")
print("2. for loop")


# -------------------------------
# 3. While Loop
# -------------------------------
# Runs as long as condition is True

print("\n===== While Loop =====")

i = 1

while i <= 5:
    print(f"Current Value: {i}")
    i += 1


# -------------------------------
# 4. While Loop Variation
# -------------------------------

print("\n===== While Loop Variation =====")

i = 1

while i <= 5:
    i += 1
    print(f"Updated Value: {i}")


# -------------------------------
# 5. Infinite Loop
# -------------------------------
# Forgetting to update variable
# can create an infinite loop

print("\n===== Infinite Loop Example =====")

# Example (DO NOT RUN)

# i = 1
# while i <= 5:
#     print(i)

print("Infinite loop occurs when loop variable never changes.")


# -------------------------------
# 6. For Loop
# -------------------------------
# Used when iteration count is known

print("\n===== For Loop =====")

print("Using range(5):")

for i in range(5):
    print(f"Value of i: {i}")

print("\nUsing range(1, 6):")

for i in range(1, 6):
    print(f"Value of i: {i}")


# -------------------------------
# 7. While Loop vs For Loop
# -------------------------------

print("\n===== While Loop vs For Loop =====")

print("While Loop:")
print("- Condition based")
print("- Manual update required")
print("- Can become infinite")

print("\nFor Loop:")
print("- Fixed iteration count")
print("- Automatic iteration")
print("- Cleaner for counting")


# -------------------------------
# 8. Even Numbers from 1 to 20
# -------------------------------

print("\n===== Even Numbers from 1 to 20 =====")

for i in range(2, 21, 2):
    print(i)

# range(start, stop, step)


# -------------------------------
# 9. Reverse Loop
# -------------------------------

print("\n===== Reverse Counting =====")

for i in range(10, 0, -1):
    print(i)


# -------------------------------
# 10. Repeating a Task
# -------------------------------

print("\n===== Repeating a Task =====")

for i in range(3):
    print("Python")


# -------------------------------
# 11. break Statement
# -------------------------------
# break immediately stops the loop

print("\n===== break Statement =====")

print("Break in for loop:")

for i in range(1, 10):

    if i == 5:
        break

    print(i)

print("\nBreak in while loop:")

num = 1

while num <= 10:

    if num == 6:
        break

    print(num)

    num += 1


# -------------------------------
# 12. continue Statement
# -------------------------------
# continue skips current iteration

print("\n===== continue Statement =====")

print("Continue in for loop:")

for i in range(1, 6):

    if i == 3:
        continue

    print(i)

print("\nContinue in while loop:")

num = 0

while num < 5:

    num += 1

    if num == 3:
        continue

    print(num)