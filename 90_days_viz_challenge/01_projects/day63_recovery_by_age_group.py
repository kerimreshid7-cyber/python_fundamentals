"""Project description: Recovery By Age Group.
This script creates a visualization that explores recovery by age group in the dataset for the 90 Days of Visualization Challenge."""

import pandas as pd
import matplotlib.pyplot as plt

hospital_df = pd.read_csv('/home/kerim/Desktop/python_fundamentals/hospital_data.csv')

age_bins = [0, 18, 35, 50, 65, 100]
age_labels = ['0-18', '18-35', '35-50', '50-65', '65+']
hospital_df['age_group'] = pd.cut(hospital_df['age'], bins=age_bins, labels=age_labels)
age_recovery = pd.crosstab(hospital_df['age_group'], hospital_df['recovery_status'])
plt.figure(figsize=(12, 7))
age_recovery.plot(kind='bar', ax=plt.gca(), color=['#2ecc71', '#f39c12', '#e74c3c'], edgecolor='black')
plt.xlabel('Age Group', fontsize=12, fontweight='bold')
plt.ylabel('Count', fontsize=12, fontweight='bold')
plt.title('Day 63: Recovery Status by Age Group', fontsize=14, fontweight='bold')
plt.xticks(rotation=0)
plt.legend(title='Recovery Status')
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('/home/kerim/Desktop/python_fundamentals/90_days_viz_challenge/evidences/day63_recovery_by_age_group.png', dpi=100, bbox_inches='tight')
plt.close()
print("✓ Day 63: Age Groups by Recovery Status")
