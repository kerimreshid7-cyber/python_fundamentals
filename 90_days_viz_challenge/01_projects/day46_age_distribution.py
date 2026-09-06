"""Project description: Age Distribution.
This script creates a visualization that explores age distribution in the dataset for the 90 Days of Visualization Challenge."""

import pandas as pd
import matplotlib.pyplot as plt

hospital_df = pd.read_csv('/home/kerim/Desktop/python_fundamentals/hospital_data.csv')

plt.figure(figsize=(12, 7))
plt.hist(hospital_df['age'], bins=30, color='salmon', edgecolor='black', alpha=0.7)
plt.xlabel('Age', fontsize=12, fontweight='bold')
plt.ylabel('Frequency', fontsize=12, fontweight='bold')
plt.title('Day 46: Patient Age Distribution', fontsize=14, fontweight='bold')
plt.grid(axis='y', alpha=0.3)
plt.savefig('/home/kerim/Desktop/python_fundamentals/90_days_viz_challenge/evidences/day46_age_distribution.png', dpi=100, bbox_inches='tight')
plt.close()
print("✓ Day 46: Age Distribution")

# Insights:
# 1. The age distribution of patients shows a peak in the 30-40 age range, indicating that this age group is the most common among the patients in the dataset. 
# 2. There is a noticeable decline in the number of patients in the older age groups, suggesting that fewer elderly patients are represented in the dataset.