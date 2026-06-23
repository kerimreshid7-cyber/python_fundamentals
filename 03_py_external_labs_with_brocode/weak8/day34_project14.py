"""
Football Project 14 — Top Assist Players
"""

from pathlib import Path
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

BASE_DIR = Path(__file__).resolve().parent
PLOTS_DIR = BASE_DIR / "plots"
PLOTS_DIR.mkdir(exist_ok=True)

df = pd.read_csv(BASE_DIR / "b_football_data_1300.csv", parse_dates=["date"])
assists_player = df.groupby("player")["assists"].sum().nlargest(12)
plt.figure(figsize=(10, 6))
sns.barplot(x=assists_player.values, y=assists_player.index, palette="viridis")
plt.title("Top Assist Players")
plt.xlabel("Assists")
plt.ylabel("Player")
plt.tight_layout()
plt.savefig(PLOTS_DIR / "project14_top_assist_players.png", dpi=150)
plt.close()
print("Saved plots/project14_top_assist_players.png")

# Insights:
# 1, Identify the top assist players in the dataset.
# 2, Analyze the distribution of assists among players.
