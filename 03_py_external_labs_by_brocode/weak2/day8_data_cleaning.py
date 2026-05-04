# Hello today i will finish the remaining concept in the video which is data cleaning.
# 

# Data cleaning is the process of fixing or removing incorrect, corrupted, incorrectly formatted, duplicate, or incomplete data within a dataset. It is an important step in the data analysis process as it helps to ensure that the data is accurate and reliable for analysis.
# As we know data cleaning is very important in data analysis.since 80% of data values in real world are strings so before we analyse them we have to clean them.

import pandas as pd
df=pd.read_csv('full_order_analysis_project/data/orders.csv',index_col='id')

# 1, drop irrelevant columns 
df.drop(columns=['discount'])
print('='*12,'data cleanining','='*12)
print(df)
print(list(df.columns))
print()


# 2, handle missing data
df=df.dropna(subset=['shipping_date'])    # this will drop the rows which have missing values in shipping date column.
df=df.fillna({'shipping_date':'2024-01-01'})    # this will fill the missing values in shipping date column with 2024-01-01

print(df)



# fixing inconsistent values 
df['name']=df['name'].replace({"Ali Hassan":"ali hassan",
                               'Sara Ahmed':"sara ahmed"})

print()

# 4.standardize text
df['name']=df['name'].str.strip().str.lower()




# 5. fix data types
print()

df["name"]=df["name"].astype("string")    # this will change the data type of name column to string
df["price"]=df["price"].astype("float")    # this will change the data


print()

# 6. remove duplicate values
df=df.drop_duplicates()    # this will remove the duplicate rows from the data frame.
print(df)

print('='*12,'this is all bout data cleaning and also pandas by bro code','='*12,'\n','i will continue data visualization.','\n','thank you very much for your time.')
# I have finished every thing in the video i got some practical knowledge about what panda can do and how we can use  for data cleaning so panda is the most important library for data analysis i have to master it  with real company data sets.
# 75%  of work don on pasndas is data cleaning. now the most important thing for me is getting job  and learning from the experts in data analysis and also data scientists.  
 
#  ============================================ THE END! ============================================