# I’m going to study lists thoroughly. What do I need to understand?
# we will answer this question soon.
# so lets start todays lesson it's nice to start from skipping values from list("_" )

# Skipping values from list("_" )  when packing and unpacking.
teacher=['amir',19,'SWE','BI analyst',"ethiopia"]
name,_,_,_,country=teacher # to unpack and to trash unwanted values using '_'.
name,*_,country=teacher    # this is the easiest way to trash un wanted values. but there are still in list.

# # Exploring and analysing data vallues in list
numbers=[1,1,7,5,90.98,76,3.83]
print("max:",max(numbers))
print("min:",min(numbers))
print("sum:",sum(numbers))
print("lenght:",len(numbers))

print(f"all: {all(numbers)}")
print(all([1,1,0,"",None,False]))

print(any([1,1,0,"",None,False]))
print(any(numbers))

# To know index of the value.
print("index",numbers.index(3.83))        # try to remember find

# # Membership and identity check in list
print(3.83 in numbers)
print([1,7,3.83] in numbers)
print(8 not in numbers)
 
print([1,3,4,7] is [1,3,4,7])   # false bc we are not all about the value rather we are about the identity which is python mades to store these data avalues are different and that is why we got false.
print([1,3,4,7] ==[1,3,4,7])    # true bc the values are the same. 


# Udate list:change the data value in list 
# there are three ways to change values in list.
# 1 append: to add values at the end
matrix=[[1,3,4,7],
        [7,3.83],
        [1,1,0,"",None,False],
        [1,1,7,5,90.98]]


numbers.append("x")
numbers.append(3+4j)
matrix.append(34)        # we can add single value in nested list 
matrix.append([34,45])   #we can also add anothe list like this.
matrix[2].append(True)    # to add in index two wc is third row at the end.
print(matrix)
print()

# 2 Extend: to add multiple values at the end of the list
print(numbers.extend(['wow',"i like it",3.83]))   # don't use this way untill you became advanced bc it will confuse you.the value changed in abstract way and in the out put you will see None.
numbers.extend(['wow',"i like it",3.83])     # use exactly this.
print(numbers)
matrix.extend(['wow',"i like it",3.83])      # this is how exactly we can add multiple values at the end of the nested loop.
print(matrix)

# # 3 Insert: to add values any where in sing and matrix list
numbers.insert(2,56)
matrix.insert(3,54)        # to insert single values specifically where we want.
matrix.insert(2,[36,78,90])   # to insert multiple values specifically where we want. 
matrix.insert(0,['wow','python','what',"a programing  languge"])
matrix[2].insert(2,'python')
print(matrix)
print()
print(numbers)


# Clear items in ilist
# there are two possible ways to remove values out of list
# 1 remove by value     clear()to remove every thing and remove() to specify.

#numbers.clear()   # this will remove everything inside numbers.
numbers.remove(90.98)
#matrix.clear()  # to clear everything inside this nested list
#matrix[3].clear()
#matrix[2].remove("")


# matrix.clear()         #  to clear everything including the nested lists then we will hav[] only.
# for row in matrix:     # to clear every thing inside this nested or matrix list.
#    row.clear


# 2 Remove by Position  (pop())
numbers.pop()         # this will automatically remove the last value
numbers.pop(1)          # now we specify the index

matrix.pop()        # will remove the last row  
matrix.pop(2)            # to remove specific row by telling python which row we want to remove using pop + index no.

matrix[2].pop(-1)

