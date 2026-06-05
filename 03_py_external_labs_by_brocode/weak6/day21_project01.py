

# hello how are today  i am gonna cover bar chart.
# bar chart is used to compare two or more categories by thier actual value
import matplotlib.pyplot as plt
players = ["Salah", "Haaland", "Mbappe", "Kane", "Lewandowski"]
goals = [29, 34, 28, 26, 24]

plt.bar(players,goals)
plt.title("top goal scorer")
plt.xlabel("players")
plt.ylabel("goal")

plt.show()



# """

# Business Project 1 — Revenue by Category
# """
# from pathlib import Path
# import pandas as pd
# import matplotlib.pyplot as plt

# BASE_DIR = Path(__file__).resolve().parent
# PLOTS_DIR = BASE_DIR / "plots"
# PLOTS_DIR.mkdir(exist_ok=True)

# df = pd.read_csv(BASE_DIR / "a_business_data_2800.csv", parse_dates=["order_date"])
# revenue_by_cat = df.groupby("product_category")["revenue"].sum().sort_values(ascending=False)
# plt.figure(figsize=(10, 6))
# revenue_by_cat.plot(kind="bar", color="#4c72b0")
# plt.title("Revenue by Product Category")
# plt.xlabel("Product Category")
# plt.ylabel("Total Revenue")
# plt.tight_layout()
# plt.savefig(PLOTS_DIR / "project01_revenue_by_category.png", dpi=150)
# plt.close()
# print("Saved plots/project01_revenue_by_category.png")
