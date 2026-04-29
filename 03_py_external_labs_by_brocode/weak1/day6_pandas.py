
# hello how are you?  today i will cover how can i import csv and json file and selction using pandas.

import pandas as pd

df=pd.read_csv("orders.csv")
print('==========================here we go ===============================')
print(df)
# # print(df.to_string())    # to get every thing in the file.
df = pd.read_csv("orders.csv")
leable=[f'cus{cus}' for cus in range(1,len(df)+1)]
df.index=leable     # this is another way to give an index own self.
print()

print('==========================changed index col ===============================')

print(df)     # we will get the first 5 and last 5 rows and the discribtion for how many rows and columns we have


# this is how we can import csv file and print it.



df2=pd.read_json('stu.json')
leble=[f'stu{stu}' for stu in range(1,len(df2)+1)]
df2.index=leble
print()

print('==========================json changed in to data fram ===============================')

print(df2.to_string)


# selection by column/s
print(df['payment_method'])
print(df2['name'].to_string)   #to get specificcol but all rows using .to_string
print()
print('==========================wow ===============================')

print(df['order_date'])  
print()
print('==========================to select specific columns ===============================')

print(df[['order_date','discount','shipping_date']])     # this is how we can select multiple columns. if needed we can add .to_string immidiate after the root list (after the outer squre brace). 
print()

# selection by row/s
print(df.loc['cus25'])    #so we can easily see the detail of this customer.
print('==========================to select specific row and specific columns ===============================')
print(df.loc['cus34',['name','payment_method']])   # this is how we can select specific row and also specfic column.
print()
print('==========================to select specific rows and columns ===============================')
print(df.loc['cus50':'cus53',['name','payment_method']])  #  this is how we can slice and decide the specific columns regarding toour need. ohhh python i couldn't belive what i doing ohh ohh pyhton. 
print()
print('=============wow python========')
print(df.iloc[3:6])  
print(df.iloc[5:8,:3])

df_df=pd.read_csv('orders.csv',index_col=('name'))     # we can easily change the default index column by what we want that is from our data frame in this case we change it by name so later we can easily select by giving the name.
print(df_df.loc['Ali Hassan'])     # so we can accces like this inthe out i got 5 rows that means this customer appear 5 times the more i practice the more i will understand.


# exercise to check some one(customer) is there or not  using index(name)
print()
print('=============real exercise using index(name)========')

customer=input("enter a customer name:")
try:
    print(df_df.loc[customer])
except KeyError:
    print(f'{customer} not found')


# exercise to check some one(customer) is there or not  using index number(default).
print()
print('=============real exercise using index number(default).========')

customer2=int(input("enter a customer name:"))
try:
    print(df.iloc[customer2])
except:
    print(f'{customer2} not found')










