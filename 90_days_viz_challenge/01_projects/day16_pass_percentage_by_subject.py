"""Project description: Pass Percentage By Subject.
This script creates a visualization that explores pass percentage by subject in the dataset for the 90 Days of Visualization Challenge."""

import pandas as pd
import matplotlib.pyplot as plt

school_df = pd.read_csv('/home/kerim/Desktop/python_fundamentals/school_data.csv')

pass_by_subject = school_df[school_df['status'] == 'Pass'].groupby('subject').size() / school_df.groupby('subject').size() * 100
pass_by_subject = pass_by_subject.sort_values(ascending=False)
plt.figure(figsize=(12, 7))
pass_by_subject.plot(kind='bar', color='lightgreen', edgecolor='black')
plt.xlabel('Subject', fontsize=12, fontweight='bold')
plt.ylabel('Pass Percentage %', fontsize=12, fontweight='bold')
plt.title('Day 16: Pass Percentage by Subject', fontsize=14, fontweight='bold')
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('/home/kerim/Desktop/python_fundamentals/90_days_viz_challenge/evidences/day16_pass_percentage_by_subject.png', dpi=100, bbox_inches='tight')
plt.close()
print("✓ Day 16: Pass Percentage by Subject")
