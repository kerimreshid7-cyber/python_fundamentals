"""Project description: Gpa Distribution.
This script creates a visualization that explores gpa distribution in the dataset for the 90 Days of Visualization Challenge."""

import pandas as pd
import matplotlib.pyplot as plt

school_df = pd.read_csv('/home/kerim/Desktop/python_fundamentals/school_data.csv')

plt.figure(figsize=(12, 7))
plt.hist(school_df['gpa'], bins=30, color='lightblue', edgecolor='black', alpha=0.7)
plt.xlabel('GPA', fontsize=12, fontweight='bold')
plt.ylabel('Frequency', fontsize=12, fontweight='bold')
plt.title('Day 12: GPA Distribution', fontsize=14, fontweight='bold')
plt.axvline(school_df['gpa'].mean(), color='red', linestyle='--', linewidth=2, label=f'Mean: {school_df["gpa"].mean():.2f}')
plt.legend()
plt.grid(axis='y', alpha=0.3)
plt.savefig('/home/kerim/Desktop/python_fundamentals/90_days_viz_challenge/evidences/day12_gpa_distribution.png', dpi=100, bbox_inches='tight')
plt.close()
print("✓ Day 12: GPA Distribution")
