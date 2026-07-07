
# Hello  how are you taday i am gonna start learning data visualization by python external libraries 
# I am gonna learn matplotlib seaborn and plotly.

# so lets start todays lesson which is matplotlib
# i will cover the basics of matplolib like ploting and grid.
from pathlib import Path

from tkinter import font

import numpy as np
import matplotlib.pyplot as plt

x = np.array([2023, 2024, 2025, 2026])

y1 = np.array([3, 23, 46, 5])
y2 = np.array([45, 43, 14, 10])
y3 = np.array([100, 43, 14, 200])

line_style = dict(
    marker=".",
    markersize=20,
    markerfacecolor="#1cd3fc",
    linewidth=3
)

plt.plot(x, y1, label="Person A", **line_style)
plt.plot(x, y2, label="Person B", **line_style)
plt.plot(x, y3, label="Person C", **line_style)

# Show values for y1
for i in range(len(x)):
    plt.text(x[i], y1[i], str(y1[i]))

# Show values for y2
for i in range(len(x)):
    plt.text(x[i], y2[i], str(y2[i]))

# Show values for y3
for i in range(len(x)):
    plt.text(x[i], y3[i], str(y3[i]))

plt.title("Performance Comparison")
plt.xlabel("Year")
plt.ylabel("Value")

plt.yticks(range(0, 201, 10))
plt.grid(True)
plt.legend()

plt.show()



"""
weak6 day20 — Data Visualization Example
Generates a combined line and bar chart PNG for weak6 day20.
"""


BASE_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = BASE_DIR.parent / "z_All_screenshots" / "weak6"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

months = ["Jan", "Feb", "Mar", "Apr"]
sales_monthly = [1200, 1500, 1800, 2200]
products = ["A", "B", "C"]
sales_products = [300, 500, 200]

fig, axes = plt.subplots(2, 1, figsize=(10, 10))
axes[0].plot(months, sales_monthly, marker="o", linewidth=2, color="#1f77b4")
axes[0].set_title("Monthly Sales")
axes[0].set_xlabel("Month")
axes[0].set_ylabel("Sales")

axes[1].bar(products, sales_products, color="#ff7f0e")
axes[1].set_title("Product Sales")
axes[1].set_xlabel("Product")
axes[1].set_ylabel("Sales")

fig.tight_layout()
output_path = OUTPUT_DIR / "day20_data_visualization.png"
fig.savefig(output_path, dpi=150)
plt.close(fig)
print(f"Saved {output_path}")
