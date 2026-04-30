# hello how are you today i am gonna cover filtering and aggregation in pandas.
# the logic is not new for me so i have to focus on the syntax and then directly jump to real project practice.
import pandas as pd

df=pd.read_csv('full_order_analysis_project/data/orders.csv',index_col='id')

high_sale=df[df['price']>3000]

print(df[df['name']=='Ali Hassan'])
print('===============ohh python===========')
print(df[df['discount']==False])     # in  pandas False mean only zero not  empty string,or None unlike python truthness

wonderfull_sale=df[(df['price']>3000) | (df['discount']==False)]
print('=============wonderfull job==========')
print(wonderfull_sale)



# aggregate function is used to summerize so taht we reduse teh set of values into asingle summery value. 
# we ususally used with group by function.

print(df.mean(numeric_only=True))   # we can summerize once like this.
print('============amazing aggreation===============')

print(df.sum(numeric_only=True))

print(df.max(numeric_only=True))

print(df.count())      # we will get every items counted so in this case string values will also be affected.
# this is how we can aggregate  the whole data frame.

# so now lets see how we can aggregate single column

print(df['name'].count())
print(df['discount'].max())
print('=========this is how can aggrgate specific multiple columns===========')
print(df[['price','discount']].count())

# aggrgation with single group by

group=df.groupby('payment_method')
print(group['discount'].max().to_frame(name='max_discount'))

print(df.groupby('payment_method'))
print(list(df.columns))

print(df.groupby('category'))

# multiple group by
print(df.groupby(['payment_method','category'])['discount'].sum())    # i have to practice more here bc it's just like title there are so many concepts bhind this.

#the next is aggregation with group by ........


# aggrgation with group by