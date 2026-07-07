"""
Football Project 18 — Top Player Contributions
"""

from pathlib import Path
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

BASE_DIR = Path(__file__).resolve().parent
PLOTS_DIR = BASE_DIR / "plots"
PLOTS_DIR.mkdir(exist_ok=True)

df = pd.read_csv(BASE_DIR / "b_football_data_1300.csv", parse_dates=["date"])
contrib = df.groupby("player")[["goals", "assists"]].sum()
contrib["contribution"] = contrib["goals"] + contrib["assists"]
top = contrib.sort_values("contribution", ascending=False).head(15)
plt.figure(figsize=(10, 7))
sns.barplot(x=top["contribution"], y=top.index, palette="magma")
plt.title("Top Player Contribution (Goals + Assists)")
plt.xlabel("Contribution")
plt.ylabel("Player")
plt.tight_layout()
plt.savefig(PLOTS_DIR / "project18_player_contribution_ratio.png", dpi=150)
plt.close()
print("Saved plots/project18_player_contribution_ratio.png")

#insights:
# 1, Identify the top players based on their combined contributions (goals + assists).
# 2, Analyze the distribution of contributions among players to understand their impact on the team's performance.
