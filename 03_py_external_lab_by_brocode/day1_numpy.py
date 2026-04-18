


# list vs array
matrix=[[1,3,4,7],
        [7,3.83],
        [1,1,0,"",None,False],
        [1,1,7,5,90.98]]

my_list=matrix*3   #this code will make the list to appear 3 times it self not multilpying the value.

print(my_list)

# this is where exaclty we need array so to use array in pyhton we have to import the external library called numpy.

import numpy as np
array_0d=np.array('ohh array')          #it's 0 dimentional array

array_1d=np.array(['kerim',3.18,3,'wow'])    #it's 1 dimentional array

array_2d=np.array([['kerim',3.83,3,'wow'],['ebrahim',3.79,2,'wow']])


array_3d = np.array([
    [
        ['kerim',3.83,3,'wow'],
        ['ebrahim',3.79,3,'wow'],
        ['abduselam',3.7,2,'wow']
    ],
    [
        ['kerim',3.83,3,'wow'],
        ['ebrahim',3.79,3,'wow'],
        ['abduselam',3.7,2,'wow']
    ],
    [
        ['kerim',3.83,3,'wow'],
        ['ebrahim',3.79,3,'wow'],
        ['abduselam',3.7,2,'wow']
    ]
])


print(array_3d.ndim)












