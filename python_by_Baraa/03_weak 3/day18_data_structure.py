# what is data structure?
# data structure is advanced data types we can put data in group there are 4 built in data structures in pyhton
# # list[],tuple(),dictionary{},and set{}
# high light difference bn those data structure 

# list [store common data typs]                        empty list       [] and list()
# set{stores unique data value}                        empty set        set()
# dict{very fundamental for data scince}               empty dict       {} and dict()
# tuple(we can't update or change after once store.)   empty tuple      ()

# 1 list
# are widly used in python bc it allows to update store similar data values(duplicate)
# mixed=[1,7,True,'kerim',3.83,]    # this is how we can create list and in list we can store dfnt data types 
# # but how pyhton store it?  fist crate  object list then store each values uniqly by create another objects regarding to there daata type.
# print(type(mixed))
# print(mixed,'\n')

# cource=list("pyhton")  #to change normal str in to list format
# print(cource,'\n')
# numbers=list(range(7))
# print(numbers)
# print()
# # nested list or matrix.
# nested=[[1,2,7,'wow',3.83],
#        [74,'now','then','here after'],
#        [True,False,None,7]]
# print(nested)

# # accessing list
# # indexing(access or read one single item from normal or matrix list)
# print(numbers[3])    # bc the fun range also start from zero like indexes.
# print(cource[-4])    # in indexing if we use -ve nos then it will start from -1.

# print(nested[0][0])  # whenever you want to read or access the first item in nested or matrix list.
# print(nested[1])      # to get the second row.
# print(nested[2][-1])    # to get no 7 that appear in the third row and fourth column.

# # slicing (access or read multiple items from normal or matrix list)
# # slicing normal list
# print(numbers[:3])
# print(cource[3:])

# # slicing matrix list
# print(nested[1:3])   # to read specific rows in matrix
# col1 = [row[1] for row in nested]   # te read the second column in the matrix.
# print(col1)                # you have to practice more in this concept understanding how it works and  knowing is this possible way to access such type of data is enough in this stage. the other thing will be how much you dedicated to use AI to solve problems.


# # but the important question is how we can specifc ordered values for ex. to read now then from the matrix.
# print(nested[1][1:3])   # we did it i can access exacttly what i want.
# print(nested[0][2:5])


# packing and unpacking lists
employee=['kerim reshid',23,'BI analyst',"ethiopia"]
# name=employee[0]
# age=employee[1]
# roll=employee[2]
# country=employee[3]  #we can  assign specifically for what we want this is called unpacking. But it's boring and there is another simple way.

name,age,roll,country=employee

print(f"name:{name} age:{age} years old")

teacher=['amir',19,'BI analyst',"ethiopia"]
name,*details,country=teacher     # using astrix we can store detail informations then access all once but the formatt will be in list.
print(name,details)               # 













































































