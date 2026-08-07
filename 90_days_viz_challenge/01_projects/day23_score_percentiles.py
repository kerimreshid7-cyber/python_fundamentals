"""Project description: Score Percentiles.
This script creates a visualization that explores score percentiles in the dataset for the 90 Days of Visualization Challenge."""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

school_df = pd.read_csv('/home/kerim/Desktop/python_fundamentals/school_data.csv')

percentiles = [10, 25, 50, 75, 90]
perc_values = [np.percentile(school_df['score'], p) for p in percentiles]
plt.figure(figsize=(12, 7))
plt.bar([f'{p}th' for p in percentiles], perc_values, color='skyblue', edgecolor='black')
plt.ylabel('Score', fontsize=12, fontweight='bold')
plt.title('Day 23: Score Percentiles', fontsize=14, fontweight='bold')
for i, v in enumerate(perc_values):
    plt.text(i, v + 1, f'{v:.1f}', ha='center', fontweight='bold')
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('/home/kerim/Desktop/python_fundamentals/90_days_viz_challenge/evidences/day23_score_percentiles.png', dpi=100, bbox_inches='tight')
plt.close()
print("✓ Day 23: Score Percentiles")

# Insights:
# 1. The bar chart provides a clear visual representation of the score distribution across different percentiles, allowing for easy comparison of student performance at various levels.
# 2. This visualization can help identify the range of scores that students are achieving, which can inform targeted interventions and support strategies to improve student outcomes.