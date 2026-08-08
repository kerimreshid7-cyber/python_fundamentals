"""Project description: Top Performers By Grade.
This script creates a visualization that explores top performers by grade in the dataset for the 90 Days of Visualization Challenge."""

import pandas as pd
import matplotlib.pyplot as plt

school_df = pd.read_csv('/home/kerim/Desktop/python_fundamentals/school_data.csv')

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
grades = school_df['grade'].unique()
for idx, grade in enumerate(sorted(grades)):
    ax = axes[idx // 2, idx % 2]
    top_in_grade = school_df[school_df['grade'] == grade].nlargest(10, 'score')[['name', 'score']]
    ax.barh(range(len(top_in_grade)), top_in_grade['score'].values, color='gold', edgecolor='black')
    ax.set_yticks(range(len(top_in_grade)))
    ax.set_yticklabels(top_in_grade['name'].values, fontsize=8)
    ax.set_xlabel('Score', fontweight='bold')
    ax.set_title(f'Top 10 Students in Grade {grade}', fontweight='bold')
    ax.grid(axis='x', alpha=0.3)
plt.tight_layout()
plt.savefig('/home/kerim/Desktop/python_fundamentals/90_days_viz_challenge/evidences/day25_top_performers_by_grade.png', dpi=100, bbox_inches='tight')
plt.close()
print("✓ Day 25: Top Performers by Grade")

# Insights:
# 1. The bar charts provide a clear visual representation of the top 10 performers in each grade, allowing for easy comparison of student performance within and across grades.
# 2. This visualization can help identify high-achieving students and inform strategies for recognizing and supporting their academic success.