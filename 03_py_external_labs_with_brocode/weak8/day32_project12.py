"""
Business Project 12 — Revenue Heatmap by Country and Channel
"""

from pathlib import Path
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

BASE_DIR = Path(__file__).resolve().parent
PLOTS_DIR = BASE_DIR / "plots"
PLOTS_DIR.mkdir(exist_ok=True)

df = pd.read_csv(BASE_DIR / "a_business_data_2800.csv", parse_dates=["order_date"])
pivot = df.pivot_table(index="country", columns="marketing_channel", values="revenue", aggfunc="sum", fill_value=0)
plt.figure(figsize=(12, 8))
sns.heatmap(pivot, cmap="Blues", linewidths=0.5)
plt.title("Revenue by Country and Marketing Channel")
plt.xlabel("Marketing Channel")
plt.ylabel("Country")
plt.tight_layout()
plt.savefig(PLOTS_DIR / "project12_country_revenue_heatmap.png", dpi=150)
plt.close()
print("Saved plots/project12_country_revenue_heatmap.png")


# insights:
# 1. The heatmap provides a clear visual representation of revenue distribution across different countries and marketing channels, allowing the business to identify which combinations are most profitable.
# 2. By analyzing the heatmap, the business can make informed decisions on where to allocate marketing resources and which channels to