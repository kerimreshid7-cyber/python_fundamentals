"""Project description: Attendance Vs Score.
This script creates a visualization that explores attendance vs score in the dataset for the 90 Days of Visualization Challenge."""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

school_df = pd.read_csv('/home/kerim/Desktop/python_fundamentals/school_data.csv')

plt.figure(figsize=(12, 7))
plt.scatter(school_df['attendance_percentage'], school_df['score'], alpha=0.5, c=school_df['gpa'], cmap='plasma', s=50)
z = np.polyfit(school_df['attendance_percentage'], school_df['score'], 1)
p = np.poly1d(z)
plt.plot(school_df['attendance_percentage'].sort_values(), p(school_df['attendance_percentage'].sort_values()), "r--", linewidth=2, label='Trend')
plt.xlabel('Attendance %', fontsize=12, fontweight='bold')
plt.ylabel('Score', fontsize=12, fontweight='bold')
plt.title('Day 24: Attendance vs Score Correlation', fontsize=14, fontweight='bold')
plt.legend()
plt.grid(alpha=0.3)
plt.colorbar(label='GPA')
plt.savefig('/home/kerim/Desktop/python_fundamentals/90_days_viz_challenge/evidences/day24_attendance_vs_score.png', dpi=100, bbox_inches='tight')
plt.close()
print("✓ Day 24: Attendance vs Score")

# Insights:
# 1. The scatter plot illustrates the relationship between attendance percentage and scores, with a trend line indicating a positive correlation.       
# 2. The color gradient representing GPA adds an additional layer of information, allowing for the observation of how GPA varies with attendance and scores, which can inform strategies to improve student performance.