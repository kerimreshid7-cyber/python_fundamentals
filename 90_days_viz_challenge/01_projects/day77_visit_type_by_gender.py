"""Project description: Visit Type By Gender.
This script creates a visualization that explores visit type by gender in the dataset for the 90 Days of Visualization Challenge."""

import pandas as pd
import matplotlib.pyplot as plt

hospital_df = pd.read_csv('/home/kerim/Desktop/python_fundamentals/hospital_data.csv')

visit_gender = pd.crosstab(hospital_df['visit_type'], hospital_df['gender'])
plt.figure(figsize=(12, 7))
visit_gender.plot(kind='bar', ax=plt.gca(), color=['#ff6b6b', '#4ecdc4'], edgecolor='black')
plt.xlabel('Visit Type', fontsize=12, fontweight='bold')
plt.ylabel('Count', fontsize=12, fontweight='bold')
plt.title('Day 77: Visit Type Distribution by Gender', fontsize=14, fontweight='bold')
plt.xticks(rotation=45, ha='right')
plt.legend(title='Gender')
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('/home/kerim/Desktop/python_fundamentals/90_days_viz_challenge/evidences/day77_visit_type_by_gender.png', dpi=100, bbox_inches='tight')
plt.close()
print("✓ Day 77: Visit Type by Gender")
