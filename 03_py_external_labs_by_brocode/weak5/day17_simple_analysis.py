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
