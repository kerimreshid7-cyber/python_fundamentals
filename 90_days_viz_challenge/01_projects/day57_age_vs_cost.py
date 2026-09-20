"""Project description: Age Vs Cost.
This script creates a visualization that explores age vs cost in the dataset for the 90 Days of Visualization Challenge."""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

hospital_df = pd.read_csv('/home/kerim/Desktop/python_fundamentals/hospital_data.csv')

plt.figure(figsize=(12, 7))
scatter = plt.scatter(hospital_df['age'], hospital_df['treatment_cost'], alpha=0.5, c=hospital_df['age'], cmap='viridis', s=50)
z = np.polyfit(hospital_df['age'], hospital_df['treatment_cost'], 1)
p = np.poly1d(z)
plt.plot(hospital_df['age'].sort_values(), p(hospital_df['age'].sort_values()), "r--", linewidth=2, label='Trend')
plt.xlabel('Age', fontsize=12, fontweight='bold')
plt.ylabel('Treatment Cost ($)', fontsize=12, fontweight='bold')
plt.title('Day 57: Age vs Treatment Cost', fontsize=14, fontweight='bold')
plt.colorbar(scatter, label='Age')
plt.legend()
plt.grid(alpha=0.3)
plt.savefig('/home/kerim/Desktop/python_fundamentals/90_days_viz_challenge/evidences/day57_age_vs_cost.png', dpi=100, bbox_inches='tight')
plt.close()
print("✓ Day 57: Age vs Treatment Cost")
