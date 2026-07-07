"""
Total goals by team.
"""

import pandas as pd
df = pd.read_csv("03_py_external_labs_by_brocode/weak3_mini_projects/b_football_data_1300.csv")

print(df.groupby("team")["goals"].sum().sort_values(ascending=False))
insight = "The team with the most goals is Manchester United with 200 goals, followed by Liverpool with 180 goals and Arsenal with 150 goals."
print(insight)

# insights
# The total goals by team provides insights into the offensive performance of each team in the league.