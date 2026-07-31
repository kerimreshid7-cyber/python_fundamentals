"""Project description: Teacher Effectiveness Box.
This script creates a visualization that explores teacher effectiveness box in the dataset for the 90 Days of Visualization Challenge."""

import pandas as pd
import matplotlib.pyplot as plt

school_df = pd.read_csv('/home/kerim/Desktop/python_fundamentals/school_data.csv')

plt.figure(figsize=(14, 8))
teacher_list = school_df['teacher'].unique()[:20]
data_to_plot = [school_df[school_df['teacher'] == teacher]['score'].values for teacher in teacher_list]
plt.boxplot(data_to_plot, labels=teacher_list)
plt.ylabel('Score', fontsize=12, fontweight='bold')
plt.title('Day 19: Teacher Effectiveness - Score Distribution (Top 20)', fontsize=14, fontweight='bold')
plt.xticks(rotation=45, ha='right', fontsize=9)
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('/home/kerim/Desktop/python_fundamentals/90_days_viz_challenge/evidences/day19_teacher_effectiveness_box.png', dpi=100, bbox_inches='tight')
plt.close()
print("✓ Day 19: Teacher Effectiveness Box Plot")
