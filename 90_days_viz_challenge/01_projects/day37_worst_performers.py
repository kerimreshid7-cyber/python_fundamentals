"""Project description: Worst Performers.
This script creates a visualization that explores worst performers in the dataset for the 90 Days of Visualization Challenge."""

import pandas as pd
import matplotlib.pyplot as plt

school_df = pd.read_csv('/home/kerim/Desktop/python_fundamentals/school_data.csv')

worst_students = school_df.nsmallest(10, 'score')[['name', 'score']].reset_index(drop=True)
plt.figure(figsize=(14, 7))
plt.barh(range(len(worst_students)), worst_students['score'].values, color='#e74c3c', edgecolor='black')
plt.yticks(range(len(worst_students)), worst_students['name'].values, fontsize=9)
plt.xlabel('Score', fontsize=12, fontweight='bold')
plt.title('Day 37: Bottom 10 Students by Score', fontsize=14, fontweight='bold')
plt.grid(axis='x', alpha=0.3)
plt.tight_layout()
plt.savefig('/home/kerim/Desktop/python_fundamentals/90_days_viz_challenge/evidences/day37_worst_performers.png', dpi=100, bbox_inches='tight')
plt.close()
print("✓ Day 37: Top 10 Worst Performers")
