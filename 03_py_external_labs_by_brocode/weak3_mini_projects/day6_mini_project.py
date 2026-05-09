"""
FOOTBALL PROJECT 3 — Shooting Efficiency
Evaluate goal conversion.
"""

import pandas as pd

df = pd.read_csv("03_py_external_labs_by_brocode/weak3_mini_projects/b_football_data_1300.csv")

df["conversion_rate"] = df["goals"] / df["shots"].replace(0,1)

eff = df.groupby("team")["conversion_rate"].mean().sort_values(ascending=False)

print("\nTEAM SHOOTING EFFICIENCY\n")
print(eff)

# Insights:
# • Most efficient attacking teams