"""Project description: Treatment Cost Distribution.
This script creates a visualization that explores treatment cost distribution in the dataset for the 90 Days of Visualization Challenge."""

import pandas as pd
import matplotlib.pyplot as plt

hospital_df = pd.read_csv('/home/kerim/Desktop/python_fundamentals/hospital_data.csv')

plt.figure(figsize=(12, 7))
plt.hist(hospital_df['treatment_cost'], bins=30, color='lightgreen', edgecolor='black', alpha=0.7)
plt.xlabel('Treatment Cost ($)', fontsize=12, fontweight='bold')
plt.ylabel('Frequency', fontsize=12, fontweight='bold')
plt.title('Day 52: Treatment Cost Distribution', fontsize=14, fontweight='bold')
plt.grid(axis='y', alpha=0.3)
plt.savefig('/home/kerim/Desktop/python_fundamentals/90_days_viz_challenge/evidences/day52_treatment_cost_distribution.png', dpi=100, bbox_inches='tight')
plt.close()
print("✓ Day 52: Treatment Cost Distribution")

# Insights:
# 1. The histogram provides a clear view of the distribution of treatment costs in the dataset, allowing healthcare professionals to identify the most common cost ranges.
# 2. Understanding treatment cost distribution can help in budgeting, resource allocation, and financial planning for healthcare facilities, ensuring that they can provide affordable care to patients while maintaining operational efficiency.

