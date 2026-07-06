

# Today I will do mini analytics prooject on to the football data.

"""
Football Project 25 — Football Stats Correlation
"""

from pathlib import Path
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

BASE_DIR = Path(__file__).resolve().parent
PLOTS_DIR = BASE_DIR / "plots"
PLOTS_DIR.mkdir(exist_ok=True)

df = pd.read_csv(BASE_DIR / "b_football_data_1300.csv", parse_dates=["date"])
numeric = df[["goals", "assists", "shots", "passes", "minutes_played"]]
corr = numeric.corr()
plt.figure(figsize=(8, 6))
sns.heatmap(corr, annot=True, cmap="coolwarm", vmin=-1, vmax=1)
plt.title("Correlation Matrix for Football Stats")
plt.tight_layout()
plt.savefig(PLOTS_DIR / "project25_numeric_correlation_heatmap.png", dpi=150)
plt.close()
print("Saved plots/project25_numeric_correlation_heatmap.png")
