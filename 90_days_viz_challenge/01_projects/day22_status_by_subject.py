"""Project description: Status By Subject.
This script creates a visualization that explores status by subject in the dataset for the 90 Days of Visualization Challenge."""

import pandas as pd
import matplotlib.pyplot as plt

school_df = pd.read_csv('/home/kerim/Desktop/python_fundamentals/school_data.csv')

status_subject = pd.crosstab(school_df['subject'], school_df['status'])
plt.figure(figsize=(14, 7))
status_subject.plot(kind='bar', ax=plt.gca(), color=['#e74c3c', '#2ecc71'], edgecolor='black')
plt.xlabel('Subject', fontsize=12, fontweight='bold')
plt.ylabel('Count', fontsize=12, fontweight='bold')
plt.title('Day 22: Pass/Fail Status by Subject', fontsize=14, fontweight='bold')
plt.xticks(rotation=45, ha='right')
plt.legend(title='Status')
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('/home/kerim/Desktop/python_fundamentals/90_days_viz_challenge/evidences/day22_status_by_subject.png', dpi=100, bbox_inches='tight')
plt.close()
print("✓ Day 22: Status by Subject")
