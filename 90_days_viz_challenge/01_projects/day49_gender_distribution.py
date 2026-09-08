"""Project description: Gender Distribution.
This script creates a visualization that explores gender distribution in the dataset for the 90 Days of Visualization Challenge."""

import pandas as pd
import matplotlib.pyplot as plt

hospital_df = pd.read_csv('/home/kerim/Desktop/python_fundamentals/hospital_data.csv')

gender_counts = hospital_df['gender'].value_counts()
plt.figure(figsize=(10, 7))
colors = ['#ff6b6b', '#4ecdc4']
plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', colors=colors, startangle=90)
plt.title('Day 49: Gender Distribution', fontsize=14, fontweight='bold')
plt.savefig('/home/kerim/Desktop/python_fundamentals/90_days_viz_challenge/evidences/day49_gender_distribution.png', dpi=100, bbox_inches='tight')
plt.close()
print("✓ Day 49: Gender Distribution")
