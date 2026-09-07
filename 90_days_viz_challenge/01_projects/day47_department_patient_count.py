"""Project description: Department Patient Count.
This script creates a visualization that explores department patient count in the dataset for the 90 Days of Visualization Challenge."""

import pandas as pd
import matplotlib.pyplot as plt

hospital_df = pd.read_csv('/home/kerim/Desktop/python_fundamentals/hospital_data.csv')

dept_count = hospital_df['department'].value_counts().sort_values(ascending=False)
plt.figure(figsize=(12, 7))
dept_count.plot(kind='barh', color='steelblue', edgecolor='black')
plt.xlabel('Patient Count', fontsize=12, fontweight='bold')
plt.title('Day 47: Patient Count by Department', fontsize=14, fontweight='bold')
plt.grid(axis='x', alpha=0.3)
for i, v in enumerate(dept_count.values):
    plt.text(v + 5, i, str(v), va='center', fontweight='bold')
plt.tight_layout()
plt.savefig('/home/kerim/Desktop/python_fundamentals/90_days_viz_challenge/evidences/day47_department_patient_count.png', dpi=100, bbox_inches='tight')
plt.close()
print("✓ Day 47: Department-wise Patient Count")

# Insights:
# 1. The visualization reveals that certain departments have significantly higher patient counts compared to others, indicating a potential focus area for resource allocation and management.
# 2. The distribution of patient counts across departments can help hospital administrators identify trends and make informed decisions regarding staffing and departmental support.