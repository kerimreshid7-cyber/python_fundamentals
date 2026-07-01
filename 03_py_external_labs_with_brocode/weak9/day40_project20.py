"""
Football Project 20 — Top Performer Contributions
"""

from pathlib import Path
import pandas as pd
import plotly.express as px

BASE_DIR = Path(__file__).resolve().parent
PLOTS_DIR = BASE_DIR / "plots"
PLOTS_DIR.mkdir(exist_ok=True)

df = pd.read_csv(BASE_DIR / "b_football_data_1300.csv", parse_dates=["date"])
summary = df.groupby("player")[["goals", "assists", "minutes_played"]].sum()
summary = summary[summary["minutes_played"] > 50]
summary["total_contribution"] = summary["goals"] + summary["assists"]
fig = px.scatter(summary.reset_index(), x="minutes_played", y="total_contribution", color="goals",
                 size="goals", hover_data=["player", "assists"], title="Top Performers: Contribution vs Minutes")
fig.write_image(PLOTS_DIR / "project20_top_performers_scatter.png")
print("Saved plots/project20_top_performers_scatter.png")
