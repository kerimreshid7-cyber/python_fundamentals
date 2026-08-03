"""Project description: Gpa By Grade.
This script creates a visualization that explores gpa by grade in the dataset for the 90 Days of Visualization Challenge."""

import pandas as pd
import matplotlib.pyplot as plt

school_df = pd.read_csv('/home/kerim/Desktop/python_fundamentals/school_data.csv')

plt.figure(figsize=(12, 7))
school_df.boxplot(column='gpa', by='grade', figsize=(12, 7))
plt.xlabel('Grade', fontsize=12, fontweight='bold')
plt.ylabel('GPA', fontsize=12, fontweight='bold')
plt.title('Day 20: GPA Distribution by Grade', fontsize=14, fontweight='bold')
plt.suptitle('')
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig('/home/kerim/Desktop/python_fundamentals/90_days_viz_challenge/evidences/day20_gpa_by_grade.png', dpi=100, bbox_inches='tight')
plt.close()
print("✓ Day 20: Grade-wise GPA Distribution")

# Insights:
#1. The box plot provides a visual representation of the distribution of GPA for each grade, allowing for easy comparison of academic performance across different grade levels.    
#2. This visualization can help identify trends and patterns in GPA distribution, which can inform educational strategies and interventions for students in different grades.