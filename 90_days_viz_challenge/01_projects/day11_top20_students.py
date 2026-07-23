"""Project description: Top20 Students.
This script creates a visualization that explores top20 students in the dataset for the 90 Days of Visualization Challenge."""

import pandas as pd
import matplotlib.pyplot as plt

school_df = pd.read_csv('/home/kerim/Desktop/python_fundamentals/school_data.csv')

top_students = school_df.nlargest(20, 'score')[['name', 'score']].reset_index(drop=True)
plt.figure(figsize=(14, 8))
plt.barh(range(len(top_students)), top_students['score'].values, color='gold', edgecolor='black')
plt.yticks(range(len(top_students)), top_students['name'].values, fontsize=9)
plt.xlabel('Score', fontsize=12, fontweight='bold')
plt.title('Day 11: Top 20 Students by Score', fontsize=14, fontweight='bold')
plt.grid(axis='x', alpha=0.3)
plt.tight_layout()
plt.savefig('/home/kerim/Desktop/python_fundamentals/90_days_viz_challenge/evidences/day11_top20_students.png', dpi=100, bbox_inches='tight')
plt.close()
print("✓ Day 11: Top 20 Students by Score")

# INSIGHTs:
# 1. The horizontal bar chart effectively highlights the top 20 students based on their scores, allowing for easy comparison of their performance.
# 2. This visualization can be used to recognize and celebrate the achievements of high-performing students, as well as to identify potential role models for their peers