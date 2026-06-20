"""
Football Project 13 — Total Goals by Team
"""

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

BASE_DIR = Path(__file__).resolve().parent
PLOTS_DIR = BASE_DIR / "plots"
PLOTS_DIR.mkdir(exist_ok=True)

df = pd.read_csv(BASE_DIR / "b_football_data_1300.csv", parse_dates=["date"])
goals_team = df.groupby("team")["goals"].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(10, 6))
goals_team.plot(kind="bar", color="#d62728")
plt.title("Top 10 Teams by Total Goals")
plt.xlabel("Team")
plt.ylabel("Goals")
plt.tight_layout()
plt.savefig(PLOTS_DIR / "project13_goals_by_team.png", dpi=150)
plt.close()
print("Saved plots/project13_goals_by_team.png")
