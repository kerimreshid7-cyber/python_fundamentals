"""Project description: Cost Percentiles.
This script creates a visualization that explores cost percentiles in the dataset for the 90 Days of Visualization Challenge."""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

hospital_df = pd.read_csv('/home/kerim/Desktop/python_fundamentals/hospital_data.csv')

percentiles = [10, 25, 50, 75, 90]
perc_values = [np.percentile(hospital_df['treatment_cost'], p) for p in percentiles]
plt.figure(figsize=(12, 7))
plt.bar([f'{p}th' for p in percentiles], perc_values, color='lightblue', edgecolor='black')
plt.ylabel('Cost ($)', fontsize=12, fontweight='bold')
plt.title('Day 62: Treatment Cost Percentiles', fontsize=14, fontweight='bold')
for i, v in enumerate(perc_values):
    plt.text(i, v + 200, f'${v:.0f}', ha='center', fontweight='bold')
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('/home/kerim/Desktop/python_fundamentals/90_days_viz_challenge/evidences/day62_cost_percentiles.png', dpi=100, bbox_inches='tight')
plt.close()
print("✓ Day 62: Treatment Cost Percentiles")


# Insights:
# 1. The bar chart illustrates the distribution of treatment costs across different percentiles, providing a clear view of how costs are distributed throughout the dataset.
# 2. Analyzing cost percentiles can help hospital management identify trends in treatment costs, allowing for better budgeting and resource allocation to ensure cost-effective patient care.