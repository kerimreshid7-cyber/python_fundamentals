"""Project description: Visit Timeline.
This script creates a visualization that explores visit timeline in the dataset for the 90 Days of Visualization Challenge."""

import pandas as pd
import matplotlib.pyplot as plt

hospital_df = pd.read_csv('/home/kerim/Desktop/python_fundamentals/hospital_data.csv')

hospital_df['visit_date_converted'] = pd.to_datetime(hospital_df['visit_date'])
visit_timeline = hospital_df.groupby(hospital_df['visit_date_converted'].dt.date).size()
plt.figure(figsize=(14, 7))
plt.plot(visit_timeline.index, visit_timeline.values, linewidth=2, marker='o', markersize=4, color='steelblue')
plt.xlabel('Date', fontsize=12, fontweight='bold')
plt.ylabel('Number of Visits', fontsize=12, fontweight='bold')
plt.title('Day 64: Visit Timeline', fontsize=14, fontweight='bold')
plt.xticks(rotation=45)
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig('/home/kerim/Desktop/python_fundamentals/90_days_viz_challenge/evidences/day64_visit_timeline.png', dpi=100, bbox_inches='tight')
plt.close()
print("✓ Day 64: Visit Date Timeline")

# Insights:
# 1. The line chart illustrates the number of visits over time, providing a clear view of visit trends and patterns.
# 2. Analyzing visit timelines can help hospital management identify peak visit periods, allowing for better resource allocation and scheduling to improve patient care and reduce wait times.