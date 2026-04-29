import re
import pandas as pd

# open the SQL file (now directly in project folder)
with open("data_insertion.sql", "r", encoding="utf-8") as f:
    text = f.read()

# extract rows inside parentheses
rows = re.findall(r"\((.*?)\)", text)

clean_rows = []
for row in rows:
    row = row.replace("'", "")
    row = row.replace("NULL", "")
    clean_rows.append(row.split(","))

columns = [
    "id","name","email","phone","payment_method",
    "product","category","price","quantity",
    "discount","order_date","shipping_date"
]

df = pd.DataFrame(clean_rows, columns=columns)

# save CSV in same folder
df.to_csv("orders.csv", index=False)

print("CSV created successfully!")

print(df.to_string())
df = pd.read_csv("orders.csv")
leable=[f'cus{cus}' for cus in range(1,len(df)+1)]
df.index=leable     # this is another way to give an index own self.

print(df)     # we will get the first 5 and last 5 rows and the discribtion for how many rows and columns we have

#print(df.head())    to get first 5 rows

#print(df.to_string())    # to get every thing in the data frame.















