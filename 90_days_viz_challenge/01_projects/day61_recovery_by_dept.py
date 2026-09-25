"""Project description: Recovery By Dept.
This script creates a visualization that explores recovery by dept in the dataset for the 90 Days of Visualization Challenge."""

import pandas as pd
import matplotlib.pyplot as plt

hospital_df = pd.read_csv('/home/kerim/Desktop/python_fundamentals/hospital_data.csv')

recovery_dept = pd.crosstab(hospital_df['department'], hospital_df['recovery_status'])
plt.figure(figsize=(14, 7))
recovery_dept.plot(kind='bar', ax=plt.gca(), color=['#2ecc71', '#f39c12', '#e74c3c'], edgecolor='black')
plt.xlabel('Department', fontsize=12, fontweight='bold')
plt.ylabel('Count', fontsize=12, fontweight='bold')
plt.title('Day 61: Recovery Status by Department', fontsize=14, fontweight='bold')
plt.xticks(rotation=45, ha='right')
plt.legend(title='Recovery Status')
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('/home/kerim/Desktop/python_fundamentals/90_days_viz_challenge/evidences/day61_recovery_by_dept.png', dpi=100, bbox_inches='tight')
plt.close()
print("✓ Day 61: Recovery Status by Department")
