"""Project description: Diagnosis By Dept.
This script creates a visualization that explores diagnosis by dept in the dataset for the 90 Days of Visualization Challenge."""

import pandas as pd
import matplotlib.pyplot as plt

hospital_df = pd.read_csv('/home/kerim/Desktop/python_fundamentals/hospital_data.csv')

diag_dept = pd.crosstab(hospital_df['department'], hospital_df['diagnosis'])
plt.figure(figsize=(16, 8))
diag_dept.plot(kind='bar', ax=plt.gca(), edgecolor='black')
plt.xlabel('Department', fontsize=12, fontweight='bold')
plt.ylabel('Count', fontsize=12, fontweight='bold')
plt.title('Day 60: Top Diagnoses by Department', fontsize=14, fontweight='bold')
plt.xticks(rotation=45, ha='right')
plt.legend(title='Diagnosis', bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=8)
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('/home/kerim/Desktop/python_fundamentals/90_days_viz_challenge/evidences/day60_diagnosis_by_dept.png', dpi=100, bbox_inches='tight')
plt.close()
print("✓ Day 60: Diagnosis by Department")
