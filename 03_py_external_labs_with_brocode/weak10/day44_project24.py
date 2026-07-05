
# Today I will do mini anallytics project onto football data.

"""
Football Project 24 — Team Result Counts
"""

from pathlib import Path
import pandas as pd
import plotly.express as px

BASE_DIR = Path(__file__).resolve().parent
PLOTS_DIR = BASE_DIR / "plots"
PLOTS_DIR.mkdir(exist_ok=True)

df = pd.read_csv(BASE_DIR / "b_football_data_1300.csv", parse_dates=["date"])
result_team = df.groupby(["team", "result"]).size().reset_index(name="count")
fig = px.bar(result_team, x="team", y="count", color="result", title="Match Result Counts by Team")
fig.write_image(PLOTS_DIR / "project24_team_result_stacked.png")
print("Saved plots/project24_team_result_stacked.png")
