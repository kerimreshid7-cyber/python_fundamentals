# hello how are you doing today? I hope you are doing well. I am going to do mini project for day 4. 
# That is fooot ball data analysis. I am going to analyze the data and find out player with most goals.

"""
FOOTBALL PROJECT 2 — Top Scorers
Identify most productive players.
"""

import pandas as pd

df = pd.read_csv("03_py_external_labs_by_brocode/weak3_mini_projects/b_football_data_1300.csv")

players = df.groupby("player")["goals"].sum().sort_values(ascending=False).head(10)

print("\nTOP GOAL SCORERS\n")
print(players)

# Insights:
# • Top performers
# • Potential transfer targets