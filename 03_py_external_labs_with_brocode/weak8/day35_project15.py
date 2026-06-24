"""
Football Project 15 — Shots vs Passes by Result
"""

from pathlib import Path
import pandas as pd
import plotly.express as px

BASE_DIR = Path(__file__).resolve().parent
PLOTS_DIR = BASE_DIR / "plots"
PLOTS_DIR.mkdir(exist_ok=True)

df = pd.read_csv(BASE_DIR / "b_football_data_1300.csv", parse_dates=["date"])
fig = px.scatter(df, x="shots", y="passes", color="result", size="minutes_played",
                 hover_data=["player", "team", "opponent"], title="Shots vs Passes by Match Result")
fig.write_image(PLOTS_DIR / "project15_shots_vs_passes.png")
print("Saved plots/project15_shots_vs_passes.png")

# insights:
# 1, Explore the relationship between shots and passes in football matches.
# 2, Analyze how the number of shots and passes varies with match results (win,loose and draw).

