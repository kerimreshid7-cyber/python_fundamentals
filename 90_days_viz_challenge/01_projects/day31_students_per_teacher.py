"""Project description: Students Per Teacher.
This script creates a visualization that explores students per teacher in the dataset for the 90 Days of Visualization Challenge."""

import pandas as pd
import matplotlib.pyplot as plt

school_df = pd.read_csv('/home/kerim/Desktop/python_fundamentals/school_data.csv')

students_per_teacher = school_df['teacher'].value_counts().sort_values(ascending=False).head(20)
plt.figure(figsize=(12, 7))
students_per_teacher.plot(kind='barh', color='steelblue', edgecolor='black')
plt.xlabel('Student Count', fontsize=12, fontweight='bold')
plt.title('Day 31: Top 20 Teachers by Student Count', fontsize=14, fontweight='bold')
plt.grid(axis='x', alpha=0.3)
plt.tight_layout()
plt.savefig('/home/kerim/Desktop/python_fundamentals/90_days_viz_challenge/evidences/day31_students_per_teacher.png', dpi=100, bbox_inches='tight')
plt.close()
print("✓ Day 31: Students per Teacher")
