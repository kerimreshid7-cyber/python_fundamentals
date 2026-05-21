"""
Top assist players.
"""

import pandas as pd
df = pd.read_csv("03_py_external_labs_by_brocode/weak3_mini_projects/b_football_data_1300.csv")

print(df.groupby("player")["assists"].sum().sort_values(ascending=False).head(10))


# insights
# The top assist players in the dataset are identified based on the total number of assists they have contributed. The player with the highest number of assists is likely a key playmaker for their team,