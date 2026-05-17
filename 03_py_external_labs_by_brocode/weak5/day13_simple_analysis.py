"""
Average goals per match.
"""

import pandas as pd
df = pd.read_csv("03_py_external_labs_by_brocode/weak3_mini_projects/b_football_data_1300.csv")

print("Avg goals:", df["goals"].mean())