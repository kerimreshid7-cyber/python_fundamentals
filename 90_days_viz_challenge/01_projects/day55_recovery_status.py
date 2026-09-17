"""Project description: Recovery Status.
This script creates a visualization that explores recovery status in the dataset for the 90 Days of Visualization Challenge."""

import pandas as pd
import matplotlib.pyplot as plt

hospital_df = pd.read_csv('/home/kerim/Desktop/python_fundamentals/hospital_data.csv')

recovery_counts = hospital_df['recovery_status'].value_counts()
plt.figure(figsize=(10, 7))
colors = ['#2ecc71', '#f39c12', '#e74c3c']
plt.pie(recovery_counts, labels=recovery_counts.index, autopct='%1.1f%%', colors=colors, startangle=90)
plt.title('Day 55: Recovery Status Distribution', fontsize=14, fontweight='bold')
plt.savefig('/home/kerim/Desktop/python_fundamentals/90_days_viz_challenge/evidences/day55_recovery_status.png', dpi=100, bbox_inches='tight')
plt.close()
print("✓ Day 55: Recovery Status")
