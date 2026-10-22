"""Project description: Cost By Visit Type.
This script creates a visualization that explores cost by visit type in the dataset for the 90 Days of Visualization Challenge."""

import pandas as pd
import matplotlib.pyplot as plt

hospital_df = pd.read_csv('/home/kerim/Desktop/python_fundamentals/hospital_data.csv')

plt.figure(figsize=(12, 7))
hospital_df.boxplot(column='treatment_cost', by='visit_type', figsize=(12, 7))
plt.xlabel('Visit Type', fontsize=12, fontweight='bold')
plt.ylabel('Treatment Cost ($)', fontsize=12, fontweight='bold')
plt.title('Day 73: Treatment Cost Distribution by Visit Type', fontsize=14, fontweight='bold')
plt.suptitle('')
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig('/home/kerim/Desktop/python_fundamentals/90_days_viz_challenge/evidences/day73_cost_by_visit_type.png', dpi=100, bbox_inches='tight')
plt.close()
print("✓ Day 73: Cost Distribution by Visit Type")

# Insights:
# 1. The boxplot illustrates the distribution of treatment costs across different visit types, providing a clear view of how costs vary by visit type.
# 2. Analyzing treatment costs in relation to visit type can help hospital administrators identify patterns and trends, allowing them to optimize resource allocation, improve patient care, and make informed decisions regarding treatment strategies and patient demographics.