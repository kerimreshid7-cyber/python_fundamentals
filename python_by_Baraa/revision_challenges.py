


# challenge 1 — CLEAN SALES DATA
# A shop exported messy sales data from its system.
# Clean the data and analyse it.

sales = ["$1200", "850$", "NaN", "$300", "400$", "", "$1,200"]

# TASKS
# 1 Remove empty values and "NaN"
# 2 Remove "$" and commas
# 3 Convert values to integers
# 4 Print:
#    - Total revenue
#    - Average sale
#    - Highest sale


# challenge 2 — TOP SPENDING CUSTOMER
# Transactions from a small online store

transactions = [
    ("Ali", 120),
    ("John", 300),
    ("Ali", 250),
    ("Sara", 400),
    ("John", 150),
]

# TASKS
# 1 Calculate total spending per customer
# 2 Find the customer who spent the most
# 3 Sort customers from highest spender to lowest


# challenge 3 — EMAIL DUPLICATE DETECTOR
# User registration emails

emails = [
 "a@gmail.com",
 "b@gmail.com",
 "a@gmail.com",
 "c@gmail.com",
 "b@gmail.com",
 "d@gmail.com"
]

# TASKS
# 1 Create list of unique emails
# 2 Create list of duplicate emails
# 3 Count how many times each email appears
# challenge 4 — WEBSITE TRAFFIC ANALYSIS


# Daily website visits for 10 days

visits = [5,7,3,10,12,6,8,15,2,9]

# TASKS
# Print:
# 1 Total visits
# 2 Average visits
# 3 Highest traffic day value
# 4 Number of days above average
# challenge 5 — FILTER VALID USERS


# App users data

users = [
 {"name":"Ali","age":25},
 {"name":"Sara","age":17},
 {"name":"John","age":30},
 {"name":"Mike","age":15},
 {"name":"Lina","age":22}
]

# TASKS
# 1 Keep only users age >= 18
# 2 Create list of valid user names
# 3 Print number of valid users

# challenge 6 — PRODUCT PRICE ANALY# Store inventory prices

products = {
 "Laptop":1200,
 "Phone":800,
 "Tablet":450,
 "Monitor":300,
 "Keyboard":150
}

# TASKS
# 1 Find most expensive product
# 2 Find cheapest product
# 3 Calculate total inventory value


# challenge 7 — WORD FREQUENCY ANAL
# Product reviews text

text = "python is easy and python is powerful and python is fun"

# TASKS
# 1 Count total words
# 2 Count unique words
# 3 Find most common word
# 3 REAL LIFE MINI PROJECTS (COPY-PASTE READY)

# These are portfolio projects.


# PROJECT 1 — SUPERMARKET SALES ANALYZER
sales = [
 {"date":"2024-01-01","product":"Milk","price":3,"qty":10},
 {"date":"2024-01-01","product":"Bread","price":2,"qty":20},
 {"date":"2024-01-02","product":"Milk","price":3,"qty":5},
 {"date":"2024-01-02","product":"Eggs","price":4,"qty":12},
 {"date":"2024-01-03","product":"Bread","price":2,"qty":15},
]

# BUILD FUNCTIONS THAT RETURN:
# 1 total_revenue()
# 2 revenue_per_product()
# 3 best_selling_product()
# 4 revenue_per_day()
# 5 average_daily_revenue()


# PROJECT 2 — CUSTOMER BEHAVIOUR ANALYSIS
customers = [
 {"name":"Ali","city":"Addis","spent":1200},
 {"name":"Sara","city":"Adama","spent":800},
 {"name":"John","city":"Addis","spent":1500},
 {"name":"Mike","city":"Adama","spent":400},
 {"name":"Lina","city":"BahirDar","spent":900},
]

# BUILD FUNCTIONS THAT RETURN:
# 1 total_revenue()
# 2 revenue_by_city()
# 3 city_with_most_customers()
# 4 top_3_customers()
# 5 average_customer_spending()



# PROJECT 3 — EMPLOYEE SALARY ANALYTICS
employees = [
 {"name":"A","dept":"IT","salary":1200},
 {"name":"B","dept":"HR","salary":800},
 {"name":"C","dept":"IT","salary":1500},
 {"name":"D","dept":"Sales","salary":900},
 {"name":"E","dept":"IT","salary":1100},
]

# BUILD FUNCTIONS THAT RETURN:
# 1 average_salary()
# 2 highest_and_lowest_salary()
# 3 salary_by_department()
# 4 department_with_highest_payroll()
# 5 salary_percentage_by_department()