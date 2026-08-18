"""Project description: Score Above Below Avg.
This script creates a visualization that explores score above below avg in the dataset for the 90 Days of Visualization Challenge."""

import pandas as pd
import matplotlib.pyplot as plt

school_df = pd.read_csv('/home/kerim/Desktop/python_fundamentals/school_data.csv')

avg_score = school_df['score'].mean()
above_below = ['Above Average' if x >= avg_score else 'Below Average' for x in school_df['score']]
above_below_counts = pd.Series(above_below).value_counts()
plt.figure(figsize=(10, 7))
colors = ['#2ecc71', '#e74c3c']
plt.pie(above_below_counts, labels=above_below_counts.index, autopct='%1.1f%%', colors=colors, startangle=90)
plt.title(f'Day 32: Score Above/Below Average (Mean: {avg_score:.1f})', fontsize=14, fontweight='bold')
plt.savefig('/home/kerim/Desktop/python_fundamentals/90_days_viz_challenge/evidences/day32_score_above_below_avg.png', dpi=100, bbox_inches='tight')
plt.close()
print("✓ Day 32: Score Above/Below Average")

# Insights:
# 1. The pie chart provides a clear visual representation of the proportion of students who scored above and below the average score, allowing for quick assessment of overall performance.
# 2. The visualization can help identify trends in student performance, highlighting areas where interventions may be needed to support students who are performing below average, and recognizing those who are excelling.
