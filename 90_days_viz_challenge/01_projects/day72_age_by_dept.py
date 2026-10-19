"""Project description: Age By Dept.
This script creates a visualization that explores age by dept in the dataset for the 90 Days of Visualization Challenge."""

import pandas as pd
import matplotlib.pyplot as plt

hospital_df = pd.read_csv('/home/kerim/Desktop/python_fundamentals/hospital_data.csv')

plt.figure(figsize=(14, 7))
hospital_df.boxplot(column='age', by='department', figsize=(14, 7))
plt.xlabel('Department', fontsize=12, fontweight='bold')
plt.ylabel('Age', fontsize=12, fontweight='bold')
plt.title('Day 72: Patient Age Distribution by Department', fontsize=14, fontweight='bold')
plt.suptitle('')
plt.xticks(rotation=45, ha='right')
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig('/home/kerim/Desktop/python_fundamentals/90_days_viz_challenge/evidences/day72_age_by_dept.png', dpi=100, bbox_inches='tight')
plt.close()
print("✓ Day 72: Patient Age by Department")
