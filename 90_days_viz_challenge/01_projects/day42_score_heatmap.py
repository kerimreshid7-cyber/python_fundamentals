"""Project description: Score Heatmap.
This script creates a visualization that explores score heatmap in the dataset for the 90 Days of Visualization Challenge."""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

school_df = pd.read_csv('/home/kerim/Desktop/python_fundamentals/school_data.csv')

grade_subject_score = school_df.pivot_table(values='score', index='grade', columns='subject', aggfunc='mean')
plt.figure(figsize=(12, 7))
sns.heatmap(grade_subject_score, annot=True, fmt='.1f', cmap='RdYlGn', cbar_kws={'label': 'Average Score'})
plt.title('Day 42: Average Score Heatmap (Grade vs Subject)', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('/home/kerim/Desktop/python_fundamentals/90_days_viz_challenge/evidences/day42_score_heatmap.png', dpi=100, bbox_inches='tight')
plt.close()
print("✓ Day 42: Score Distribution Heatmap")
