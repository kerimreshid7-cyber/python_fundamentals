"""
Average goals per match.
"""

import pandas as pd
df = pd.read_csv("03_py_external_labs_by_brocode/weak3_mini_projects/b_football_data_1300.csv")

print("Avg goals:", df["goals"].mean())

# insights  
# The average goals per match is a key performance indicator that provides insights into the offensive capabilities of the teams in the league. A higher average suggests a more attacking style of play, which can be more entertaining for fans and may indicate a competitive league. Conversely, a lower average may suggest a more defensive approach, which could impact the overall excitement of the matches. Understanding this metric can help teams and analysts identify trends and make strategic decisions to improve performance.