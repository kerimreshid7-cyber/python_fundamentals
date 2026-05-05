# Hello how are you today.
# These days i have final exams and i am very busy with my studies but i will try to do one mini project every day to practice what i have learned at all.

"""
PROJECT 1 — Executive KPI Report

This script calculates core business KPIs used by executives
to evaluate company performance.
"""

import pandas as pd

df = pd.read_csv("03_py_external_labs_by_brocode/weak3_mini_projects/a_business_data_2800.csv")

total_revenue = df["revenue"].sum()
total_orders = df["order_id"].nunique()
avg_order_value = df["revenue"].mean()
return_rate = df["returned"].mean() * 100

print("\n" + "="*40)
print("EXECUTIVE KPI REPORT")
print("="*40)
print(f"Total Revenue: ${total_revenue:,.2f}")
print(f"Total Orders: {total_orders}")
print(f"Average Order Value: ${avg_order_value:.2f}")
print(f"Return Rate: {return_rate:.2f}%")
print("="*40)


print('======================================for sure the manager will love this report')




