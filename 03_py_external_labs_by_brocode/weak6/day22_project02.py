

# hello how are you today i am gonna learn pie chart and scater graph.

# pie chart is the circular chart to represent the percentage of the total.
# it's good for visiualizing distibution among categories.

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

import matplotlib.pyplot as plt
import numpy as np

# Pie chart  
plt.figure()         # used to display two or more graphs once
categories = ['freshman', 'swe', 'cs']
values = [32, 73, 14]
colors = ['red', 'green', 'yellow']

plt.pie(
    values,
    labels=categories,
    colors=colors,
    autopct='%1.1f%%',
    explode=[0, 0, 0.3],
    shadow=True,
    startangle=180
)
plt.title('Kerim Reshid College')

#scatter is used to show the relation ship between two variables 
# it used to identify corelation (+,-,None)
# example study hour and test result


# Scatter plot
# study_H=[1,4,5,3,2,1,5]
# test_result=[67,86,76,67,76,57,90]
# plt.scatter(study_H,test_result)


# plt.show()

plt.figure()    # used to display two or more graphs once

study_H1 = np.array([1,4,5,3,2,1,5])
test_result1 = np.array([67,86,76,67,76,57,90])

study_H2 = np.array([5,4,7,3,6,1,2])
test_result2 = np.array([67,67,86,85,76,57,32])

plt.scatter(study_H1, test_result1, label='Stu_A')
plt.scatter(study_H2, test_result2, label='Stu_B')

plt.title('Study Hours vs Test Result')
plt.xlabel('Study Hours')
plt.ylabel('Test Result')
plt.legend()

plt.show()
# """
# Business Project 2 — Top Countries by Order Count
# """


# BASE_DIR = Path(__file__).resolve().parent
# PLOTS_DIR = BASE_DIR / "plots"
# PLOTS_DIR.mkdir(exist_ok=True)

# df = pd.read_csv(BASE_DIR / "a_business_data_2800.csv", parse_dates=["order_date"])
# orders_country = df["country"].value_counts().head(10)
# plt.figure(figsize=(8, 8))
# orders_country.plot(kind="pie", autopct="%1.1f%%", startangle=140, pctdistance=0.75)
# plt.title("Top 10 Countries by Order Count")
# plt.ylabel("")
# plt.tight_layout()
# plt.savefig(PLOTS_DIR / "project02_orders_by_country.png", dpi=150)
# plt.close()
# print("Saved plots/project02_orders_by_country.png")

