"""Project description: Blood Type By Gender.
This script creates a visualization that explores blood type by gender in the dataset for the 90 Days of Visualization Challenge."""

import pandas as pd
import matplotlib.pyplot as plt

hospital_df = pd.read_csv('/home/kerim/Desktop/python_fundamentals/hospital_data.csv')

blood_gender = pd.crosstab(hospital_df['blood_type'], hospital_df['gender'])
plt.figure(figsize=(12, 7))
blood_gender.plot(kind='bar', ax=plt.gca(), color=['#ff6b6b', '#4ecdc4'], edgecolor='black')
plt.xlabel('Blood Type', fontsize=12, fontweight='bold')
plt.ylabel('Count', fontsize=12, fontweight='bold')
plt.title('Day 65: Blood Type Distribution by Gender', fontsize=14, fontweight='bold')
plt.xticks(rotation=0)
plt.legend(title='Gender')
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('/home/kerim/Desktop/python_fundamentals/90_days_viz_challenge/evidences/day65_blood_type_by_gender.png', dpi=100, bbox_inches='tight')
plt.close()
print("✓ Day 65: Blood Type by Gender")
