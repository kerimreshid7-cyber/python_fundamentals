"""Project description: Doctor Patient Count.
This script creates a visualization that explores doctor patient count in the dataset for the 90 Days of Visualization Challenge."""

import pandas as pd
import matplotlib.pyplot as plt

hospital_df = pd.read_csv('/home/kerim/Desktop/python_fundamentals/hospital_data.csv')

doctor_count = hospital_df['doctor'].value_counts().head(15)
plt.figure(figsize=(12, 7))
doctor_count.plot(kind='barh', color='mediumpurple', edgecolor='black')
plt.xlabel('Patient Count', fontsize=12, fontweight='bold')
plt.title('Day 56: Top 15 Doctors by Patient Count', fontsize=14, fontweight='bold')
plt.grid(axis='x', alpha=0.3)
plt.tight_layout()
plt.savefig('/home/kerim/Desktop/python_fundamentals/90_days_viz_challenge/evidences/day56_doctor_patient_count.png', dpi=100, bbox_inches='tight')
plt.close()
print("✓ Day 56: Doctor-wise Patient Count")

# Insights:
# 1. The horizontal bar chart provides a clear visual representation of the top 15 doctors by patient count, allowing healthcare administrators to quickly identify which doctors are seeing the most patients.
# 2. Understanding doctor-wise patient distribution can help in resource allocation, workload management, and identifying potential areas for improvement in patient care, ensuring that doctors are not overwhelmed and that patients receive timely attention.