"""Project description: Subject Popularity.
This script creates a visualization that explores subject popularity in the dataset for the 90 Days of Visualization Challenge."""

import pandas as pd
import matplotlib.pyplot as plt

school_df = pd.read_csv('/home/kerim/Desktop/python_fundamentals/school_data.csv')

subject_pop = school_df['subject'].value_counts()
plt.figure(figsize=(12, 7))
plt.barh(subject_pop.index, subject_pop.values, color='coral', edgecolor='black')
plt.xlabel('Number of Students', fontsize=12, fontweight='bold')
plt.title('Day 34: Subject Popularity', fontsize=14, fontweight='bold')
for i, v in enumerate(subject_pop.values):
    plt.text(v + 5, i, str(v), va='center', fontweight='bold')
plt.grid(axis='x', alpha=0.3)
plt.tight_layout()
plt.savefig('/home/kerim/Desktop/python_fundamentals/90_days_viz_challenge/evidences/day34_subject_popularity.png', dpi=100, bbox_inches='tight')
plt.close()
print("✓ Day 34: Subject Popularity")
