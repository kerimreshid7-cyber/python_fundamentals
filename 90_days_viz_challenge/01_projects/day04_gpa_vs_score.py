import pandas as pd
import matplotlib.pyplot as plt

school_df = pd.read_csv('/home/kerim/Desktop/python_fundamentals/school_data.csv')

plt.figure(figsize=(12, 7))
scatter = plt.scatter(school_df['score'], school_df['gpa'], alpha=0.5, c=school_df['gpa'], cmap='viridis', s=50)
plt.xlabel('Score', fontsize=12, fontweight='bold')
plt.ylabel('GPA', fontsize=12, fontweight='bold')
plt.title('Day 4: GPA vs Score', fontsize=14, fontweight='bold')
plt.colorbar(scatter, label='GPA')
plt.grid(alpha=0.3)
plt.savefig('/home/kerim/Desktop/python_fundamentals/90_days_viz_challenge/evidences/day04_gpa_vs_score.png', dpi=100, bbox_inches='tight')
plt.close()
print("✓ Day 4: GPA vs Score Scatter Plot")
