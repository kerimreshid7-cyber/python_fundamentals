


# Hello how are you today i am gonna cover histogram
# Histogram is visual presentation of distrbution of numerical values by groupig values into ranges(bins)


from pathlib import Path
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


plt.figure()
scores=np.random.normal(loc=60,scale=10,size=100)

plt.hist(scores)


# Real Company Scenario

# A company wants to analyze employee salaries.

plt.figure()
salaries = [
    25000, 28000, 30000, 32000, 35000,
    37000, 40000, 42000, 45000, 47000,
    50000, 52000, 55000, 58000, 60000,
    62000, 65000, 70000, 75000, 80000
]

plt.hist(salaries, bins=5, color="#1f77b4", edgecolor="black")

plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Number of Employees")

plt.show()   # but what if we do it by others like bar chart?   i mean what is the differnce usig this and  others in this data.


"""
Business Project 3 — Price Distribution
"""


BASE_DIR = Path(__file__).resolve().parent
PLOTS_DIR = BASE_DIR / "plots"
PLOTS_DIR.mkdir(exist_ok=True)

df = pd.read_csv(BASE_DIR / "a_business_data_2800.csv", parse_dates=["order_date"])
plt.figure(figsize=(10, 6))
sns.histplot(df["price"], kde=True, color="#2ca02c", bins=35)
plt.title("Product Price Distribution")
plt.xlabel("Price")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig(PLOTS_DIR / "project03_price_distribution.png", dpi=150)
plt.close()
print("Saved plots/project03_price_distribution.png")
