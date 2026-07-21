"""Project description: Subject Count.
This script creates a visualization that explores subject count in the dataset for the 90 Days of Visualization Challenge."""

import pandas as pd
import matplotlib.pyplot as plt

school_df = pd.read_csv('/home/kerim/Desktop/python_fundamentals/school_data.csv')

subject_counts = school_df['subject'].value_counts().sort_values(ascending=False)
plt.figure(figsize=(12, 7))
subject_counts.plot(kind='bar', color='steelblue', edgecolor='black')
plt.xlabel('Subject', fontsize=12, fontweight='bold')
plt.ylabel('Count', fontsize=12, fontweight='bold')
plt.title('Day 7: Subject Count Distribution', fontsize=14, fontweight='bold')
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('/home/kerim/Desktop/python_fundamentals/90_days_viz_challenge/evidences/day07_subject_count.png', dpi=100, bbox_inches='tight')
plt.close()
print("✓ Day 7: Subject Count Bar Chart")


# Insights:
# 1. The bar chart provides a clear visual representation of the number of students enrolled in each subject, allowing for easy comparison of the popularity of different subjects.
# 2. The chart shows the distribution of students across various subjects, making it easy to identify which subjects have the highest and
    