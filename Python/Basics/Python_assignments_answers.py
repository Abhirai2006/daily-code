# =========================================
# Python Assignment Solutions
# =========================================


# -------------------------------------------------
# Q1. Voting Eligibility Checker
# -------------------------------------------------
# Take age as input and check whether
# the person is eligible to vote or not.

age = int(input("Enter your age: "))

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")


# -------------------------------------------------
# Q2. Set Operations
# -------------------------------------------------
# Perform union, intersection and difference.

set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Union → combines all unique elements
print("Union:", set1 | set2)

# Intersection → common elements
print("Intersection:", set1 & set2)

# Difference → elements present only in first set
print("set1 - set2:", set1 - set2)

print("set2 - set1:", set2 - set1)


# -------------------------------------------------
# Q3. Reverse a String
# -------------------------------------------------
# Reverse string using slicing.

name = input("Enter a string: ")

# [::-1] reverses the string
print("Reversed String:", name[::-1])


# -------------------------------------------------
# Q4. Palindrome Checker
# -------------------------------------------------
# Check whether string reads same
# forward and backward.

text = input("Enter a word: ")

# Compare original string with reversed string
if text == text[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")


# -------------------------------------------------
# Q5. Greatest Among Three Numbers
# -------------------------------------------------
# Find largest among 3 numbers.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a > b and a > c:
    print("Greatest Number:", a)

elif b > a and b > c:
    print("Greatest Number:", b)

else:
    print("Greatest Number:", c)


# -------------------------------------------------
# Q6. Prime Numbers from 1 to 20
# -------------------------------------------------
# Print all prime numbers between 1 and 20.

for num in range(2, 21):

    # Assume number is prime
    prime = True

    # Check divisibility
    for i in range(2, num):

        # If divisible → not prime
        if num % i == 0:
            prime = False
            break

    # Print only prime numbers
    if prime:
        print(num)


# -------------------------------------------------
# Q7. Lambda + Map Practice
# -------------------------------------------------
# Add 10 to every element using map() and lambda.

numbers = [2, 3, 4, 5, 6]

# map() applies operation to every element
updated_numbers = list(map(lambda x: x + 10, numbers))

print(updated_numbers)


# -------------------------------------------------
# Q8. Sum of Digits
# -------------------------------------------------
# Find sum of all digits in a number.

num = int(input("Enter a number: "))

total = 0

while num > 0:

    # Get last digit
    digit = num % 10

    # Add digit to total
    total += digit

    # Remove last digit
    num //= 10

print("Sum of digits:", total)


# -------------------------------------------------
# Q9. Count Digits in a Number
# -------------------------------------------------
# Count total digits present in number.

num = int(input("Enter a number: "))

count = 0

while num != 0:

    # Remove last digit
    num //= 10

    # Increase counter
    count += 1

print("Total digits:", count)


# -------------------------------------------------
# Q10. Count Vowels in a String
# -------------------------------------------------
# Count vowels present in string.

word = input("Enter a word: ")

count = 0

# lower() converts everything to lowercase
for ch in word.lower():

    # Check if character is vowel
    if ch in "aeiou":
        count += 1

print("Number of vowels:", count)


# -------------------------------------------------
# Q11. Anagram Checker
# -------------------------------------------------
# Check whether two strings are anagrams.

s1 = input("Enter first word: ").lower()
s2 = input("Enter second word: ").lower()

# Sort both strings and compare
if sorted(s1) == sorted(s2):
    print("Anagram")

else:
    print("Not Anagram")


# -------------------------------------------------
# Q12. Sum of Elements in a List
# -------------------------------------------------
# Function that returns sum of list elements.

def list_sum(lst):

    total = 0

    for i in lst:
        total += i

    return total


numbers = [10, 20, 30, 40]

result = list_sum(numbers)

print("Sum of list elements:", result)


# -------------------------------------------------
# Q13. Sum of User Input List Elements
# -------------------------------------------------
# Store numbers inside list and find sum.

n = int(input("How many numbers: "))

numbers = []

# Take list input from user
for i in range(n):

    x = int(input("Enter number: "))
    numbers.append(x)


def list_sum(lst):

    total = 0

    for i in lst:
        total += i

    return total


print("Total Sum:", list_sum(numbers))


# -------------------------------------------------
# Q14. Reverse a Number
# -------------------------------------------------
# Reverse integer input.

num = int(input("Enter a number: "))

reverse = 0

while num > 0:

    # Extract last digit
    digit = num % 10

    # Build reversed number
    reverse = reverse * 10 + digit

    # Remove last digit
    num //= 10

print("Reversed Number:", reverse)


# -------------------------------------------------
# Q15. Armstrong Number Checker
# -------------------------------------------------
# Check whether number is Armstrong or not.

num = int(input("Enter a number: "))

temp = num

# Count total digits
n = len(str(num))

total = 0

while temp > 0:

    # Extract last digit
    digit = temp % 10

    # Add power of digit
    total += digit ** n

    # Remove last digit
    temp //= 10


if total == num:
    print("Armstrong Number")

else:
    print("Not an Armstrong Number")


# -------------------------------------------------
# Q16. Frequency of Elements in a List
# -------------------------------------------------
# Count occurrence of each element.

numbers = [1, 2, 2, 3, 3, 3, 4, 4]

frequency = {}

for i in numbers:

    # If already present → increase count
    if i in frequency:
        frequency[i] += 1

    # Otherwise create new entry
    else:
        frequency[i] = 1


# Print frequency dictionary
for key, value in frequency.items():
    print(key, "→", value)


# -------------------------------------------------
# Q17. Character Frequency Counter
# -------------------------------------------------
# Count how many times each character appears.

text = input("Enter a string: ")

frequency = {}

for ch in text:

    if ch in frequency:
        frequency[ch] += 1

    else:
        frequency[ch] = 1


for key, value in frequency.items():
    print(key, "→", value)


# -------------------------------------------------
# Q18. Student Marks Analysis
# -------------------------------------------------
# Find average marks and topper.

marks = {
    "Rahul": 85,
    "Anita": 90,
    "Adarsh": 89,
    "Lalit": 75
}

total = 0
highest = 0
top_student = ""

for name, score in marks.items():

    # Add marks to total
    total += score

    # Check highest marks
    if score > highest:
        highest = score
        top_student = name


# Calculate average
average = total / len(marks)

print("Average Marks:", average)

print("Top Student:", top_student)


# -------------------------------------------------
# Q19. Longest Word in a List
# -------------------------------------------------
# Find longest word from list.

words = [
    "python",
    "apple",
    "machine",
    "programming"
]

# Assume first word is longest
longest = words[0]

for word in words:

    # Compare word lengths
    if len(word) > len(longest):
        longest = word

print("Longest Word:", longest)


# -------------------------------------------------
# Q20. Sorting Words using Lambda
# -------------------------------------------------
# Sort words based on length.

words = [
    "python",
    "apple",
    "machine",
    "programming"
]

# key decides sorting rule
result = sorted(words, key=lambda x: len(x))

print(result)


# -------------------------------------------------
# Q21. Find Duplicate Elements in a List
# -------------------------------------------------
# Find duplicate elements from list.

data = [1, 1, 2, 2, 3, 4, 4, 5]

duplicates = []

for i in data:

    # Check if element appears more than once
    if data.count(i) > 1 and i not in duplicates:

        duplicates.append(i)

print("Duplicate Elements:", duplicates)