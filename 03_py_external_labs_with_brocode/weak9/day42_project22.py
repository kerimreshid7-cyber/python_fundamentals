"""
Football Project 22 — Team Goals Heatmap by Result
"""

from pathlib import Path
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

BASE_DIR = Path(__file__).resolve().parent
PLOTS_DIR = BASE_DIR / "plots"
PLOTS_DIR.mkdir(exist_ok=True)

df = pd.read_csv(BASE_DIR / "b_football_data_1300.csv", parse_dates=["date"])
pivot = df.pivot_table(index="team", columns="result", values="goals", aggfunc="sum", fill_value=0)
plt.figure(figsize=(12, 10))
sns.heatmap(pivot, annot=True, fmt="d", cmap="rocket")
plt.title("Goals by Team and Match Result")
plt.xlabel("Result")
plt.ylabel("Team")
plt.tight_layout()
plt.savefig(PLOTS_DIR / "project22_team_performance_heatmap.png", dpi=150)
plt.close()
print("Saved plots/project22_team_performance_heatmap.png")
