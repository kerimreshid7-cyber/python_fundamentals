"""
PROJECT 2 — Customer Segmentation
Identify high value customers.
"""

import pandas as pd

df = pd.read_csv("03_py_external_labs_by_brocode/weak3_mini_projects/a_business_data_2800.csv")

customer_value = df.groupby("customer_id")["revenue"].sum()
top_customers = customer_value.sort_values(ascending=False).head(10)

print("\nTOP 10 CUSTOMERS")
print(top_customers)