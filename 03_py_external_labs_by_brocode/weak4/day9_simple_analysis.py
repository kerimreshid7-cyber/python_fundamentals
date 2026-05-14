"""
PROJECT 5 — Delivery vs Returns Analysis
Check if slow delivery increases returns.
"""

import pandas as pd

df = pd.read_csv("03_py_external_labs_by_brocode/weak3_mini_projects/a_business_data_2800.csv")

returns = df.groupby("returned")["delivery_days"].mean()

print("\nDELIVERY IMPACT REPORT")
print("Avg delivery (not returned):", returns[0])
print("Avg delivery (returned):", returns[1])

# Insights:
# • Logistics impact on customer satisfaction
# • Potential for improving delivery times to reduce returns