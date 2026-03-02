# BI Mini Project: Variables, Data Types (int, float/double, string, boolean), Lists
# NO loops, NO functions, only direct assignment and basic operations

# -----------------------------
# Variables and Data Types
# -----------------------------
# Individual sales items
date1 = "2026-01-01"          # string
region1 = "Addis Ababa"       # string
product1 = "Electronics"      # string
units_sold1 = 20              # int
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