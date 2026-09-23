"""Project description: Gender By Dept.
This script creates a visualization that explores gender by dept in the dataset for the 90 Days of Visualization Challenge."""

import pandas as pd
import matplotlib.pyplot as plt

hospital_df = pd.read_csv('/home/kerim/Desktop/python_fundamentals/hospital_data.csv')

gender_dept = pd.crosstab(hospital_df['department'], hospital_df['gender'])
plt.figure(figsize=(12, 7))
gender_dept.plot(kind='bar', ax=plt.gca(), color=['#ff6b6b', '#4ecdc4'], edgecolor='black')
plt.xlabel('Department', fontsize=12, fontweight='bold')
plt.ylabel('Count', fontsize=12, fontweight='bold')
plt.title('Day 59: Gender Distribution by Department', fontsize=14, fontweight='bold')
plt.xticks(rotation=45, ha='right')
plt.legend(title='Gender')
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('/home/kerim/Desktop/python_fundamentals/90_days_viz_challenge/evidences/day59_gender_by_dept.png', dpi=100, bbox_inches='tight')
plt.close()
print("✓ Day 59: Gender by Department")
