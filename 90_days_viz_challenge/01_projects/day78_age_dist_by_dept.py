"""Project description: Age Dist By Dept.
This script creates a visualization that explores age dist by dept in the dataset for the 90 Days of Visualization Challenge."""

import pandas as pd
import matplotlib.pyplot as plt

hospital_df = pd.read_csv('/home/kerim/Desktop/python_fundamentals/hospital_data.csv')

fig, axes = plt.subplots(2, 5, figsize=(18, 10))
axes = axes.flatten()
departments = hospital_df['department'].unique()

for idx, dept in enumerate(sorted(departments)):
    dept_ages = hospital_df[hospital_df['department'] == dept]['age']
    axes[idx].hist(dept_ages, bins=15, color='skyblue', edgecolor='black', alpha=0.7)
    axes[idx].set_title(f'{dept}', fontweight='bold', fontsize=9)
    axes[idx].set_xlabel('Age', fontsize=8)
    axes[idx].set_ylabel('Count', fontsize=8)

plt.suptitle('Day 78: Age Distribution by Department', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('/home/kerim/Desktop/python_fundamentals/90_days_viz_challenge/evidences/day78_age_dist_by_dept.png', dpi=100, bbox_inches='tight')
plt.close()
print("✓ Day 78: Age Distribution by Department")
