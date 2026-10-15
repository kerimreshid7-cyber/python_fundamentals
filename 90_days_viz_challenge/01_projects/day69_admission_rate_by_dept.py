"""Project description: Admission Rate By Dept.
This script creates a visualization that explores admission rate by dept in the dataset for the 90 Days of Visualization Challenge."""

import pandas as pd
import matplotlib.pyplot as plt

hospital_df = pd.read_csv('/home/kerim/Desktop/python_fundamentals/hospital_data.csv')

admitted_dept = hospital_df[hospital_df['admitted'] == 'Yes'].groupby('department').size()
total_dept = hospital_df.groupby('department').size()
admission_rate = (admitted_dept / total_dept * 100).sort_values(ascending=False)
plt.figure(figsize=(12, 7))
admission_rate.plot(kind='bar', color='steelblue', edgecolor='black')
plt.ylabel('Admission Rate (%)', fontsize=12, fontweight='bold')
plt.title('Day 69: Admission Rate by Department', fontsize=14, fontweight='bold')
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('/home/kerim/Desktop/python_fundamentals/90_days_viz_challenge/evidences/day69_admission_rate_by_dept.png', dpi=100, bbox_inches='tight')
plt.close()
print("✓ Day 69: Admission Rate by Department")
