"""
Football Project 23 — Opponent Shots Trend
"""

from pathlib import Path
import pandas as pd
import plotly.express as px

BASE_DIR = Path(__file__).resolve().parent
PLOTS_DIR = BASE_DIR / "plots"
PLOTS_DIR.mkdir(exist_ok=True)

df = pd.read_csv(BASE_DIR / "b_football_data_1300.csv", parse_dates=["date"])
opponent_shots = df.groupby(["date", "opponent"])["shots"].sum().reset_index()
fig = px.line(opponent_shots, x="date", y="shots", color="opponent", title="Opponent Shots Trend")
fig.write_image(PLOTS_DIR / "project23_opponent_shots_trend.png")
print("Saved plots/project23_opponent_shots_trend.png")
