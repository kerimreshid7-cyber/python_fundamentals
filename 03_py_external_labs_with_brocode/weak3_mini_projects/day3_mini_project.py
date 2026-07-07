"""
PROJECT 2 — Country Revenue Analysis
Identify strongest and weakest markets.
"""

import pandas as pd

df = pd.read_csv("03_py_external_labs_with_brocode/weak3_mini_projects/a_business_data_2800.csv")

country_rev = df.groupby("country")["revenue"].sum().sort_values(ascending=False)

print("\nTOP PERFORMING COUNTRIES\n")
print(country_rev)

print("\nBEST MARKET:", country_rev.idxmax())
print("WEAKEST MARKET:", country_rev.idxmin())




# Insights:
# • Identify expansion opportunities
# • Find underperforming regions


# finally , i  understod how to think like a data analyst not only that i also learned how to concatinate what i learned in the previous mini projects. 