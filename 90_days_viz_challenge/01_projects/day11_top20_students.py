import pandas as pd
import matplotlib.pyplot as plt

school_df = pd.read_csv('/home/kerim/Desktop/python_fundamentals/school_data.csv')

top_students = school_df.nlargest(20, 'score')[['name', 'score']].reset_index(drop=True)
plt.figure(figsize=(14, 8))
plt.barh(range(len(top_students)), top_students['score'].values, color='gold', edgecolor='black')
plt.yticks(range(len(top_students)), top_students['name'].values, fontsize=9)
plt.xlabel('Score', fontsize=12, fontweight='bold')
plt.title('Day 11: Top 20 Students by Score', fontsize=14, fontweight='bold')
plt.grid(axis='x', alpha=0.3)
plt.tight_layout()
plt.savefig('/home/kerim/Desktop/python_fundamentals/90_days_viz_challenge/evidences/day11_top20_students.png', dpi=100, bbox_inches='tight')
plt.close()
print("✓ Day 11: Top 20 Students by Score")
