"""Project description: Doctor Recovery Rate.
This script creates a visualization that explores doctor recovery rate in the dataset for the 90 Days of Visualization Challenge."""

import pandas as pd
import matplotlib.pyplot as plt

hospital_df = pd.read_csv('/home/kerim/Desktop/python_fundamentals/hospital_data.csv')

doctor_recovered = hospital_df[hospital_df['recovery_status'] == 'Recovered'].groupby('doctor').size()
doctor_total = hospital_df.groupby('doctor').size()
doctor_recovery_rate = (doctor_recovered / doctor_total * 100).sort_values(ascending=False).head(15)
plt.figure(figsize=(12, 7))
doctor_recovery_rate.plot(kind='barh', color='mediumpurple', edgecolor='black')
plt.xlabel('Recovery Rate (%)', fontsize=12, fontweight='bold')
plt.title('Day 67: Top 15 Doctors by Recovery Rate', fontsize=14, fontweight='bold')
plt.grid(axis='x', alpha=0.3)
plt.tight_layout()
plt.savefig('/home/kerim/Desktop/python_fundamentals/90_days_viz_challenge/evidences/day67_doctor_recovery_rate.png', dpi=100, bbox_inches='tight')
plt.close()
print("✓ Day 67: Doctor Effectiveness")

# insights:
# 1. The horizontal bar chart illustrates the recovery rate for the top 15 doctors, providing a clear view of doctor effectiveness in terms of patient recovery.
# 2. Analyzing doctor recovery rates can help hospital administrators identify high-performing doctors, improve patient care, and implement best practices across the medical staff to enhance overall treatment outcomes.