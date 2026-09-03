"""Project description: School Dashboard.
This script creates a visualization that explores school dashboard in the dataset for the 90 Days of Visualization Challenge."""

import pandas as pd
import matplotlib.pyplot as plt

school_df = pd.read_csv('/home/kerim/Desktop/python_fundamentals/school_data.csv')

fig = plt.figure(figsize=(16, 10))
gs = fig.add_gridspec(3, 3, hspace=0.3, wspace=0.3)

# Subplot 1: Score Distribution
ax1 = fig.add_subplot(gs[0, 0])
ax1.hist(school_df['score'], bins=20, color='skyblue', edgecolor='black')
ax1.set_title('Score Distribution', fontweight='bold')
ax1.set_xlabel('Score')

# Subplot 2: Grade Distribution
ax2 = fig.add_subplot(gs[0, 1])
school_df['grade'].value_counts().plot(kind='bar', ax=ax2, color='coral')
ax2.set_title('Grade Distribution', fontweight='bold')
ax2.set_ylabel('Count')

# Subplot 3: Pass/Fail
ax3 = fig.add_subplot(gs[0, 2])
school_df['status'].value_counts().plot(kind='pie', ax=ax3, autopct='%1.1f%%', colors=['#2ecc71', '#e74c3c'])
ax3.set_title('Pass/Fail Ratio', fontweight='bold')

# Subplot 4: Subject Average
ax4 = fig.add_subplot(gs[1, 0])
school_df.groupby('subject')['score'].mean().plot(kind='barh', ax=ax4, color='mediumpurple')
ax4.set_title('Subject Avg Scores', fontweight='bold')

# Subplot 5: Attendance
ax5 = fig.add_subplot(gs[1, 1])
ax5.hist(school_df['attendance_percentage'], bins=15, color='lightgreen', edgecolor='black')
ax5.set_title('Attendance Distribution', fontweight='bold')
ax5.set_xlabel('Attendance %')

# Subplot 6: GPA
ax6 = fig.add_subplot(gs[1, 2])
ax6.hist(school_df['gpa'], bins=15, color='lightblue', edgecolor='black')
ax6.set_title('GPA Distribution', fontweight='bold')
ax6.set_xlabel('GPA')

# Subplot 7: Remarks
ax7 = fig.add_subplot(gs[2, 0])
school_df['remarks'].value_counts().plot(kind='bar', ax=ax7, color='teal')
ax7.set_title('Remarks Distribution', fontweight='bold')
ax7.set_ylabel('Count')

# Subplot 8: Status by Grade
ax8 = fig.add_subplot(gs[2, 1])
pd.crosstab(school_df['grade'], school_df['status']).plot(kind='bar', ax=ax8, color=['#e74c3c', '#2ecc71'])
ax8.set_title('Status by Grade', fontweight='bold')
ax8.set_ylabel('Count')

# Subplot 9: Top Teachers
ax9 = fig.add_subplot(gs[2, 2])
school_df.groupby('teacher')['score'].mean().nlargest(5).plot(kind='barh', ax=ax9, color='gold')
ax9.set_title('Top 5 Teachers', fontweight='bold')

fig.suptitle('Day 45: School Analytics Summary Dashboard', fontsize=16, fontweight='bold')
plt.savefig('/home/kerim/Desktop/python_fundamentals/90_days_viz_challenge/evidences/day45_school_dashboard.png', dpi=100, bbox_inches='tight')
plt.close()
print("✓ Day 45: School Analytics Summary Dashboard")

# Insights:
# 1. The dashboard provides a comprehensive overview of various aspects of school performance, including score distribution, grade distribution, pass/fail ratio, subject average scores, attendance, GPA, remarks, status by grade, and top teachers.
# 2. It allows educators and administrators to quickly identify areas of concern, track student performance, and make data-driven decisions to improve overall academic outcomes.