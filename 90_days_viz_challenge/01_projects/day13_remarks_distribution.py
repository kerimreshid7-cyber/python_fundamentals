"""Project description: Remarks Distribution.
This script creates a visualization that explores remarks distribution in the dataset for the 90 Days of Visualization Challenge."""

import pandas as pd
import matplotlib.pyplot as plt

school_df = pd.read_csv('/home/kerim/Desktop/python_fundamentals/school_data.csv')

remarks_counts = school_df['remarks'].value_counts()
plt.figure(figsize=(10, 7))
colors = ['#27ae60', '#3498db', '#f39c12', '#e74c3c']
plt.pie(remarks_counts, labels=remarks_counts.index, autopct='%1.1f%%', colors=colors, startangle=90)
plt.title('Day 13: Student Remarks Distribution', fontsize=14, fontweight='bold')
plt.savefig('/home/kerim/Desktop/python_fundamentals/90_days_viz_challenge/evidences/day13_remarks_distribution.png', dpi=100, bbox_inches='tight')
plt.close()
print("✓ Day 13: Remarks Distribution")
