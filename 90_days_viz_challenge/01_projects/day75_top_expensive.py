"""Project description: Top Expensive.
This script creates a visualization that explores top expensive in the dataset for the 90 Days of Visualization Challenge."""

import pandas as pd
import matplotlib.pyplot as plt

hospital_df = pd.read_csv('/home/kerim/Desktop/python_fundamentals/hospital_data.csv')

top_expensive = hospital_df.nlargest(10, 'treatment_cost')[['patient_id', 'diagnosis', 'treatment_cost']].reset_index(drop=True)
plt.figure(figsize=(14, 7))
plt.barh(range(len(top_expensive)), top_expensive['treatment_cost'].values, color='#e74c3c', edgecolor='black')
plt.yticks(range(len(top_expensive)), [f"Pt {id} - {diag}" for id, diag in zip(top_expensive['patient_id'], top_expensive['diagnosis'])], fontsize=9)
plt.xlabel('Cost ($)', fontsize=12, fontweight='bold')
plt.title('Day 75: Top 10 Most Expensive Treatments', fontsize=14, fontweight='bold')
plt.grid(axis='x', alpha=0.3)
plt.tight_layout()
plt.savefig('/home/kerim/Desktop/python_fundamentals/90_days_viz_challenge/evidences/day75_top_expensive.png', dpi=100, bbox_inches='tight')
plt.close()
print("✓ Day 75: Top 10 Expensive Treatments")
