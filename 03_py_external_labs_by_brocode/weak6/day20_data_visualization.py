# hello everyone, in this video we will be learning about data visualization using matplotlib in python. Data visualization is the graphical representation of information and data. It helps us to understand complex data by presenting it in a visual format. Matplotlib is a popular library in python for creating static, animated, and interactive visualizations. 
# To get started, we need to install matplotlib if we haven't already. You can do this using pip


import matplotlib.pyplot as plt
print(plt.matplotlib.__version__)

# line chart
# Used for trends over time.

import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr"]
sales = [1200, 1500, 1800, 2200]

plt.plot(months, sales)
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()


# 2. Bar Chart
# Used to compare categories.

import matplotlib.pyplot as plt

products = ["A", "B", "C"]
sales = [300, 500, 200]

plt.bar(products, sales)
plt.title("Product Sales")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.show()