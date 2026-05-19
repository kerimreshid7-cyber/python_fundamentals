"""
Total goals by team.
"""

import pandas as pd
df = pd.read_csv("03_py_external_labs_by_brocode/weak3_mini_projects/b_football_data_1300.csv")

print(df.groupby("team")["goals"].sum().sort_values(ascending=False))