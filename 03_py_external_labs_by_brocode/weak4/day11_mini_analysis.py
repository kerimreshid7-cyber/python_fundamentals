"""
Monthly Revenue Growth Report
Measures how revenue changes month to month.
"""

import pandas as pd

df = pd.read_csv("03_py_external_labs_by_brocode/weak3_mini_projects/a_business_data_2800.csv")
df["order_date"] = pd.to_datetime(df["order_date"])
df["month"] = df["order_date"].dt.to_period("M")

monthly = df.groupby("month")["revenue"].sum()
growth = monthly.pct_change() * 100

print("\nMONTHLY REVENUE GROWTH (%)\n")
print(growth.dropna())