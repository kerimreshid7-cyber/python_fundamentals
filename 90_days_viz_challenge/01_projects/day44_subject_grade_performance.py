"""Project description: Subject Grade Performance.
This script creates a visualization that explores subject grade performance in the dataset for the 90 Days of Visualization Challenge."""

import pandas as pd
import matplotlib.pyplot as plt

school_df = pd.read_csv('/home/kerim/Desktop/python_fundamentals/school_data.csv')

subject_grade_pass = school_df[school_df['status'] == 'Pass'].groupby(['subject', 'grade']).size().unstack(fill_value=0)
plt.figure(figsize=(14, 7))
subject_grade_pass.plot(kind='bar', ax=plt.gca(), edgecolor='black')
plt.xlabel('Subject', fontsize=12, fontweight='bold')
plt.ylabel('Number of Passes', fontsize=12, fontweight='bold')
plt.title('Day 44: Pass Count by Subject and Grade', fontsize=14, fontweight='bold')
plt.xticks(rotation=45, ha='right')
plt.legend(title='Grade')
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('/home/kerim/Desktop/python_fundamentals/90_days_viz_challenge/evidences/day44_subject_grade_performance.png', dpi=100, bbox_inches='tight')
plt.close()
print("✓ Day 44: Subject-Grade Performance")
