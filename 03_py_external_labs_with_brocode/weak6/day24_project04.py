

# Hello how are you taday i am gonna cover subplots and i will practce by integrating real company data set.
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

print(plt.subplots(3,2))
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

""""
Project: Football Club Performance Dashboard

Description
-----------
This project demonstrates how to build a professional dashboard
using Matplotlib subplots.

The dashboard visualizes key football performance metrics:

1. Goals scored per month (Line Chart)
2. Match results: Wins, Draws, and Losses (Bar Chart)
3. Goal contribution by top scorers (Pie Chart)
4. Distribution of goals scored per match (Histogram)
"""

# Goals scored per month
months = ["Aug", "Sep", "Oct", "Nov", "Dec", "Jan"]
goals_per_month = [8, 12, 10, 15, 13, 18]

# Match results
results = ["Wins", "Draws", "Losses"]
counts = [18, 6, 4]

# Top scorers
players = ["Salah", "Diaz", "Gakpo", "Others"]
goals = [20, 12, 10, 18]

# Goals scored in each match
match_goals = [2, 1, 3, 2, 4, 1, 0, 2, 3, 1,
               2, 5, 1, 3, 2, 4, 0, 1, 2, 3]

# Create dashboard
fig, axes = plt.subplots(2, 2, figsize=(12, 8))

# ---------------------------
# 1. Line Chart
# ---------------------------
axes[0, 0].plot(months, goals_per_month, marker="o")
axes[0, 0].set_title("Goals Scored Per Month")
axes[0, 0].set_xlabel("Month")
axes[0, 0].set_ylabel("Goals")
axes[0, 0].grid(True)

# ---------------------------
# 2. Bar Chart
# ---------------------------
axes[0, 1].bar(results, counts)
axes[0, 1].set_title("Match Results")
axes[0, 1].set_ylabel("Number of Matches")

# ---------------------------
# 3. Pie Chart
# ---------------------------
axes[1, 0].pie(goals, labels=players, autopct="%1.1f%%")
axes[1, 0].set_title("Goal Contribution")

# ---------------------------
# 4. Histogram
# ---------------------------
axes[1, 1].hist(match_goals, bins=6)
axes[1, 1].set_title("Distribution of Goals Per Match")
axes[1, 1].set_xlabel("Goals Scored")
axes[1, 1].set_ylabel("Frequency")

# Dashboard title
fig.suptitle("Football Club Performance Dashboard", fontsize=16)

# Prevent overlapping
plt.tight_layout()

# Show dashboard
plt.show()