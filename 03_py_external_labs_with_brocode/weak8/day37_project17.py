"""
Football Project 17 — Goals per Match Trend by Team
"""

from pathlib import Path
import pandas as pd
import plotly.express as px

BASE_DIR = Path(__file__).resolve().parent
PLOTS_DIR = BASE_DIR / "plots"
PLOTS_DIR.mkdir(exist_ok=True)

df = pd.read_csv(BASE_DIR / "b_football_data_1300.csv", parse_dates=["date"])
team_goals = df.groupby(["date", "team"]).sum().reset_index()
fig = px.line(team_goals, x="date", y="goals", color="team", title="Goals per Match Trend by Team", line_shape="spline")
fig.update_layout(showlegend=False)
fig.write_image(PLOTS_DIR / "project17_goals_per_match_trend.png")
print("Saved plots/project17_goals_per_match_trend.png")

# insights:
# 1, Analyze the trend of goals scored by each team over time.
# 2, Identify teams with consistent goal-scoring performance and those with fluctuating trends.
