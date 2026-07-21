"""Project description: Attendance Distribution.
This script creates a visualization that explores attendance distribution in the dataset for the 90 Days of Visualization Challenge."""

import pandas as pd
import matplotlib.pyplot as plt

school_df = pd.read_csv('/home/kerim/Desktop/python_fundamentals/school_data.csv')

plt.figure(figsize=(12, 7))
plt.hist(school_df['attendance_percentage'], bins=20, color='lightgreen', edgecolor='black', alpha=0.7)
plt.xlabel('Attendance %', fontsize=12, fontweight='bold')
plt.ylabel('Number of Students', fontsize=12, fontweight='bold')
plt.title('Day 5: Attendance Percentage Distribution', fontsize=14, fontweight='bold')
plt.grid(axis='y', alpha=0.3)
plt.savefig('/home/kerim/Desktop/python_fundamentals/90_days_viz_challenge/evidences/day05_attendance_distribution.png', dpi=100, bbox_inches='tight')
plt.close()
print("✓ Day 5: Attendance Percentage Distribution")

#insights:
# 1. The histogram illustrates the distribution of attendance percentages among students, highlighting the most common attendance ranges.
# 2. The shape of the distribution can provide insights into student engagement and attendance patterns,
#    which may inform strategies for improving attendance rates.