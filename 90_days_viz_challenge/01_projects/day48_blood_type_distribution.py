"""Project description: Blood Type Distribution.
This script creates a visualization that explores blood type distribution in the dataset for the 90 Days of Visualization Challenge."""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

hospital_df = pd.read_csv('/home/kerim/Desktop/python_fundamentals/hospital_data.csv')

blood_counts = hospital_df['blood_type'].value_counts()
plt.figure(figsize=(10, 7))
colors = plt.cm.Spectral(np.linspace(0, 1, len(blood_counts)))
plt.pie(blood_counts, labels=blood_counts.index, autopct='%1.1f%%', colors=colors, startangle=90)
plt.title('Day 48: Blood Type Distribution', fontsize=14, fontweight='bold')
plt.savefig('/home/kerim/Desktop/python_fundamentals/90_days_viz_challenge/evidences/day48_blood_type_distribution.png', dpi=100, bbox_inches='tight')
plt.close()
print("✓ Day 48: Blood Type Distribution")
