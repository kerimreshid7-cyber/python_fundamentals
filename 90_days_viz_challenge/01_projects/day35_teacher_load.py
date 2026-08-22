"""Project description: Teacher Load.
This script creates a visualization that explores teacher load in the dataset for the 90 Days of Visualization Challenge."""

import pandas as pd
import matplotlib.pyplot as plt

school_df = pd.read_csv('/home/kerim/Desktop/python_fundamentals/school_data.csv')

teacher_load = school_df['teacher'].value_counts()
plt.figure(figsize=(12, 7))
plt.hist(teacher_load.values, bins=20, color='mediumpurple', edgecolor='black', alpha=0.7)
plt.xlabel('Number of Students per Teacher', fontsize=12, fontweight='bold')
plt.ylabel('Frequency', fontsize=12, fontweight='bold')
plt.title('Day 35: Teacher Load Distribution', fontsize=14, fontweight='bold')
plt.axvline(teacher_load.mean(), color='red', linestyle='--', linewidth=2, label=f'Mean: {teacher_load.mean():.1f}')
plt.legend()
plt.grid(axis='y', alpha=0.3)
plt.savefig('/home/kerim/Desktop/python_fundamentals/90_days_viz_challenge/evidences/day35_teacher_load.png', dpi=100, bbox_inches='tight')
plt.close()
print("✓ Day 35: Teacher Load Distribution")

# Insights:
# 1. The histogram provides a clear view of the distribution of students per teacher, highlighting  the range and frequency of teacher loads across the dataset.
# 2. The mean line indicates the average number of students per teacher, which can help identify teachers who may be overburdened or underutilized, guiding decisions for resource allocation and workload balancing in educational institutions.