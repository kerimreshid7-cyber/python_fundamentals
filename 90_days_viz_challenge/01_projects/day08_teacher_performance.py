import pandas as pd
import matplotlib.pyplot as plt

school_df = pd.read_csv('/home/kerim/Desktop/python_fundamentals/school_data.csv')

teacher_perf = school_df.groupby('teacher')['score'].mean().sort_values(ascending=False).head(15)
plt.figure(figsize=(12, 7))
teacher_perf.plot(kind='barh', color='mediumpurple', edgecolor='black')
plt.xlabel('Average Score', fontsize=12, fontweight='bold')
plt.title('Day 8: Top 15 Teachers by Average Score', fontsize=14, fontweight='bold')
plt.grid(axis='x', alpha=0.3)
plt.tight_layout()
plt.savefig('/home/kerim/Desktop/python_fundamentals/90_days_viz_challenge/evidences/day08_teacher_performance.png', dpi=100, bbox_inches='tight')
plt.close()
print("✓ Day 8: Teacher-wise Performan")

# INSIGHTs:
# 1. The horizontal bar chart effectively highlights the top 15 teachers based on their average scores, allowing for easy comparison of their performance.
# 2. The chart provides a clear visual representation of the teachers' performance, making it