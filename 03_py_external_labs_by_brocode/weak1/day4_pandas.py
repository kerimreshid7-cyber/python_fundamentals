
# hello how are you? you good? well lets dive in to todays lesson.
# today i am gonna start pandas

# pandas abbrivation for panel datas which is an external library built on top of numpy.
# so we can import, manipualte and export datas using pandas.  lets install and import pandas here.

import pandas as pd

print(pd.__version__)
print('====================================')
# we must differntiate the concepts of series and data fram. so lets see them one by one
# series = a pandas 1-dimentional labled array that can hold any data type
#          think of it like a single coumn in a spreadsheet (1-dim).

# to create Series in pandas
data_usage=[1.2, 0.8, 1.5, 2.1, 1.9, 0.7, 1.0, 1.3, 2.4, 1.8,
     0.9, 1.6, 2.0, 2.3, 1.1, 0.6, 1.4, 1.7, 2.5, 2.2,
     1.0, 0.8, 1.9, 2.6, 2.8, 1.2, 1.5, 2.0, 2.4, 3.0]

lables=[f"day{day}"for day in range(1,31)]
series=pd.Series(data_usage,index=lables)

#print(series)

# accesing specific data
print(series.loc["day2"])    # wow python   i love pyhton oooooohhh    it's realy amazing we can access like this "python for smart worker"
print(series.iloc[3])        # to access value using index.  so we'll see 2.1 in the out put.    so we can say it it's keyed and at the same time indexed.

# to update the series
series.loc["day25"]=3.83
print('=============== updated version of my series ==================')
print()
print(series)
 
# to filter in series
print(series[(series<3/2) | (series>1+1)])
print()

# data frame = is a tabular  data structure with rows and columns.(2dim)
# it is similar to an excel spreadsheet.

stu_data = {'name':['kerim','ebrahim','abduselam','ayub','sydo','sami'],
            'gpa':[3.83,3.77,3.7,3.6,3.5,3.8]
        }

indx=[f'stu{stu}' for stu in  range(1,7)]    # this is how we can give index our self using list comprehension and for loop and also i used f string.
df= pd.DataFrame(stu_data,index=indx)        #the way to create data fram is some thing similar with creating series. but the differece here is we can assign for multiple values for one key. so the keys is to be column name and the values are to be columns. 
print('=============this is the out put for my data frame==============')
print(df)

# accessing data frame
print(df.loc['stu4'])     # the out put is very clear and amazing no wonder to get this bc it's python. 
print('====to accese by index=====')
print(df.iloc[2])         

# adding new column
df['job']=['data analyst','AI developer','web app developer','merchant','It professional','AI developer']

print(df)


# adding new row
# new_row=pd.DataFrame([{'name':'sadiq','gpa':3.75,'job':'web app developer'}])
# df=pd.concat([df,new_row])

# print(df)       # the new row concatinated but  the problem is the index name doesnnit much so lets fix it.
 

# new_row=pd.DataFrame([{'name':'sadiq','gpa':3.75,'job':'web app developer'}],index=['stu7'])

# to add multiple rows

new_row=pd.DataFrame([{'name':'sadiq','gpa':3.75,'job':'web app developer'},
                     {'name':'kyredin','gpa':3.6,'job':'GIS professional'}],
                   index=['stu7','stu8'])


df=pd.concat([df,new_row])

print('=========here is the updated Data frame====================','\n',df)


# but the question is how can we update Data frame?

