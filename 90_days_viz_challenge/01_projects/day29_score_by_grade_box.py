"""Project description: Score By Grade Box.
This script creates a visualization that explores score by grade box in the dataset for the 90 Days of Visualization Challenge."""

import pandas as pd
import matplotlib.pyplot as plt

school_df = pd.read_csv('/home/kerim/Desktop/python_fundamentals/school_data.csv')

plt.figure(figsize=(12, 7))
school_df.boxplot(column='score', by='grade', figsize=(12, 7))
plt.xlabel('Grade', fontsize=12, fontweight='bold')
plt.ylabel('Score', fontsize=12, fontweight='bold')
plt.title('Day 29: Score Distribution by Grade (Box Plot)', fontsize=14, fontweight='bold')
plt.suptitle('')
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig('/home/kerim/Desktop/python_fundamentals/90_days_viz_challenge/evidences/day29_score_by_grade_box.png', dpi=100, bbox_inches='tight')
plt.close()
print("✓ Day 29: Grade Distribution Box Plot")

# Insights:
# 1. The box plot reveals the distribution of scores across different grades, highlighting the median, quartiles, and potential outliers.
# 2. Grades with a wider interquartile range may indicate greater variability in student performance, while grades with a narrower range may suggest more consistent performance among students.