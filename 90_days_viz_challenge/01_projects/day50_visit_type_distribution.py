"""Project description: Visit Type Distribution.
This script creates a visualization that explores visit type distribution in the dataset for the 90 Days of Visualization Challenge."""

import pandas as pd
import matplotlib.pyplot as plt

hospital_df = pd.read_csv('/home/kerim/Desktop/python_fundamentals/hospital_data.csv')

visit_counts = hospital_df['visit_type'].value_counts()
plt.figure(figsize=(12, 7))
visit_counts.plot(kind='bar', color='mediumpurple', edgecolor='black')
plt.ylabel('Count', fontsize=12, fontweight='bold')
plt.title('Day 50: Visit Type Distribution', fontsize=14, fontweight='bold')
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', alpha=0.3)
for i, v in enumerate(visit_counts.values):
    plt.text(i, v + 10, str(v), ha='center', fontweight='bold')
plt.tight_layout()
plt.savefig('/home/kerim/Desktop/python_fundamentals/90_days_viz_challenge/evidences/day50_visit_type_distribution.png', dpi=100, bbox_inches='tight')
plt.close()
print("✓ Day 50: Visit Type Distribution")

# Insights:
# 1. The visualization shows the distribution of different visit types in the dataset, which can provide insights into the most common reasons for hospital visits.
# 2. Understanding visit type distribution can help healthcare providers allocate resources effectively, improve patient care strategies, and identify areas for potential improvement in service delivery.