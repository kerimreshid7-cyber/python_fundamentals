# TYPES OF FUNCTIONS BASED ON THEIR WORK (ROLE)
# Action | Validator | Transformer | Orchestrator


# 1) ACTION FUNCTIONS
# Short note:
# Do something in the real world.
# Produce side effects like printing, saving, sending.
# Usually do NOT return a value.


# Example 1 — ATM receipt printer
def print_receipt(amount):
    print("Transaction successful")
    print("Withdrawn:", amount, "Birr")

# Example call
print_receipt(500)

# Expected Output:
# Transaction successful
# Withdrawn: 500 Birr



# Example 2 — Football goal announcement
def announce_goal(player):
    print("GOAL!!!")
    print(player, "scored the goal!")

announce_goal("Messi")

# Expected Output:
# GOAL!!!
# Messi scored the goal!



# 2) VALIDATOR FUNCTIONS
# Short note:
# Check rules and return True or False.


# Example 1 — Password strength checker
def is_password_strong(password):
    return len(password) >= 8

print(is_password_strong("abc"))
print(is_password_strong("abc12345"))

# Expected Output:
# False
# True



# Example 2 — Age validation for cinema
def can_watch_movie(age):
    return age >= 18

print(can_watch_movie(16))
print(can_watch_movie(21))

# Expected Output:
# False
# True



# 3) TRANSFORMER FUNCTIONS
# Short note:
# Take data → modify → return new improved data.


# Example 1 — Username formatter
def format_username(name):
    return name.strip().title()

print(format_username("   bilal habesha  "))

# Expected Output:
# Bilal Habesha



# Example 2 — Currency converter
def birr_to_dollar(birr):
    rate = 0.018
    return birr * rate

print(birr_to_dollar(1000))

# Expected Output:
# 18.0



# 4) ORCHESTRATOR FUNCTIONS
# Short note:
# Manager function that calls other functions
# and controls full workflow.


# --- small helper functions ---
def validate_payment():
    print("Payment verified")

def cook_food():
    print("Food is being prepared")

def assign_driver():
    print("Driver assigned")

def send_confirmation():
    print("Customer notified")


# --- ORCHESTRATOR ---
def place_order():
    validate_payment()
    cook_food()
    assign_driver()
    send_confirmation()

place_order()

# Expected Output:
# Payment verified
# Food is being prepared
# Driver assigned
# Customer notified



# Example 2 — University admission workflow
def check_grades():
    print("Grades checked")

def check_documents():
    print("Documents verified")

def send_acceptance():
    print("Acceptance email sent")

def admission_process():
    check_grades()
    check_documents()
    send_acceptance()

admission_process()

# Expected Output:
# Grades checked
# Documents verified
# Acceptance email sent


# MEMORY SUMMARY
# Action      → Do something
# Validator   → Check something (True/False)
# Transformer → Change data and return new value
# Orchestrator→ Control full process (call many functions)
