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
# The significant growth in the first month could be attributed to various factors such as a successful marketing campaign, seasonal demand, or the launch of a new product. The decline in the second month might be due to market saturation, increased competition, or changes in consumer behavior. The recovery in the third month suggests that the business may have implemented effective strategies to address the decline, but it will be important to continue monitoring revenue growth and identifying areas for improvement to ensure long-term success.