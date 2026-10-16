"""Project description: Days Admitted By Diag.
This script creates a visualization that explores days admitted by diag in the dataset for the 90 Days of Visualization Challenge."""

import pandas as pd
import matplotlib.pyplot as plt

hospital_df = pd.read_csv('/home/kerim/Desktop/python_fundamentals/hospital_data.csv')

diag_days = hospital_df.groupby('diagnosis')['days_admitted'].mean().sort_values(ascending=False)
plt.figure(figsize=(12, 7))
diag_days.plot(kind='barh', color='coral', edgecolor='black')
plt.xlabel('Average Days Admitted', fontsize=12, fontweight='bold')
plt.title('Day 70: Average Days Admitted by Diagnosis', fontsize=14, fontweight='bold')
plt.grid(axis='x', alpha=0.3)
plt.tight_layout()
plt.savefig('/home/kerim/Desktop/python_fundamentals/90_days_viz_challenge/evidences/day70_days_admitted_by_diag.png', dpi=100, bbox_inches='tight')
plt.close()
print("✓ Day 70: Average Days Admitted by Diagnosis")

