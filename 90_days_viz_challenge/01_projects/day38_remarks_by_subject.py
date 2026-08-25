"""Project description: Remarks By Subject.
This script creates a visualization that explores remarks by subject in the dataset for the 90 Days of Visualization Challenge."""

import pandas as pd
import matplotlib.pyplot as plt

school_df = pd.read_csv('/home/kerim/Desktop/python_fundamentals/school_data.csv')

remarks_subject = pd.crosstab(school_df['subject'], school_df['remarks'])
plt.figure(figsize=(14, 7))
remarks_subject.plot(kind='bar', ax=plt.gca(), edgecolor='black')
plt.xlabel('Subject', fontsize=12, fontweight='bold')
plt.ylabel('Count', fontsize=12, fontweight='bold')
plt.title('Day 38: Remarks Distribution by Subject', fontsize=14, fontweight='bold')
plt.xticks(rotation=45, ha='right')
plt.legend(title='Remarks')
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('/home/kerim/Desktop/python_fundamentals/90_days_viz_challenge/evidences/day38_remarks_by_subject.png', dpi=100, bbox_inches='tight')
plt.close()
print("✓ Day 38: Subject-wise Remarks Distribution")

# Insights:
# 1. The bar chart illustrates the distribution of remarks across different subjects, allowing for a quick comparison of how students are performing in each subject.
# 2. This visualization can help educators identify subjects where students may be struggling and require additional support or resources to improve their performance.