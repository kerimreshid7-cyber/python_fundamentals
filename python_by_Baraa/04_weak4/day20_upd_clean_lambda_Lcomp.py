
# update 
numbers=[1,1,7,5,90.98,76,3.83]

matrix=[[1,3,4,7],
        [7,3.83],
        [1,1,0,"",None,False],
        [1,1,7,5,90.98]]

numbers[3]=9
matrix[2][4]=True
matrix[-1]=[1,1,7,5]
print(matrix)

# sorting and composition
numbers.sort(reverse=True)
new_matrix=sorted(matrix,reverse=True)     # it's different from sort bc the original list will not be removed.
matrix.sort()    # when  we want sort nested list python will check the first item and sort according to that result if the first item is the same then check the second item like that...
matrix[-2].sort(reverse=True)   # to order specific row in descending.
numbers.reverse()      # or ::-1
new_numbers=reversed(numbers)   # it won't remove the orignal list like sorted.

no1=[1,1,7,5]
no2= [7,3.83]
sum_no=no1+no2   # or no2 is extended after no1
print(sum_no)     
sum_no=no1.extend(no2)    # these two methods have the same result.

# copy the list   it's important to put data if something happened and we need to get the orignal data and also to compare the analysed data.
matrix_copy=matrix    # python won't make another list object it will store the objecte that is created for the original list.
matrix_copy.extend(["there was match yesteday. But,i didn't see it.",'so i gotto see highlight.'])
print(matrix_copy)      # when ever we add new item in copy the original list also will be affected.
print(matrix)        # so to fix this what we have to do?

matrix_copy_independent=matrix_copy.copy       # so now we can easily analyse the orignal or copy list. no more affecting the copy while anlysing the orignal one and vice versa.
# i think it's clear and easy right? lets continue.




















































