"""Project description: Student Count By Subject.
This script creates a visualization that explores student count by subject in the dataset for the 90 Days of Visualization Challenge."""

import pandas as pd
import matplotlib.pyplot as plt

school_df = pd.read_csv('/home/kerim/Desktop/python_fundamentals/school_data.csv')

subject_student = school_df['subject'].value_counts()
plt.figure(figsize=(12, 7))
subject_student.plot(kind='barh', color='mediumpurple', edgecolor='black')
plt.xlabel('Student Count', fontsize=12, fontweight='bold')
plt.title('Day 21: Student Count by Subject', fontsize=14, fontweight='bold')
plt.grid(axis='x', alpha=0.3)
plt.tight_layout()
plt.savefig('/home/kerim/Desktop/python_fundamentals/90_days_viz_challenge/evidences/day21_student_count_by_subject.png', dpi=100, bbox_inches='tight')
plt.close()
print("✓ Day 21: Subject-wise Student Count")
