
import pandas as pd
print('==================here we go this is the mini project to practice series and data frame ==========================')

total_usage = pd.Series({
    "Ali": 4.4,
    "Sara": 2.8,
    "John": 5.1,
    "Mona": 3.7
})

print(total_usage)
#tenation
# #  Scenario

# # You are analyzing internet usage (GB) of students for 3 months.

# # Students:
# # Ali, Sara, John, Mona

# # Months:
# # January, February, March

# #  Tasks (Try first, solution below)
# # Task 1 — Create a Series

# # Create a Series showing total usage per student:

# # Ali 4.4
# # Sara 2.8
# # John 5.1
# # Mona 3.7


print('==================here we go this is the mini project to practice series and data frame ==========================')

total_usage = pd.Series({
    "Ali": 4.4,
    "Sara": 2.8,
    "John": 5.1,
    "Mona": 3.7
})

print(total_usage)


# Task 2 — Create a DataFrame

# Create a DataFrame of monthly usage:

# Student	Jan	Feb	Mar
# Ali	1.2	1.5	1.7
# Sara	0.8	0.9	1.1
# John	1.5	1.7	1.9
# Mona	1.0	1.2	1.5
# Set students as index.

data = {
    "Jan": [1.2, 0.8, 1.5, 1.0],
    "Feb": [1.5, 0.9, 1.7, 1.2],
    "Mar": [1.7, 1.1, 1.9, 1.5]
}

students = ["Ali", "Sara", "John", "Mona"]

df = pd.DataFrame(data, index=students)
print(df)

