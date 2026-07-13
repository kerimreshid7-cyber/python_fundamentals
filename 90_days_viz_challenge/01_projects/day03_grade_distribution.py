import pandas as pd
import matplotlib.pyplot as plt

school_df = pd.read_csv('/home/kerim/Desktop/python_fundamentals/school_data.csv')

grade_counts = school_df['grade'].value_counts()
plt.figure(figsize=(10, 8))
colors = plt.cm.Set3(range(len(grade_counts)))
plt.pie(grade_counts, labels=grade_counts.index, autopct='%1.1f%%', colors=colors, startangle=90)
plt.title('Day 3: Grade Distribution', fontsize=14, fontweight='bold')
plt.savefig('/home/kerim/Desktop/python_fundamentals/90_days_viz_challenge/evidences/day03_grade_distribution.png', dpi=100, bbox_inches='tight')
plt.close()
print("✓ Day 3: Grade Distribution Pie Chart")

# Insights:
# 1. The pie chart illustrates the distribution of students across different grades, providing a clear visual representation of the student population.
# 2. The largest segment represents the grade with the highest number of students, indicating where the majority of the student body is concentrated.
# 3. Smaller segments highlight grades with fewer students, which may require additional attention or resources to ensure balanced educational support across all grades.