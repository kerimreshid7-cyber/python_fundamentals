"""Project description: Dept Efficiency.
This script creates a visualization that explores dept efficiency in the dataset for the 90 Days of Visualization Challenge."""

import pandas as pd
import matplotlib.pyplot as plt

hospital_df = pd.read_csv('/home/kerim/Desktop/python_fundamentals/hospital_data.csv')

dept_visits = hospital_df.groupby('department').size()
dept_total_cost = hospital_df.groupby('department')['treatment_cost'].sum()
dept_efficiency = dept_total_cost / dept_visits
plt.figure(figsize=(12, 7))
dept_efficiency.plot(kind='barh', color='gold', edgecolor='black')
plt.xlabel('Average Cost per Visit ($)', fontsize=12, fontweight='bold')
plt.title('Day 66: Department Efficiency (Cost per Visit)', fontsize=14, fontweight='bold')
plt.grid(axis='x', alpha=0.3)
plt.tight_layout()
plt.savefig('/home/kerim/Desktop/python_fundamentals/90_days_viz_challenge/evidences/day66_dept_efficiency.png', dpi=100, bbox_inches='tight')
plt.close()
print("✓ Day 66: Department Efficiency")
