"""Project description: Pass Rate Stacked.
This script creates a visualization that explores pass rate stacked in the dataset for the 90 Days of Visualization Challenge."""

import pandas as pd
import matplotlib.pyplot as plt

school_df = pd.read_csv('/home/kerim/Desktop/python_fundamentals/school_data.csv')

pass_fail_subject = pd.crosstab(school_df['subject'], school_df['status'], normalize='index') * 100
plt.figure(figsize=(12, 7))
pass_fail_subject.plot(kind='bar', stacked=True, color=['#e74c3c', '#2ecc71'], edgecolor='black')
plt.xlabel('Subject', fontsize=12, fontweight='bold')
plt.ylabel('Percentage', fontsize=12, fontweight='bold')
plt.title('Day 28: Pass Rate % by Subject', fontsize=14, fontweight='bold')
plt.xticks(rotation=45, ha='right')
plt.legend(title='Status')
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('/home/kerim/Desktop/python_fundamentals/90_days_viz_challenge/evidences/day28_pass_rate_stacked.png', dpi=100, bbox_inches='tight')
plt.close()
print("✓ Day 28: Subject-wise Pass Rate")
