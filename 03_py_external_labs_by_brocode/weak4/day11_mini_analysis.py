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

# insights
# I have understood that the business had a significant growth in revenue in the first month, followed by a decline in the second month. The third month showed a recovery with a positive growth rate, but it was not as high as the first month. This indicates that while there was an initial surge in revenue, it was not sustained, and the business may need to analyze the factors contributing to the decline and recovery to develop strategies for consistent growth.
