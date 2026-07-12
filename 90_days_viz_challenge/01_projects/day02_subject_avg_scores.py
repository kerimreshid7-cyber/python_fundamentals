

import pandas as pd
import matplotlib.pyplot as plt

school_df = pd.read_csv('/home/kerim/Desktop/python_fundamentals/school_data.csv')

subject_avg = school_df.groupby('subject')['score'].mean().sort_values(ascending=False)
plt.figure(figsize=(12, 7))
subject_avg.plot(kind='barh', color='coral', edgecolor='black')
plt.xlabel('Average Score', fontsize=12, fontweight='bold')
plt.title('Day 2: Subject-wise Average Scores', fontsize=14, fontweight='bold')
plt.grid(axis='x', alpha=0.3)
plt.tight_layout()
plt.savefig('/home/kerim/Desktop/python_fundamentals/90_days_viz_challenge/evidences/day02_subject_avg_scores.png', dpi=100, bbox_inches='tight')
plt.close()
print("✓ Day 2: Subject-wise Average Scores")

# Insights:
# 1. The subject with the highest average score is 'Mathematics', indicating strong performance in that area.
# 2. 'Science' and 'English' follow with moderate average scores, suggesting room for improvement.
# 3. 'History' has the lowest average score, highlighting a potential need for targeted support or curriculum adjustments.