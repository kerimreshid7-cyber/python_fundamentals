"""
Football Project 19 — Match Result Distribution
"""

from pathlib import Path
import pandas as pd
import plotly.express as px

BASE_DIR = Path(__file__).resolve().parent
PLOTS_DIR = BASE_DIR / "plots"
PLOTS_DIR.mkdir(exist_ok=True)

df = pd.read_csv(BASE_DIR / "b_football_data_1300.csv", parse_dates=["date"])
result_counts = df["result"].value_counts().reset_index()
result_counts.columns = ["result", "count"]
fig = px.pie(result_counts, names="result", values="count", hole=0.4, title="Match Result Distribution")
fig.write_image(PLOTS_DIR / "project19_result_distribution.png")
print("Saved plots/project19_result_distribution.png")

# Insights:
# 1. The pie chart provides a clear visual representation of the distribution of match results (win, loss, draw) in the dataset.
# 2. This analysis can help identify trends in team performance and inform strategies for future matches.