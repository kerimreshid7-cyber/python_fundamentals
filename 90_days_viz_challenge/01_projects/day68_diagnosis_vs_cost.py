"""Project description: Diagnosis Vs Cost.
This script creates a visualization that explores diagnosis vs cost in the dataset for the 90 Days of Visualization Challenge."""

import pandas as pd
import matplotlib.pyplot as plt

hospital_df = pd.read_csv('/home/kerim/Desktop/python_fundamentals/hospital_data.csv')

diag_cost = hospital_df.groupby('diagnosis')['treatment_cost'].mean().sort_values(ascending=False)
plt.figure(figsize=(12, 7))
diag_cost.plot(kind='barh', color='salmon', edgecolor='black')
plt.xlabel('Average Cost ($)', fontsize=12, fontweight='bold')
plt.title('Day 68: Average Cost by Diagnosis', fontsize=14, fontweight='bold')
plt.grid(axis='x', alpha=0.3)
plt.tight_layout()
plt.savefig('/home/kerim/Desktop/python_fundamentals/90_days_viz_challenge/evidences/day68_diagnosis_vs_cost.png', dpi=100, bbox_inches='tight')
plt.close()
print("✓ Day 68: Diagnosis vs Cost Relationship")
