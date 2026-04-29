
# # Mini Project: Student Monthly Internet Usage

# # You will practice:

# # Creating Series
# # Creating DataFrame
# # Indexing
# # Filtering
# # Calculations
# # Concatenation
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




# import pandas as pd
# print('==================here we go this is the mini project to practice series and data frame ==========================')

# total_usage = pd.Series({
#     "Ali": 4.4,
#     "Sara": 2.8,
#     "John": 5.1,
#     "Mona": 3.7
# })

# print(total_usage)


# # Task 2 — Create a DataFrame

# # Create a DataFrame of monthly usage:

# # Student	Jan	Feb	Mar
# # Ali	1.2	1.5	1.7
# # Sara	0.8	0.9	1.1
# # John	1.5	1.7	1.9
# # Mona	1.0	1.2	1.5
# # Set students as index.

# data = {
#     "Jan": [1.2, 0.8, 1.5, 1.0],
#     "Feb": [1.5, 0.9, 1.7, 1.2],
#     "Mar": [1.7, 1.1, 1.9, 1.5]
# }

# students = ["Ali", "Sara", "John", "Mona"]

# df = pd.DataFrame(data, index=students)
# print(df)



# # Task 3 — Get Sara’s data only
# print(df.loc["Sara"])


# # Task 4 — Get February column only
# print(df["Feb"])


# # Task 5 — Add new column "Total"
# # Total = Jan + Feb + Mar

# df["Total"] = df["Jan"] + df["Feb"] + df["Mar"]
# print(df)



# # Task 6 — Find students who used more than 4GB total
# heavy_users = df[df["Total"] > 4]
# print(heavy_users)


# # Task 7 — Concatenate new student

# # Add new student:
# new_student = pd.DataFrame({
#     "Jan":[1.3],
#     "Feb":[1.4],
#     "Mar":[1.6],
#     "Total":[1.3+1.4+1.6]
# }, index=["David"])

# df = pd.concat([df, new_student])
# print(df)
