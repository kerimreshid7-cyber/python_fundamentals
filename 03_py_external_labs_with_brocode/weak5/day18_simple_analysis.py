"""
Day-of-week performance.
"""

import pandas as pd

df = pd.read_csv("03_py_external_labs_by_brocode/weak3_mini_projects/a_business_data_2800.csv")
df["order_date"] = pd.to_datetime(df["order_date"])
df["weekday"] = df["order_date"].dt.day_name()

print(df.groupby("weekday")["revenue"].sum().sort_values(ascending=False))

#insight: 
# The business generates the most revenue on Fridays, followed by Saturdays and Sundays. This suggests that the business may want to focus its marketing efforts on these days to maximize revenue. Additionally, it may be beneficial to analyze the factors contributing to higher revenue on these days, such as promotions, customer behavior, or product offerings, to further optimize sales strategies.
# The lower revenue on Mondays and Tuesdays may indicate an opportunity to implement targeted promotions or marketing campaigns to boost sales on these days. Understanding the reasons behind the variations in revenue across different days of the week can help the business make informed decisions to enhance overall performance.