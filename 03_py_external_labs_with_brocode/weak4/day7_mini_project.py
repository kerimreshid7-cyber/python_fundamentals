# hello how are you today? we will be working on a mini project that analyzes business data. 


"""
PROJECT 4 — Product Category Analysis
Find best selling product categories.
"""

import pandas as pd

df = pd.read_csv("03_py_external_labs_by_brocode/weak3_mini_projects/a_business_data_2800.csv")

category = df.groupby("product_category")["revenue"].agg(["sum","mean","count"])
category = category.sort_values("sum", ascending=False)

print("\nCATEGORY PERFORMANCE\n")
print(category)

# Insights:
# • Top revenue category
# • Weak categories needing strategy