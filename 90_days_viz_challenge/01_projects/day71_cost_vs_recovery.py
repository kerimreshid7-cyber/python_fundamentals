"""Project description: Cost Vs Recovery.
This script creates a visualization that explores cost vs recovery in the dataset for the 90 Days of Visualization Challenge."""

import pandas as pd
import matplotlib.pyplot as plt

hospital_df = pd.read_csv('/home/kerim/Desktop/python_fundamentals/hospital_data.csv')

plt.figure(figsize=(12, 7))
hospital_df.boxplot(column='treatment_cost', by='recovery_status', figsize=(12, 7))
plt.xlabel('Recovery Status', fontsize=12, fontweight='bold')
plt.ylabel('Treatment Cost ($)', fontsize=12, fontweight='bold')
plt.title('Day 71: Treatment Cost vs Recovery Status', fontsize=14, fontweight='bold')
plt.suptitle('')
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig('/home/kerim/Desktop/python_fundamentals/90_days_viz_challenge/evidences/day71_cost_vs_recovery.png', dpi=100, bbox_inches='tight')
plt.close()
print("✓ Day 71: Treatment Cost vs Recovery Status")
