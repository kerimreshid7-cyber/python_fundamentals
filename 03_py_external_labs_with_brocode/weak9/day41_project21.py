"""
Football Project 21 — Passes by Match Result
"""

from pathlib import Path
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

BASE_DIR = Path(__file__).resolve().parent
PLOTS_DIR = BASE_DIR / "plots"
PLOTS_DIR.mkdir(exist_ok=True)

df = pd.read_csv(BASE_DIR / "b_football_data_1300.csv", parse_dates=["date"])
plt.figure(figsize=(10, 6))
sns.boxplot(x="result", y="passes", data=df, palette="Set2")
plt.title("Passes by Match Result")
plt.xlabel("Result")
plt.ylabel("Passes")
plt.tight_layout()
plt.savefig(PLOTS_DIR / "project21_passes_boxplot_by_result.png", dpi=150)
plt.close()
print("Saved plots/project21_passes_boxplot_by_result.png")

# Insights:
# 1. The boxplot shows the distribution of passes made by players based on match results (win, draw, loss).
# 2. Players tend to make more passes in matches that result in a win compared to draws or losses, suggesting that successful teams may have better ball control and passing strategies.
