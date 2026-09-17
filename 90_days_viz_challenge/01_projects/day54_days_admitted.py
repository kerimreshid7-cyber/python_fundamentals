"""Project description: Days Admitted.
This script creates a visualization that explores days admitted in the dataset for the 90 Days of Visualization Challenge."""

import pandas as pd
import matplotlib.pyplot as plt

hospital_df = pd.read_csv('/home/kerim/Desktop/python_fundamentals/hospital_data.csv')

plt.figure(figsize=(12, 7))
plt.hist(hospital_df['days_admitted'], bins=25, color='lightblue', edgecolor='black', alpha=0.7)
plt.xlabel('Days Admitted', fontsize=12, fontweight='bold')
plt.ylabel('Frequency', fontsize=12, fontweight='bold')
plt.title('Day 54: Days Admitted Distribution', fontsize=14, fontweight='bold')
plt.axvline(hospital_df['days_admitted'].mean(), color='red', linestyle='--', linewidth=2, label=f'Mean: {hospital_df["days_admitted"].mean():.1f}')
plt.legend()
plt.grid(axis='y', alpha=0.3)
plt.savefig('/home/kerim/Desktop/python_fundamentals/90_days_viz_challenge/evidences/day54_days_admitted.png', dpi=100, bbox_inches='tight')
plt.close()
print("✓ Day 54: Days Admitted Distribution")

# Insights:
# 1. The histogram provides a clear visual representation of the distribution of days admitted, allowing healthcare professionals to quickly assess the frequency of different lengths of hospital stays.
# 2. Understanding the distribution of days admitted can help in resource planning, patient flow management, and identifying potential areas for improvement in the admission process, ultimately enhancing patient care and hospital efficiency.