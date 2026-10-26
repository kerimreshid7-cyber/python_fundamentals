"""Project description: Cheap Vs Expensive.
This script creates a visualization that explores cheap vs expensive in the dataset for the 90 Days of Visualization Challenge."""

import pandas as pd
import matplotlib.pyplot as plt

hospital_df = pd.read_csv('/home/kerim/Desktop/python_fundamentals/hospital_data.csv')

dept_cost = hospital_df.groupby('department')['treatment_cost'].mean().sort_values()
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))

cheapest = dept_cost.head(5)
cheapest.plot(kind='barh', ax=ax1, color='#2ecc71', edgecolor='black')
ax1.set_xlabel('Average Cost ($)', fontweight='bold')
ax1.set_title('5 Cheapest Departments', fontweight='bold')
ax1.grid(axis='x', alpha=0.3)

expensive = dept_cost.tail(5)
expensive.plot(kind='barh', ax=ax2, color='#e74c3c', edgecolor='black')
ax2.set_xlabel('Average Cost ($)', fontweight='bold')
ax2.set_title('5 Most Expensive Departments', fontweight='bold')
ax2.grid(axis='x', alpha=0.3)

plt.suptitle('Day 76: Cheapest vs Most Expensive Departments', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('/home/kerim/Desktop/python_fundamentals/90_days_viz_challenge/evidences/day76_cheap_vs_expensive.png', dpi=100, bbox_inches='tight')
plt.close()
print("✓ Day 76: Cheapest vs Most Expensive Departments")

# Insights:
# 1. The visualization clearly shows the average treatment costs for the five cheapest and five most expensive departments in the hospital dataset.
# 2. The cheapest departments have significantly lower average costs compared to the most expensive ones,
#     which may indicate differences in the types of treatments offered or the resources required for those treatments as well as the complexity of the procedures.