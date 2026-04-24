
# hello how are you today i am gonna start numpy(numerical pyhton) which makes pyhton fast. "with out numpy python is slow." brocode said. i am learning by bro code video. he is one of the most influencer in coding.
#and, I will cover every thing i need to to know in the video also i will read some documentations for future. but the most important thing is practice practic and practice.


# here we go
# list vs array
matrix=[[1,3,4,7],
        [7,3.83],
        [1,1,0,"",None,False],
        [1,1,7,5,90.98]]

my_list=matrix*3   #this code will make the list to appear 3 times it self not multilpying the value.

print(my_list)

# this is where exaclty we need array so to use array in pyhton we have to install and import the external library called numpy.

import numpy as np
array_0d=np.array('ohh array')          #it's 0 dimentional array

array_1d=np.array(['kerim',3.18,3,'wow'])    #it's 1 dimentional array

array_2d=np.array([[3.83,3,7],
                   [3.79,2,5],
                   [3.65,2,3]])   #array won't store different data type unlike list what it gonna do is like it will choose the safe data type to store every thing then it'll treate all values as one data type. This process is called type promotion (upcasting).

array_3d = np.array([
    [
        ['kerim',3.83,3,'wow'],
        ['ebrahim',3.79,3,'wow'],
        ['abduselam',3.7,2,'wow']
    ],
    [
        ['chala',3.83,3,'mine'],
        ['bruk',3.79,3,'yours'],
        ['mame',3.7,2,'our']
    ],
    [
        ['jbo',3.83,3,'theirs'],
        ['wawa',3.79,3,'his'],
        ['arebu',3.7,2,'her']
    ]
])

print(array_0d.ndim)

print(array_1d.ndim)

print(array_2d.ndim)

print(array_3d.ndim)

print()
# so now we can easily applie mathimathical oprations like addition and multiplication on array bc we have imoprted numpy. and python with out nump is slow how ever with numpy it's fast.

pro_array_2d=array_2d*3
print(pro_array_2d)

# array indexing and slicing
# indexing
print(pro_array_2d[-1][1])
print(array_3d[2][2][3])     # this is how we can acces specific value from  3d arary using chain indexing
print()

# slicing
print(array_2d[::2])
print(array_2d[::-1])
print()
print(array_2d[::-2])  # to print reverse and to jump step by two.    


print(array_2d[:,1])
print(array_2d[1:3,1:3])   # this how we can easily access the specific row and specific column using this power full library.
print()
print(array_2d[:,0:2])
print()

print(array_2d[0:1,:])

print(array_2d[1:3,1:3])
print(array_2d.dtype)

woo=np.array([[3,3,7],
              [3,2,5],
              [3,2,3],
              ['wow array','array loves rectangle','if i miss even one value python return an error']])

print(woo.dtype)
print(woo[3:,1:])