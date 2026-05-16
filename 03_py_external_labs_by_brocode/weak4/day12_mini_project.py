"""
Customer Loyalty Analysis
Measures repeat purchase behaviour.
"""

import pandas as pd

df = pd.read_csv("03_py_external_labs_by_brocode/weak3_mini_projects/a_business_data_2800.csv")
orders = df.groupby("customer_id")["order_id"].count()

repeat = (orders > 1).sum()
single = (orders == 1).sum()

print("\nCUSTOMER LOYALTY REPORT")
print("Repeat Customers:", repeat)
print("One-time Customers:", single)

# insights
# The analysis of customer loyalty reveals that there is a significant number of repeat customers, which indicates