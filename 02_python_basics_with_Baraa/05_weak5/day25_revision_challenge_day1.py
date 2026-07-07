
# I have finished every thing in video Barra is absolutly different i mean his experiance the way he understand concepts the way he teaches he explain
# his flow of learning something the raod map he is something special he helped me alot. i am thinking like data analyst some steps for my dream.

# I give a shot to revise everything practically by doing real life chalenges and some mini projects.



# here we go

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

sales = ["$1200", "850$", "NaN", "$300", "400$", "", "$1,200"]

clean_sales = []

for s in sales:
    if s != "" and s != "NaN":
        s = s.replace("$","").replace(",","")
        clean_sales.append(int(s))

total_revenue = sum(clean_sales)
average_sale = total_revenue / len(clean_sales)
highest_sale = max(clean_sales)

print("Total:", total_revenue)
print("Average:", average_sale)
print("Highest:", highest_sale)

print()

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

transactions = [
    ("Ali",120),
    ("John",300),
    ("Ali",250),
    ("Sara",400),
    ("John",150),
]

spending = {}

for name, amount in transactions:
    spending[name] = spending.get(name,0) + amount

top_spender = max(spending, key=spending.get)
sorted_customers = sorted(spending.items(), key=lambda x:x[1], reverse=True)

print(spending)
print("Top:", top_spender)
print("Sorted:", sorted_customers)

print()


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

emails = ["a@gmail.com","b@gmail.com","a@gmail.com","c@gmail.com","b@gmail.com","d@gmail.com"]

unique_emails = list(set(emails))

count = {}
for e in emails:
    count[e] = count.get(e,0) + 1

duplicates = [email for email, c in count.items() if c > 1]

print("Unique:", unique_emails)
print("Duplicates:", duplicates)
print("Count:", count)

print()


# challenge 4 — WEBSITE TRAFFIC ANALYSIS
# Daily website visits for 10 days

visits = [5,7,3,10,12,6,8,15,2,9]

# TASKS
# Print:
# 1 Total visits
# 2 Average visits
# 3 Highest traffic day value
# 4 Number of days above average

visits = [5,7,3,10,12,6,8,15,2,9]

total = sum(visits)
avg = total / len(visits)
highest = max(visits)
above_avg_days = len([v for v in visits if v > avg])

print(total, avg, highest, above_avg_days)

print()


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

valid_users = [u for u in users if u["age"] >= 18]
names = [u["name"] for u in valid_users]

print(valid_users)
print(names)
print(len(valid_users))
