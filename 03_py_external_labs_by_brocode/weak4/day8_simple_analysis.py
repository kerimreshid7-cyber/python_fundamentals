"""
FOOTBALL PROJECT 4 — Playmaking Report
Analyze assists and passing.
"""

import pandas as pd

df = pd.read_csv("03_py_external_labs_by_brocode/weak3_mini_projects/b_football_data_1300.csv")

playmakers = df.groupby("player")[["assists","passes"]].sum().sort_values("assists", ascending=False).head(10)

print("\nTOP PLAYMAKERS\n")
print(playmakers)

# Insights:
# • Creative players and midfield strength
# • Tactical focus on playmaking