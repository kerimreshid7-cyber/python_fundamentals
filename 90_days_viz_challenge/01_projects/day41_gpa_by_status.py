"""Project description: Gpa By Status.
This script creates a visualization that explores gpa by status in the dataset for the 90 Days of Visualization Challenge."""

import pandas as pd
import matplotlib.pyplot as plt

school_df = pd.read_csv('/home/kerim/Desktop/python_fundamentals/school_data.csv')

plt.figure(figsize=(12, 7))
school_df.boxplot(column='gpa', by='status', figsize=(12, 7))
plt.xlabel('Status', fontsize=12, fontweight='bold')
plt.ylabel('GPA', fontsize=12, fontweight='bold')
plt.title('Day 41: GPA Distribution by Status (Pass/Fail)', fontsize=14, fontweight='bold')
plt.suptitle('')
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig('/home/kerim/Desktop/python_fundamentals/90_days_viz_challenge/evidences/day41_gpa_by_status.png', dpi=100, bbox_inches='tight')
plt.close()
print("✓ Day 41: GPA vs Status")
