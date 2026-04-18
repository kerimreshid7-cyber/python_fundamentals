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



# so now i have understod every thing in function so lets do mini projet.

"""
MINI PROJECT — SALES DATA CLEANING & ANALYSIS PIPELINE

Author: Bilal Habesha
Goal:
    Simulate a real-world data analysis workflow:
    1) Validate raw data quality
    2) Clean and transform messy records
    3) Produce business insights

Dataset format per row:
    [customer_name, city, product, price, quantity]
"""

# --------------------------------------------------
# RAW DATA (Simulated messy export from company system)
# --------------------------------------------------

sales_data = [
    [" bilal ", "Addis Ababa", "Laptop", "45000", "1"],
    ["sara", "addis ababa", "Mouse", "800", "2"],
    ["mike", "Adama", "Keyboard", "", "1"],   # Missing price
    ["", "Adama", "Monitor", "12000", "1"],   # Missing customer name
    ["John", "ADDIS ABABA", "Laptop", "45000", "1"],
]


# --------------------------------------------------
# VALIDATION LAYER
# --------------------------------------------------

def is_valid_row(row: list) -> bool:
    """
    Validate a raw data row.

    Rules:
        - Customer name must exist
        - Price must exist

    Parameters
    ----------
    row : list
        Raw record from dataset.

    Returns
    -------
    bool
        True if row passes validation checks, False otherwise.
    """
    name, city, product, price, qty = row
    return name != "" and price != ""


# --------------------------------------------------
# TRANSFORMATION LAYER
# --------------------------------------------------

def clean_text(text: str) -> str:
    """
    Standardize text values.

    Operations:
        - Remove extra whitespace
        - Convert to title case

    Example:
        " addis ababa " → "Addis Ababa"
    """
    return text.strip().title()


def to_int(value: str) -> int:
    """
    Convert numeric string to integer.

    Raises ValueError if conversion fails.
    """
    return int(value)


def transform_row(row: list) -> list:
    """
    Convert a raw row into a clean structured record.

    Transformations:
        - Standardize text fields
        - Convert price and quantity to integers

    Returns
    -------
    list
        Cleaned row in same column order.
    """
    name, city, product, price, qty = row

    return [
        clean_text(name),
        clean_text(city),
        clean_text(product),
        to_int(price),
        to_int(qty)
    ]


# --------------------------------------------------
# PRESENTATION LAYER
# --------------------------------------------------

def show_clean_data(data: list) -> None:
    """
    Display cleaned dataset in readable format.
    """
    print("\nCLEAN DATASET")
    print("-" * 40)
    for row in data:
        print(row)


# --------------------------------------------------
# ANALYTICS LAYER
# --------------------------------------------------

def calculate_total_revenue(data: list) -> int:
    """
    Compute total revenue.

    Formula:
        revenue = price * quantity
    """
    total = 0
    for name, city, product, price, qty in data:
        total += price * qty
    return total


def revenue_by_city(data: list) -> dict:
    """
    Aggregate revenue grouped by city.

    Returns
    -------
    dict
        { city : total_revenue }
    """
    result = {}

    for name, city, product, price, qty in data:
        revenue = price * qty
        result[city] = result.get(city, 0) + revenue

    return result


# --------------------------------------------------
# PIPELINE ORCHESTRATOR
# --------------------------------------------------

def run_sales_pipeline(raw_data: list) -> None:
    """
    Main controller for the entire pipeline.

    Pipeline Steps:
        1) Validate raw data
        2) Transform valid records
        3) Display cleaned dataset
        4) Compute business metrics
    """

    # Step 1 — Validate
    valid_rows = [row for row in raw_data if is_valid_row(row)]

    # Step 2 — Transform
    clean_rows = [transform_row(row) for row in valid_rows]

    # Step 3 — Display cleaned dataset
    show_clean_data(clean_rows)

    # Step 4 — Business analytics
    total_revenue = calculate_total_revenue(clean_rows)
    city_sales = revenue_by_city(clean_rows)

    print("\nBUSINESS INSIGHTS")
    print("-" * 40)
    print("Total Revenue:", total_revenue)
    print("Revenue by City:", city_sales)


# --------------------------------------------------
# EXECUTION ENTRY POINT
# --------------------------------------------------

if __name__ == "__main__":
    run_sales_pipeline(sales_data)