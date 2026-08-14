"""Project description: Cumulative Score.
This script creates a visualization that explores cumulative score in the dataset for the 90 Days of Visualization Challenge."""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

school_df = pd.read_csv('/home/kerim/Desktop/python_fundamentals/school_data.csv')

sorted_scores = np.sort(school_df['score'])
plt.figure(figsize=(12, 7))
plt.plot(sorted_scores, np.arange(1, len(sorted_scores) + 1), linewidth=2, color='darkblue')
plt.xlabel('Score', fontsize=12, fontweight='bold')
plt.ylabel('Cumulative Count', fontsize=12, fontweight='bold')
plt.title('Day 30: Cumulative Score Distribution', fontsize=14, fontweight='bold')
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig('/home/kerim/Desktop/python_fundamentals/90_days_viz_challenge/evidences/day30_cumulative_score.png', dpi=100, bbox_inches='tight')
plt.close()
print("✓ Day 30: Cumulative Score Distribution")
