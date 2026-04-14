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

print()
# Expected Output:
# Transaction successful
# Withdrawn: 500 Birr



# Example 2 — Football goal announcement
def announce_goal(player):
    print("GOAL!!!")
    print(player, "scored the goal!")

announce_goal("Ronaldo")

print()

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

print()

# Expected Output:
# False
# True



# Example 2 — Age validation for cinema
def can_watch_movie(age):
    return age >= 18

print(can_watch_movie(16))
print(can_watch_movie(21))

print()

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

print()

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



# so now i have understod every thing in function so lets do mini projet now.

# MINI PROJECT — SALES DATA CLEANING & ANALYSIS PIPELINE
# Goal:
# Clean messy sales data and calculate business insights.

# RAW DATA (Messy dataset from "company system")
# Each row = [customer_name, city, product, price, quantity]


sales_data = [
    [" bilal ", "Addis Ababa", "Laptop", "45000", "1"],
    ["sara", "addis ababa", "Mouse", "800", "2"],
    ["mike", "Adama", "Keyboard", "", "1"],   # bad price
    ["", "Adama", "Monitor", "12000", "1"],   # missing name
    ["John", "ADDIS ABABA", "Laptop", "45000", "1"],
]


# VALIDATOR FUNCTION
# Check if row is usable (data quality check)

def is_valid_row(row):
    name, city, product, price, qty = row
    
    if name == "":
        return False
    if price == "":
        return False
    
    return True

# TRANSFORMER FUNCTIONS
# Clean text and convert numbers

def clean_text(text):
    return text.strip().title()

def to_int(value):
    return int(value)

def transform_row(row):
    name, city, product, price, qty = row
    
    name = clean_text(name)
    city = clean_text(city)
    product = clean_text(product)
    price = to_int(price)
    qty = to_int(qty)
    
    return [name, city, product, price, qty]

# ACTION FUNCTION
# Show cleaned dataset

def show_clean_data(data):
    print("\nCLEAN DATA:")
    for row in data:
        print(row)


# ANALYSIS FUNCTIONS (Computation)

def calculate_total_revenue(data):
    total = 0
    for row in data:
        price = row[3]
        qty = row[4]
        total += price * qty
    return total


def revenue_by_city(data):
    result = {}
    
    for row in data:
        city = row[1]
        price = row[3]
        qty = row[4]
        revenue = price * qty
        
        if city not in result:
            result[city] = 0
        
        result[city] += revenue
    
    return result

# ORCHESTRATOR FUNCTION (MAIN PIPELINE)
# Controls full workflow step-by-step

def run_sales_pipeline(raw_data):
    
    # 1) VALIDATE DATA
    valid_rows = []
    for row in raw_data:
        if is_valid_row(row):
            valid_rows.append(row)
    
    # 2) TRANSFORM DATA
    clean_rows = []
    for row in valid_rows:
        clean_rows.append(transform_row(row))
    
    # 3) SHOW CLEAN DATA
    show_clean_data(clean_rows)
    
    # 4) ANALYSE DATA
    total = calculate_total_revenue(clean_rows)
    city_sales = revenue_by_city(clean_rows)
    
    print("\nTOTAL REVENUE:", total)
    print("\nREVENUE BY CITY:")
    print(city_sales)


# here we go we are about to run the project

run_sales_pipeline(sales_data)