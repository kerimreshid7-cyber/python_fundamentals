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
