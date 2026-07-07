
# hello how are you today i am gonna cover evry thing remaining in the video.

# aggregate functions are functions to summerize the values inside array.

import numpy as np

sales = np.array([
    [125, 150, 100, 170, 130],  #week1
    [147, 167, 110, 180, 150],  #week2
    [130, 170, 123, 160, 141],  #week3
    [150, 187, 130, 191, 160]   #week4
])
print(np.sum(sales))
print('the total sale is ',np.sum(sales))
print('the mean of the sales',np.mean(sales))

print(np.var(sales)) 
print(np.std(sales))    #is the squre root of variance
print()
print(np.max(sales))
print(np.min(sales))
print(np.argmax(sales))    # to get the index no of maximum value.
print(np.argmin(sales))


# to aggregate specific axis
print('to add by column',np.sum(sales,axis=0))    #to add by column so python will summerize and give immidiatly.
print()
print("to add by row",np.sum(sales,axis=1))


# filtering

high_sales=sales[sales>=150]
print('low sales',sales[sales<130])
 
normal_sales=sales[(sales>=130) & (sales<=180)]  #we can't use "and" in array so instede we use '&'
not_normal_sales=sales[(sales<130)|(sales<180)]  # this is how we can use 'or' in num py.

print('even sales',sales[sales%2==0])
print('odd sales',sales[sales%2==1])

# but all the out puts here won't keep the orignal shape so this is when exactly we need 'where' 

# Where
higher_sales=np.where(sales>160,sales,'low sale')    #first we filter then we command to take the original array then third we have to replace the filterd out(uncessary datas) by some thing else.
print(higher_sales)
print(np.where(sales>160,sales,'low sale'))
print(np.where((sales>160) & (sales<240),sales,'out of budget'))
# random number generation in numpy
print('==============random number generating========')
ran_num_gen=np.random.default_rng()
print(ran_num_gen)     #i got Generator(PCG64) in the out put I think there is no need to master this now. i mean in this lable. 
print(ran_num_gen.integers(low=2,high=200))    # if we don't put integers then python will generate randomm numbers bn 0 & 1  so i think we can't decide the boundaries.
print(ran_num_gen.integers(low=1,high=100,size=3))     # it's similar with random.randint(in the python basics) #we'll get 3 random nums.   
print(ran_num_gen.integers(low=7,high=300,size=(3,4)))    #so wi'll get 3 rows and 4 columns.
print()
# by the way in numpy random numbers are not random they follow sequence so we can decide this sequence using 'seed'.

ran_num=np.random.default_rng(seed=42)
print(ran_num.integers(3,75,size=(2,3)))
print('=============')
ran_num2=np.random.default_rng(seed=100)
print(ran_num2.integers(30,70,(1,3)))   # i don't understand well about seed 
#                                          #but it's enogh in this stage  but i relized one thing new that there is no need to write like(low=,high,size)
print()
# generating random numbers using 'uniform'. 
ran_num_global2=np.random.uniform()
print("to get random nums bn 0 and 1 here   ",ran_num_global2)
ran_num_global=np.random.uniform(low=1,high=235,size=(2,3))       # it's similar with random.random(in the python basics)  but the difference is we can generate floats even out fo 0 &1 by deciding like this.
print(ran_num_global)
# in summary
# default_rng is the modern, controlled way  can generate float and int
# uniform is the quick old-style way         can generate only float.


# so now lets ingrate random with the array
ran_gen_stu=np.random.default_rng()
students = np.array(["Ali", "Sara", "John", "Mona", "David", "Liya"])
print(students)
print('=====random students out of students=====')

# shuffle
ran_gen_stu.shuffle(students)
print(students)

# choice
ran_choice=ran_gen_stu.choice(students)
print("the choice for today==",ran_choice)

ran_choice=ran_gen_stu.choice(students,3)
print("the choices for today==",ran_choice)

an_choice=ran_gen_stu.choice(students,(2,3))
print("the choices for today==",ran_choice)
