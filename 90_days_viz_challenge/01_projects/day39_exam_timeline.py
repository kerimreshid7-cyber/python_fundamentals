"""Project description: Exam Timeline.
This script creates a visualization that explores exam timeline in the dataset for the 90 Days of Visualization Challenge."""

import pandas as pd
import matplotlib.pyplot as plt

school_df = pd.read_csv('/home/kerim/Desktop/python_fundamentals/school_data.csv')

school_df['exam_date_converted'] = pd.to_datetime(school_df['exam_date'])
exam_timeline = school_df.groupby(school_df['exam_date_converted'].dt.date).size()
plt.figure(figsize=(14, 7))
plt.plot(exam_timeline.index, exam_timeline.values, linewidth=2, marker='o', markersize=4, color='steelblue')
plt.xlabel('Date', fontsize=12, fontweight='bold')
plt.ylabel('Number of Exams', fontsize=12, fontweight='bold')
plt.title('Day 39: Exam Timeline Distribution', fontsize=14, fontweight='bold')
plt.xticks(rotation=45)
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig('/home/kerim/Desktop/python_fundamentals/90_days_viz_challenge/evidences/day39_exam_timeline.png', dpi=100, bbox_inches='tight')
plt.close()
print("✓ Day 39: Exam Date Timeline")
