"""Project description: Score By Subject Box.
This script creates a visualization that explores score by subject box in the dataset for the 90 Days of Visualization Challenge."""

import pandas as pd
import matplotlib.pyplot as plt

school_df = pd.read_csv('/home/kerim/Desktop/python_fundamentals/school_data.csv')

plt.figure(figsize=(14, 7))
school_df.boxplot(column='score', by='subject', figsize=(14, 7))
plt.xlabel('Subject', fontsize=12, fontweight='bold')
plt.ylabel('Score', fontsize=12, fontweight='bold')
plt.title('Day 26: Score Distribution by Subject (Box Plot)', fontsize=14, fontweight='bold')
plt.suptitle('')
plt.xticks(rotation=45, ha='right')
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig('/home/kerim/Desktop/python_fundamentals/90_days_viz_challenge/evidences/day26_score_by_subject_box.png', dpi=100, bbox_inches='tight')
plt.close()
print("✓ Day 26: Score by Subject Box Plot")
