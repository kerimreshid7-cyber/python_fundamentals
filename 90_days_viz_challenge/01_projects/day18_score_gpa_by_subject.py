"""Project description: Score Gpa By Subject.
This script creates a visualization that explores score gpa by subject in the dataset for the 90 Days of Visualization Challenge."""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

school_df = pd.read_csv('/home/kerim/Desktop/python_fundamentals/school_data.csv')

fig, ax = plt.subplots(figsize=(14, 8))
subjects = school_df['subject'].unique()
colors_map = plt.cm.tab10(np.linspace(0, 1, len(subjects)))
for i, subject in enumerate(subjects):
    subject_data = school_df[school_df['subject'] == subject]
    ax.scatter(subject_data['score'], subject_data['gpa'], label=subject, alpha=0.6, s=30, c=[colors_map[i]])
plt.xlabel('Score', fontsize=12, fontweight='bold')
plt.ylabel('GPA', fontsize=12, fontweight='bold')
plt.title('Day 18: Score vs GPA by Subject', fontsize=14, fontweight='bold')
plt.legend(loc='best', fontsize=9)
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig('/home/kerim/Desktop/python_fundamentals/90_days_viz_challenge/evidences/day18_score_gpa_by_subject.png', dpi=100, bbox_inches='tight')
plt.close()
print("✓ Day 18: Score vs GPA by Subject")

# Insights:
# 1. The scatter plot provides a visual representation of the relationship between score and GPA for each subject, allowing for easy comparison of performance across different subjects.
# 2. This visualization can help identify trends and patterns in student performance, which can inform teaching strategies and curriculum development for each subject.