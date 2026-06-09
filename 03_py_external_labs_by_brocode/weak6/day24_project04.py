

# Hello how are you taday i am gonna finish the remainig concepts in the video and i will practce by integrating real company data set
# the video is just to get hint and order bc bro is smart to do that but ineed to go further so i will learn with chat gpt and others  finally i will do mini project.


# subplot
# A subplot means putting multiple graphs inside one figure (window).
# for example   Graph 1: # Revenue Chart
# Graph 2: # Orders Chart
# Graph 3: Customers by month       we can display these all once.

from pathlib import Path
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# print(plt.subplots(3,2))
plt.figure()
figure,axes=plt.subplots(2,2)
x=np.array([1,2,3,4,5])
axes[0,0].plot(x,1/x)
axes[0,0].set_title('x,1/x')

axes[0,1].bar(x,x**2)
axes[1,0].hist(x,x*2)
axes[1,1].pie(x,x/x)



plt.figure()
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]

revenue = [45000, 50000, 47000, 60000, 65000, 70000]
orders = [300, 320, 310, 400, 430, 450]


fig, axes = plt.subplots(1, 2, figsize=(10, 4))

# Revenue Chart
axes[0].bar(months, revenue)
axes[0].set_title("Monthly Revenue")
axes[0].set_ylabel("Revenue ($)")

# Orders Chart
axes[1].plot(months, orders, marker="o")
axes[1].set_title("Monthly Orders")
axes[1].set_ylabel("Orders")

plt.tight_layout()  #To adjustAutomatically  the spacing between graphs so that titles, labels, and axes don't overlap.
plt.show()

# """
# Business Project 4 — Quantity vs Revenue
# """

# BASE_DIR = Path(__file__).resolve().parent
# PLOTS_DIR = BASE_DIR / "plots"
# PLOTS_DIR.mkdir(exist_ok=True)

# df = pd.read_csv(BASE_DIR / "a_business_data_2800.csv", parse_dates=["order_date"])
# plt.figure(figsize=(10, 6))
# sns.regplot(data=df, x="quantity", y="revenue", scatter_kws={"alpha": 0.4}, line_kws={"color": "#d62728"})
# plt.title("Quantity vs Revenue")
# plt.xlabel("Quantity")
# plt.ylabel("Revenue")
# plt.tight_layout()
# plt.savefig(PLOTS_DIR / "project04_quantity_vs_revenue.png", dpi=150)
# plt.close()
# print("Saved plots/project04_quantity_vs_revenue.png")
