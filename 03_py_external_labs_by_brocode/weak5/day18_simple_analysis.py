"""
Day-of-week performance.
"""

import pandas as pd

df = pd.read_csv("03_py_external_labs_by_brocode/weak3_mini_projects/a_business_data_2800.csv")
df["order_date"] = pd.to_datetime(df["order_date"])
df["weekday"] = df["order_date"].dt.day_name()

print(df.groupby("weekday")["revenue"].sum().sort_values(ascending=False))