"""Project description: Dept Avg Cost.
This script creates a visualization that explores dept avg cost in the dataset for the 90 Days of Visualization Challenge."""

import pandas as pd
import matplotlib.pyplot as plt

hospital_df = pd.read_csv('/home/kerim/Desktop/python_fundamentals/hospital_data.csv')

dept_avg_cost = hospital_df.groupby('department')['treatment_cost'].mean().sort_values(ascending=False)
plt.figure(figsize=(12, 7))
dept_avg_cost.plot(kind='barh', color='coral', edgecolor='black')
plt.xlabel('Average Cost ($)', fontsize=12, fontweight='bold')
plt.title('Day 58: Average Treatment Cost by Department', fontsize=14, fontweight='bold')
plt.grid(axis='x', alpha=0.3)
plt.tight_layout()
plt.savefig('/home/kerim/Desktop/python_fundamentals/90_days_viz_challenge/evidences/day58_dept_avg_cost.png', dpi=100, bbox_inches='tight')
plt.close()
print("✓ Day 58: Department-wise Average Cost")

# Insights:
# 1. The bar chart illustrates the average treatment cost across different hospital departments, highlighting which departments incur higher costs on average. This information can be valuable for hospital management in identifying areas where cost optimization may be necessary.
# 2. Understanding department-wise cost distribution can aid in strategic planning, resource allocation, and improving operational efficiency, ensuring that departments with higher costs are scrutinized for potential cost-saving measures without compromising patient care quality.