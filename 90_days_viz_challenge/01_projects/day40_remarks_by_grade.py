"""Project description: Remarks By Grade.
This script creates a visualization that explores remarks by grade in the dataset for the 90 Days of Visualization Challenge."""

import pandas as pd
import matplotlib.pyplot as plt

school_df = pd.read_csv('/home/kerim/Desktop/python_fundamentals/school_data.csv')

remarks_grade = pd.crosstab(school_df['grade'], school_df['remarks'])
plt.figure(figsize=(12, 7))
remarks_grade.plot(kind='bar', ax=plt.gca(), edgecolor='black')
plt.xlabel('Grade', fontsize=12, fontweight='bold')
plt.ylabel('Count', fontsize=12, fontweight='bold')
plt.title('Day 40: Remarks Distribution by Grade', fontsize=14, fontweight='bold')
plt.xticks(rotation=0)
plt.legend(title='Remarks', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('/home/kerim/Desktop/python_fundamentals/90_days_viz_challenge/evidences/day40_remarks_by_grade.png', dpi=100, bbox_inches='tight')
plt.close()
print("✓ Day 40: Remarks by Grade")
