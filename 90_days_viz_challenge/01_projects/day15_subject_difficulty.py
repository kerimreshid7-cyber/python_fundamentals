"""Project description: Subject Difficulty.
This script creates a visualization that explores subject difficulty in the dataset for the 90 Days of Visualization Challenge."""

import pandas as pd
import matplotlib.pyplot as plt

school_df = pd.read_csv('/home/kerim/Desktop/python_fundamentals/school_data.csv')

subject_difficulty = school_df.groupby('subject')['score'].mean().sort_values()
plt.figure(figsize=(12, 7))
subject_difficulty.plot(kind='barh', color='coral', edgecolor='black')
plt.xlabel('Average Score', fontsize=12, fontweight='bold')
plt.title('Day 15: Subject Difficulty by Average Score', fontsize=14, fontweight='bold')
plt.grid(axis='x', alpha=0.3)
plt.tight_layout()
plt.savefig('/home/kerim/Desktop/python_fundamentals/90_days_viz_challenge/evidences/day15_subject_difficulty.png', dpi=100, bbox_inches='tight')
plt.close()
print("✓ Day 15: Subject Difficulty")

# Insights:
# 1. The horizontal bar chart provides a clear visual representation of the average score for each subject, allowing for easy comparison of subject difficulty based on average scores.
# 2. This visualization can help identify subjects that may be more challenging for students, which can inform curriculum adjustments or additional support for students in those subjects.