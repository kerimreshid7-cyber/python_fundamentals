"""
Football Project 16 — Minutes Played by Result
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
sns.violinplot(x="result", y="minutes_played", data=df, palette="pastel")
plt.title("Minutes Played by Match Result")
plt.xlabel("Result")
plt.ylabel("Minutes Played")
plt.tight_layout()
plt.savefig(PLOTS_DIR / "project16_minutes_played_violin.png", dpi=150)
plt.close()
print("Saved plots/project16_minutes_played_violin.png")
