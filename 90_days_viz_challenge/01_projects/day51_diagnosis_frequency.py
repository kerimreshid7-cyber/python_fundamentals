"""Project description: Diagnosis Frequency.
This script creates a visualization that explores diagnosis frequency in the dataset for the 90 Days of Visualization Challenge."""

import pandas as pd
import matplotlib.pyplot as plt

hospital_df = pd.read_csv('/home/kerim/Desktop/python_fundamentals/hospital_data.csv')

diagnosis_counts = hospital_df['diagnosis'].value_counts().sort_values(ascending=False)
plt.figure(figsize=(12, 7))
diagnosis_counts.plot(kind='barh', color='coral', edgecolor='black')
plt.xlabel('Frequency', fontsize=12, fontweight='bold')
plt.title('Day 51: Diagnosis Frequency', fontsize=14, fontweight='bold')
plt.grid(axis='x', alpha=0.3)
plt.tight_layout()
plt.savefig('/home/kerim/Desktop/python_fundamentals/90_days_viz_challenge/evidences/day51_diagnosis_frequency.png', dpi=100, bbox_inches='tight')
plt.close()
print("✓ Day 51: Diagnosis Frequency")

# Insights:
# 1. The horizontal bar chart provides a clear view of the frequency of different diagnoses in the dataset, allowing healthcare professionals to identify the most common health issues.
# 2. Understanding diagnosis frequency can help in resource allocation, planning preventive measures, and improving patient care strategies by focusing on prevalent health conditions.