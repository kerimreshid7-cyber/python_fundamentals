"""Project description: Correlation Heatmap.
This script creates a visualization that explores correlation heatmap in the dataset for the 90 Days of Visualization Challenge."""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

school_df = pd.read_csv('/home/kerim/Desktop/python_fundamentals/school_data.csv')

correlation = school_df[['score', 'gpa', 'attendance_percentage']].corr()
plt.figure(figsize=(10, 8))
sns.heatmap(correlation, annot=True, cmap='coolwarm', center=0, square=True, cbar_kws={'label': 'Correlation'})
plt.title('Day 43: Correlation Heatmap (Score, GPA, Attendance)', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('/home/kerim/Desktop/python_fundamentals/90_days_viz_challenge/evidences/day43_correlation_heatmap.png', dpi=100, bbox_inches='tight')
plt.close()
print("✓ Day 43: Correlation Heatmap")
