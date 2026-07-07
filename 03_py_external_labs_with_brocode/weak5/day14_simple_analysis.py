"""
Average Basket Size
How many items customers buy per order.
"""

import pandas as pd

df = pd.read_csv("03_py_external_labs_by_brocode/weak3_mini_projects/a_business_data_2800.csv")

basket = df.groupby("order_id")["quantity"].sum().mean()
print("\nAverage Items Per Order:", basket)


# insights
# The average basket size indicates that customers are purchasing a moderate number of items per order, which
# can be useful for inventory management and marketing strategies. Businesses can use this information to optimize their product offerings and promotions to encourage larger purchases, ultimately increasing revenue.
# Additionally, understanding the average basket size can help in forecasting demand and managing supply chain logistics more effectively.