"""Project description: Student Count By Grade.
This script creates a visualization that explores student count by grade in the dataset for the 90 Days of Visualization Challenge."""

import pandas as pd
import matplotlib.pyplot as plt

school_df = pd.read_csv('/home/kerim/Desktop/python_fundamentals/school_data.csv')

grade_student_count = school_df['grade'].value_counts()
plt.figure(figsize=(10, 7))
grade_student_count.plot(kind='bar', color='steelblue', edgecolor='black')
plt.xlabel('Grade', fontsize=12, fontweight='bold')
plt.ylabel('Student Count', fontsize=12, fontweight='bold')
plt.title('Day 17: Student Count by Grade', fontsize=14, fontweight='bold')
plt.xticks(rotation=0)
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('/home/kerim/Desktop/python_fundamentals/90_days_viz_challenge/evidences/day17_student_count_by_grade.png', dpi=100, bbox_inches='tight')
plt.close()
print("✓ Day 17: Student Count by Grade")
