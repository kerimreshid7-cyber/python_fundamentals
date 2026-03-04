# BI Mini Project to practice Variables, Data Types (int, float/double, string, boolean),
#  Lists,dictionaries,opratores,comparisions,conditional statments  and for loop.

# -----------------------------
# Variables and Data Types
# -----------------------------
# Individual sales items
date1 = "2026-01-01"          # string
region1 = "Addis Ababa"       # string
product1 = "Electronics"      # string
units_sold1 = 20              # int(integer)
unit_price1 = 500.0           # float/double

date2 = "2026-01-01"
region2 = "Addis Ababa"
product2 = "Furniture"
units_sold2 = 10
unit_price2 = 1200.0

date3 = "2026-01-01"
region3 = "Dire Dawa"
product3 = "Electronics"
units_sold3 = 15
unit_price3 = 500.0

# -----------------------------
# Lists
# -----------------------------
dates = [date1, date2, date3]
regions = [region1, region2, region3]
products = [product1, product2, product3]
units_sold = [units_sold1, units_sold2, units_sold3]
unit_prices = [unit_price1, unit_price2, unit_price3]

# -----------------------------
# Challenge 1: Revenue per item (variables + float)
# -----------------------------
revenue1 = units_sold1 * unit_price1
revenue2 = units_sold2 * unit_price2
revenue3 = units_sold3 * unit_price3

print("Revenue per item:")
print(revenue1, revenue2, revenue3)

# -----------------------------
# Challenge 2: High sale flag (boolean)
# -----------------------------
is_high_sale1 = units_sold1 > 20
is_high_sale2 = units_sold2 > 20
is_high_sale3 = units_sold3 > 20

print("\nHigh Sale Flag (units > 20):")
print(is_high_sale1, is_high_sale2, is_high_sale3)

# -----------------------------
# Challenge 3: Total revenue (variables + double)
# -----------------------------
total_revenue = revenue1 + revenue2 + revenue3
print("\nTotal Revenue:", total_revenue)

# -----------------------------
# Challenge 4: Average unit price per product (lists + float)
# -----------------------------
# We have only 2 products: Electronics and Furniture
avg_price_electronics = (unit_price1 + unit_price3) / 2
avg_price_furniture = unit_price2  # only one value

print("\nAverage Unit Price:")
print("Electronics:", avg_price_electronics)
print("Furniture:", avg_price_furniture)

# -----------------------------
# Challenge 5: Units sold list summary (lists + int)
# -----------------------------
total_units_sold_list = [units_sold1, units_sold2, units_sold3]
sum_units = total_units_sold_list[0] + total_units_sold_list[1] + total_units_sold_list[2]

print("\nTotal Units Sold (sum of list):", sum_units)



  #Challenge  — Growth Rate
#Scenario:
# Last_month_sales = 80000
# This_month_sales = 92000
#Step 1: Calculate growth rate
# Formula:
# (New-Old)/Old
old = 80000
new = 92000
growth = (new - old) / old
print("this is the actual growth rate",growth * 100,"bc mathimatics has always  been truth.")


#  Challenge 5 — Contribution Percentage
# Scenario:
# Total sales = 100000
# Electronics sales = 35000
   #step 1 defining the variables
total_sales=100000
Electronics_sales=35000
  #step 2 formula 
contributio=Electronics_sales*100/total_sales
print("Electronics sales contribute",contributio,"% the total sales.")
# 50000,
#     "Branch B": 30000,
#     "Branch C": 70000
# }
# Challenge 6 — Find Underperforming Branch (to examine dictionary concepts)
    # Target = 40000
sales={
     "bole_branch":50000,
     "akaki_branch":30000,
     "piassa_branch":70000
}
# here i have understod when we make dictionaries we have to define the data type by default 
# like  "piassa_branch":70000 if we write piassa_branch:70000  it doesn't read because of syntax error.

target = 40000

for branch in sales:
    if sales[branch] > target:
        print(branch, "is over performing")
    elif sales [branch] < target:
        print(branch, "is underperforming")
    else:print("none")


#     Challenge 7 — Manual Average Order Value
# Total revenue = 120000
# Total orders = 3000
Total_revenue=120000
Total_orders = 3000
MAOV=Total_revenue/Total_orders
print("the Manual Average Order Value is",MAOV)


