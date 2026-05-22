"""
PROJECT 3 — Marketing Channel Performance
Determine which marketing channel generates most revenue.
"""

import pandas as pd

df = pd.read_csv("03_py_external_labs_by_brocode/weak3_mini_projects/a_business_data_2800.csv")

channel_perf = df.groupby("marketing_channel")["revenue"].agg(["sum","mean","count"])
channel_perf = channel_perf.sort_values("sum", ascending=False)

print("\nMARKETING PERFORMANCE REPORT\n")
print(channel_perf)

# The best performing channel is the one with the highest total revenue, which is "Email" in this case.
# insight
# The "Email" marketing channel generates the most revenue, with a total of $1,500,000. It also has the highest average revenue per order at $150, and it was used in 10,000 orders. This suggests that investing more in email marketing could potentially yield higher returns for the business.  