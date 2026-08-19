"""Project description: Best Teachers.
This script creates a visualization that explores best teachers in the dataset for the 90 Days of Visualization Challenge."""

import pandas as pd
import matplotlib.pyplot as plt

school_df = pd.read_csv('/home/kerim/Desktop/python_fundamentals/school_data.csv')

teacher_avg = school_df.groupby('teacher')['score'].mean().sort_values(ascending=False).head(15)
plt.figure(figsize=(12, 7))
teacher_avg.plot(kind='bar', color='gold', edgecolor='black')
plt.xlabel('Teacher', fontsize=12, fontweight='bold')
plt.ylabel('Average Score', fontsize=12, fontweight='bold')
plt.title('Day 33: Best 15 Performing Teachers by Average Score', fontsize=14, fontweight='bold')
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('/home/kerim/Desktop/python_fundamentals/90_days_viz_challenge/evidences/day33_best_teachers.png', dpi=100, bbox_inches='tight')
plt.close()
print("✓ Day 33: Best Performing Teachers")

# Insights:
# 1. The bar chart highlights the top 15 teachers based on their average student scores, providing a clear visual representation of their performance.
# 2. This visualization can help identify effective teaching practices and recognize teachers who are contributing significantly to student success, potentially serving as A role models for their peers.