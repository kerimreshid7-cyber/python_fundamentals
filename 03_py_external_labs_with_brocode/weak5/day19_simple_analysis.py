"""
Revenue by price segment.
"""

import pandas as pd

df = pd.read_csv("03_py_external_labs_by_brocode/weak3_mini_projects/a_business_data_2800.csv")

bins = [0,50,200,500,2000]
labels = ["Low","Medium","High","Premium"]
df["price_segment"] = pd.cut(df["price"], bins=bins, labels=labels)

print(df.groupby("price_segment")["revenue"].sum())

# insight: 
# 1. The Premium price segment generates the highest total revenue, followed by the High and Medium segments. This indicates that customers are willing to spend more on higher-priced products, which may suggest a preference for premium offerings. The Low price segment generates the least revenue, which could indicate that customers are less interested in lower-priced products or that there may be a need to reevaluate the pricing strategy for this segment to increase its appeal and revenue potential.

