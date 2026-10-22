"""Project description: Recovery Rate By Dept.
This script creates a visualization that explores recovery rate by dept in the dataset for the 90 Days of Visualization Challenge."""

import pandas as pd
import matplotlib.pyplot as plt

hospital_df = pd.read_csv('/home/kerim/Desktop/python_fundamentals/hospital_data.csv')

recovered_dept = hospital_df[hospital_df['recovery_status'] == 'Recovered'].groupby('department').size()
total_dept = hospital_df.groupby('department').size()
recovery_rate_dept = (recovered_dept / total_dept * 100).sort_values(ascending=False)
plt.figure(figsize=(12, 7))
recovery_rate_dept.plot(kind='bar', color='#2ecc71', edgecolor='black')
plt.ylabel('Recovery Rate (%)', fontsize=12, fontweight='bold')
plt.title('Day 74: Recovery Rate by Department', fontsize=14, fontweight='bold')
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('/home/kerim/Desktop/python_fundamentals/90_days_viz_challenge/evidences/day74_recovery_rate_by_dept.png', dpi=100, bbox_inches='tight')
plt.close()
print("✓ Day 74: Department-wise Recovery Rate")
