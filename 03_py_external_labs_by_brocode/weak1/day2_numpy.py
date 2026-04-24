# hello how are you today i am gonna cover some concepts in numpy 

#scalar arithmetic
import numpy as np
array_2d=np.array([[3.83,3.34,7],
                   [3.79,2,5.45],
                   [3.65,2,3.342]])

wow_numpy=array_2d+2
print(wow_numpy)

print(array_2d*7)
print(array_2d-30)
print()

print(array_2d/3)
print()
print(array_2d**2)
print(array_2d%2)
print()

print(array_2d//4)



# vectorized math funcs
print(np.sqrt(array_2d))
print(np.round(array_2d))
print()
print(np.round(array_2d,1))
print(np.floor(array_2d))
print()

print(np.ceil(array_2d))
print(np.pi)

# exercise   find the area of circle for all list(radius given in the list)
radius=np.array([2,4,6])
area=np.pi * radius**2

print(area)


# element-wise arihtmetic
array_2d2=np.array([[4.3,3.34,5.4],
                   [2.56,3.56,5.45],
                   [3.65,2,3.342]])

print(array_2d-array_2d2)
print(array_2d2+array_2d2)

print()
print(array_2d2*array_2d)    # we can apply eveything i think with differnt arrays.


# comparision oprators
stu_scores=np.array([91,34,45,76,100,80])

print(stu_scores==100)     # we will get boool value in the out put
print(f'is pass?{stu_scores>50}')

# or we can do by another advanced way
for score in stu_scores:
    print(f'score{score}-> is pass?{score>50}')

# lets update
stu_scores[stu_scores<60]=0
print(stu_scores)


# brodcasting
array1=np.array([[1,2,3,4]])
array2=np.array([[1],[3],[5],[7]])

print(array1.shape)
print(array2.shape)

print(array1*array2)
print()
# exercise:  make multiple table
multiplicand=np.array([1,2,3,4,5,6,7,8,9])
multiplier=np.array([[1],[2],[3],[4],[5],[6],[7],[8],[9]])

products=multiplicand*multiplier
print('==========multiple table==========')
print(products)












