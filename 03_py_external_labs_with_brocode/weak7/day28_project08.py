
# today i will do mini analytics projecct.

"""
Business Project 8 — Top Customers by Revenue
"""

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

BASE_DIR = Path(__file__).resolve().parent
PLOTS_DIR = BASE_DIR / "plots"
PLOTS_DIR.mkdir(exist_ok=True)

df = pd.read_csv(BASE_DIR / "a_business_data_2800.csv", parse_dates=["order_date"])
top_customers = df.groupby("customer_id")["revenue"].sum().nlargest(10)
plt.figure(figsize=(10, 6))
top_customers.plot(kind="barh", color="#9467bd")
plt.title("Top 10 Customers by Revenue")
plt.xlabel("Revenue")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig(PLOTS_DIR / "project08_top_customers_by_revenue.png", dpi=150)
plt.close()
print("Saved plots/project08_top_customers_by_revenue.png")


#insights:
# 1. The top 10 customers contribute significantly to the overall revenue, indicating a strong reliance on a small group of customers for business success.
# 2. The revenue distribution among the