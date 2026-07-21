"""Project description: Score Ranges.
This script creates a visualization that explores score ranges in the dataset for the 90 Days of Visualization Challenge."""

import pandas as pd
import matplotlib.pyplot as plt

school_df = pd.read_csv('/home/kerim/Desktop/python_fundamentals/school_data.csv')

bins = [0, 30, 40, 50, 60, 70, 80, 90, 100]
labels = ['0-30', '30-40', '40-50', '50-60', '60-70', '70-80', '80-90', '90-100']
score_ranges = pd.cut(school_df['score'], bins=bins, labels=labels)
plt.figure(figsize=(12, 7))
score_ranges.value_counts().sort_index().plot(kind='bar', color='teal', edgecolor='black')
plt.xlabel('Score Range', fontsize=12, fontweight='bold')
plt.ylabel('Count', fontsize=12, fontweight='bold')
plt.title('Day 9: Score Range Distribution', fontsize=14, fontweight='bold')
plt.xticks(rotation=0)
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('/home/kerim/Desktop/python_fundamentals/90_days_viz_challenge/evidences/day09_score_ranges.png', dpi=100, bbox_inches='tight')
plt.close()
print("✓ Day 9: Score Range Distribution")


# INSIGHTs:
# 1. The bar chart effectively illustrates the distribution of scores across different ranges, providing a clear overview of how students are performing in various score brackets.
# 2. The visualization highlights the concentration of scores in specific ranges, which can help identify areas where students may need additional support or resources.