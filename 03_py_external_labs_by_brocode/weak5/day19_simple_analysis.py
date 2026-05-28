"""
Revenue by price segment.
"""

import pandas as pd

df = pd.read_csv("03_py_external_labs_by_brocode/weak3_mini_projects/a_business_data_2800.csv")

bins = [0,50,200,500,2000]
labels = ["Low","Medium","High","Premium"]
df["price_segment"] = pd.cut(df["price"], bins=bins, labels=labels)

print(df.groupby("price_segment")["revenue"].sum())



