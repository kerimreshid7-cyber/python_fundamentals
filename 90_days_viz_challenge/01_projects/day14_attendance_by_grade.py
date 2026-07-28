"""Project description: Attendance By Grade.
This script creates a visualization that explores attendance by grade in the dataset for the 90 Days of Visualization Challenge."""

import pandas as pd
import matplotlib.pyplot as plt

school_df = pd.read_csv('/home/kerim/Desktop/python_fundamentals/school_data.csv')

att_grade = school_df.groupby('grade')['attendance_percentage'].mean().sort_values(ascending=False)
plt.figure(figsize=(12, 7))
att_grade.plot(kind='bar', color='teal', edgecolor='black')
plt.xlabel('Grade', fontsize=12, fontweight='bold')
plt.ylabel('Average Attendance %', fontsize=12, fontweight='bold')
plt.title('Day 14: Average Attendance by Grade', fontsize=14, fontweight='bold')
plt.xticks(rotation=0)
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('/home/kerim/Desktop/python_fundamentals/90_days_viz_challenge/evidences/day14_attendance_by_grade.png', dpi=100, bbox_inches='tight')
plt.close()
print("✓ Day 14: Attendance by Grade")

# Insights:
# 1. The bar chart provides a clear visual representation of the average attendance percentage for each grade, allowing for easy comparison of attendance rates across different grades.
# 2. This visualization can help identify grades with lower attendance rates, which may indicate potential issues that need to be addressed to improve the overall attendance in the school.