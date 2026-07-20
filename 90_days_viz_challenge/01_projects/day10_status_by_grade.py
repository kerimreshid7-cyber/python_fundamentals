import pandas as pd
import matplotlib.pyplot as plt

school_df = pd.read_csv('/home/kerim/Desktop/python_fundamentals/school_data.csv')

status_grade = pd.crosstab(school_df['grade'], school_df['status'])
plt.figure(figsize=(12, 7))
status_grade.plot(kind='bar', ax=plt.gca(), color=['#e74c3c', '#2ecc71'], edgecolor='black')
plt.xlabel('Grade', fontsize=12, fontweight='bold')
plt.ylabel('Count', fontsize=12, fontweight='bold')
plt.title('Day 10: Pass/Fail Status by Grade', fontsize=14, fontweight='bold')
plt.xticks(rotation=0)
plt.legend(title='Status')
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('/home/kerim/Desktop/python_fundamentals/90_days_viz_challenge/evidences/day10_status_by_grade.png', dpi=100, bbox_inches='tight')
plt.close()
print("✓ Day 10: Status by Grade")
