"""
FOOTBALL PROJECT 2 — Team Performance
Analyze team results.
"""

import pandas as pd

df = pd.read_csv("03_py_external_labs_by_brocode/weak3_mini_projects/b_football_data_1300.csv")

results = df.groupby("team")["result"].value_counts().unstack().fillna(0)

print("\nTEAM PERFORMANCE TABLE\n")
print(results)