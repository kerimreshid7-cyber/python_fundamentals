"""Project description: Admission Status.
This script creates a visualization that explores admission status in the dataset for the 90 Days of Visualization Challenge."""

import pandas as pd
import matplotlib.pyplot as plt

hospital_df = pd.read_csv('/home/kerim/Desktop/python_fundamentals/hospital_data.csv')

admitted_counts = hospital_df['admitted'].value_counts()
plt.figure(figsize=(10, 7))
colors = ['#e74c3c', '#2ecc71']
plt.pie(admitted_counts, labels=admitted_counts.index, autopct='%1.1f%%', colors=colors, startangle=90)
plt.title('Day 53: Admission Status', fontsize=14, fontweight='bold')
plt.savefig('/home/kerim/Desktop/python_fundamentals/90_days_viz_challenge/evidences/day53_admission_status.png', dpi=100, bbox_inches='tight')
plt.close()
print("✓ Day 53: Admission vs Non-admission")
