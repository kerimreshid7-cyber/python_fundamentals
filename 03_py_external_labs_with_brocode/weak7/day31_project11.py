"""
Business Project 11 — Daily Order Count
"""

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

BASE_DIR = Path(__file__).resolve().parent
PLOTS_DIR = BASE_DIR / "plots"
PLOTS_DIR.mkdir(exist_ok=True)

df = pd.read_csv(BASE_DIR / "a_business_data_2800.csv", parse_dates=["order_date"])
daily = df.groupby(df["order_date"].dt.date).size().reset_index(name="orders")
plt.figure(figsize=(12, 5))
sns.lineplot(data=daily, x="order_date", y="orders", marker="o")
plt.title("Daily Order Count")
plt.xlabel("Date")
plt.ylabel("Number of Orders")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(PLOTS_DIR / "project11_daily_order_count.png", dpi=150)
plt.close()
print("Saved plots/project11_daily_order_count.png")


# insights:
# 1, This line chart shows the daily order count over time, revealing trends and patterns in customer purchasing behavior, such as peaks during holidays or promotional events.
# 2. The chart can help identify seasonal trends, allowing the business to optimize inventory and