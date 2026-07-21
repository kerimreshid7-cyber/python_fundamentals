"""Project description: Score Distribution.
This script creates a visualization that explores score distribution in the dataset for the 90 Days of Visualization Challenge."""

import pandas as pd
import matplotlib.pyplot as plt

school_df = pd.read_csv('/home/kerim/Desktop/python_fundamentals/school_data.csv')

plt.figure(figsize=(12, 7))
plt.hist(school_df['score'], bins=30, color='skyblue', edgecolor='black', alpha=0.7)
plt.xlabel('Score', fontsize=12, fontweight='bold')
plt.ylabel('Frequency', fontsize=12, fontweight='bold')
plt.title('Day 1: Score Distribution Histogram', fontsize=14, fontweight='bold')
plt.grid(axis='y', alpha=0.3)
plt.savefig('/home/kerim/Desktop/python_fundamentals/90_days_viz_challenge/evidences/day01_score_distribution.png', dpi=100, bbox_inches='tight')
plt.close()
print("✓ Day 1: Score Distribution Histogram")

# Insights:
# 1. The majority of students have scores between 60 and 80.
# 2. There are a few students with scores below 40, indicating potential areas for improvement.