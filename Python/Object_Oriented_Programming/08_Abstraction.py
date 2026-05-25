# =========================================
# Python OOPs: Abstraction
# =========================================

# In this file, we will learn:
# - Abstraction
# - Abstract Classes
# - Abstract Methods
# - ABC Module
# - Hiding Internal Implementation


# =========================================
# What is Abstraction?
# =========================================

# Abstraction means:
# Hiding internal implementation details
# and showing only the essential features
# to the user.

# The user only knows:
# - What to do

# The user does not need to know:
# - How it works internally


# =========================================
# Real World Example
# =========================================

# ATM Machine:
# We only:
# - Insert card
# - Enter PIN
# - Withdraw money

# We do not know:
# - Server communication
# - Database operations
# - Security checks

# This is abstraction.


# =========================================
# Simple Example Without Abstraction
# =========================================

def send_email():
    print("Connecting To Server...")
    print("Authenticating User...")
    print("Sending Email...")


# ----- Sending Email -----

print("\n----- Sending Email -----")
send_email()

# User only calls:
# send_email()

# Internal implementation is hidden.

