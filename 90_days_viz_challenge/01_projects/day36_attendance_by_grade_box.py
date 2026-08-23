"""Project description: Attendance By Grade Box.
This script creates a visualization that explores attendance by grade box in the dataset for the 90 Days of Visualization Challenge."""

import pandas as pd
import matplotlib.pyplot as plt

school_df = pd.read_csv('/home/kerim/Desktop/python_fundamentals/school_data.csv')

att_grade_dist = school_df.boxplot(column='attendance_percentage', by='grade', figsize=(12, 7), return_type='dict')
plt.xlabel('Grade', fontsize=12, fontweight='bold')
plt.ylabel('Attendance %', fontsize=12, fontweight='bold')
plt.title('Day 36: Attendance Distribution by Grade', fontsize=14, fontweight='bold')
plt.suptitle('')
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig('/home/kerim/Desktop/python_fundamentals/90_days_viz_challenge/evidences/day36_attendance_by_grade_box.png', dpi=100, bbox_inches='tight')
plt.close()
print("✓ Day 36: Grade-wise Attendance")

# Insights:
# 1. The boxplot shows the distribution of attendance percentages across different grades, allowing for easy comparison.
# 2. The median attendance percentage varies across grades, indicating differences in attendance behavior among students.
# 3. Outliers in attendance percentages can be observed in certain grades, which may warrant further investigation into the reasons behind these anomalies.