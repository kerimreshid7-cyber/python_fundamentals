import pandas as pd
import matplotlib.pyplot as plt

school_df = pd.read_csv('/home/kerim/Desktop/python_fundamentals/school_data.csv')

status_counts = school_df['status'].value_counts()
plt.figure(figsize=(10, 7))
colors = ['#2ecc71', '#e74c3c']
plt.bar(status_counts.index, status_counts.values, color=colors, edgecolor='black', width=0.5)
plt.ylabel('Count', fontsize=12, fontweight='bold')
plt.title('Day 6: Pass/Fail Ratio', fontsize=14, fontweight='bold')
for i, v in enumerate(status_counts.values):
    plt.text(i, v + 20, str(v), ha='center', fontweight='bold')
plt.grid(axis='y', alpha=0.3)
plt.savefig('/home/kerim/Desktop/python_fundamentals/90_days_viz_challenge/evidences/day06_pass_fail_ratio.png', dpi=100, bbox_inches='tight')
plt.close()
print("✓ Day 6: Pass/Fail Ratio")
