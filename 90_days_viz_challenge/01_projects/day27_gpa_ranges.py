"""Project description: Gpa Ranges.
This script creates a visualization that explores gpa ranges in the dataset for the 90 Days of Visualization Challenge."""

import pandas as pd
import matplotlib.pyplot as plt

school_df = pd.read_csv('/home/kerim/Desktop/python_fundamentals/school_data.csv')

gpa_bins = [0, 2.5, 3.0, 3.5, 4.0]
gpa_labels = ['0-2.5', '2.5-3.0', '3.0-3.5', '3.5-4.0']
gpa_ranges = pd.cut(school_df['gpa'], bins=gpa_bins, labels=gpa_labels)
plt.figure(figsize=(10, 7))
gpa_ranges.value_counts().sort_index().plot(kind='bar', color='lightblue', edgecolor='black')
plt.xlabel('GPA Range', fontsize=12, fontweight='bold')
plt.ylabel('Count', fontsize=12, fontweight='bold')
plt.title('Day 27: GPA Ranges Distribution', fontsize=14, fontweight='bold')
plt.xticks(rotation=0)
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('/home/kerim/Desktop/python_fundamentals/90_days_viz_challenge/evidences/day27_gpa_ranges.png', dpi=100, bbox_inches='tight')
plt.close()
print("✓ Day 27: GPA Ranges Distribution")

# Insights:
# 1. The majority of students fall within the 3.0-3.5 GPA range, indicating a strong academic performance among the student population.
# 2. The 0-2.5 GPA range has the lowest count, suggesting a smaller number of students with lower academic performance.