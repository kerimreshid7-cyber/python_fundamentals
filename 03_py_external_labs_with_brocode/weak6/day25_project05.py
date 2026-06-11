


# Hello how are you today I am gonna cover the remaining concept in the video which is the most important thing in analysis.
# lets get started.
# today  i will cover how we can visualize dataframe by integrating pandas and matplotlib.finally i will do mini project to get practical knowledge.

from pathlib import Path
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# df = pd.read_csv("03_py_external_labs_with_brocode/weak3_mini_projects/a_business_data_2800.csv")

# # print(df.columns.tolist())

# type_count=df['country'].value_counts()

# plt.bar(type_count.index,type_count.values)
# plt.show()


"""
Project 5: Customer Distribution by Country

Description
-----------
This project analyzes customer geographic distribution
using business transaction data.

The goal is to answer the following business question:

1. Which countries have the highest number of customers?

Business Value
--------------
Understanding customer distribution helps businesses:

- Identify key markets
- Allocate marketing budgets effectively
- Discover expansion opportunities
- Support regional business strategies

Skills Demonstrated
-------------------
- Pandas Data Analysis
- Data Aggregation
- Value Counts
- Data Visualization with Matplotlib
- Business-Oriented Reporting

Author: Bilal Habesha
"""

import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv(
    "03_py_external_labs_with_brocode/weak3_mini_projects/a_business_data_2800.csv"
)

# Count customers by country
country_counts = df["country"].value_counts()

# Display summary
print("Customer Count by Country")
print("-" * 30)
print(country_counts)

# Create visualization
plt.figure(figsize=(10, 6))
plt.bar(country_counts.index, country_counts.values)

plt.title("Customer Distribution by Country")
plt.xlabel("Country")
plt.ylabel("Number of Customers")

plt.xticks(rotation=45)
plt.tight_layout()

plt.show()