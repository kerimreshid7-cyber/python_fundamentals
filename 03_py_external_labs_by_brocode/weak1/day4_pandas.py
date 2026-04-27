
# hello how are you? you good? well lets dive in todays lesson.
# today i will start pandas

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
print(series.iloc[3])        # to access value using index.  so we'll see 2.1 in the out put.

# to update the series
series.loc["day25"]=3.83
print('=============== updated version of my series ==================')
print()
print(series)
 
# to filter in series
print(series[(series<3/2) | (series>1+1)])


# data frame = is a tabular  data structure with rows and columns.(2dim)
# it is similar to an excel spreadsheet.

stu_data = {'name':['kerim','ebrahim','abduselam'],
        'gpa':[3.83,3.77,3.7],
        }

indx=[f'stu{stu}' for stu in  range(1,4)]
df= pd.DataFrame(stu_data,index=indx)
print(df)








































