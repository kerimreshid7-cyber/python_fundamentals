# how are you? today i am gonna cover for loop with reallife practical challenges.

# challenge 1
# print 7 times table from 1 upto 10 using for loop
for num in range(10):      #will start from 0 but exclude 10
    print(f"7*{num}={7*num}")
for num in range(1,11):             # will start or include 1 but exclude 11
    print("7*",num,"=",7*num)
print()  #just because you know what i mean to  create gab.

# challenge 2 print left aligned pyramid of stars with 6 rows
for i in range(1,7):
    print("*"*i)



# so lets continue todays new ideas or topics.
# loop control statments  we will see three of them
# break,continue,and pass        so we are about to see the advancd for loop.

# break statment  is used to stop the itration when the condition is true if the condition is false then print and again return to the first step so the logic is like that.
names=['ker','ebr','abd','syd',"",'ayub','sam']
for name in names:
    if name=="":
        print('empty value detected!')
        break
    print(name)
print()
# what if the break statment missed lets see what will gonna happen
for name in names:
    if name=="":
        print('empty value detected!')
    print(name)    # here i get all names in the out put but after empty value detected! the order is unexpected for me it should be i need to learn some thing new. 
print()


# continue is used to continue the loop  after even the 2nd condition is true it's opposite to even 
for name in names:
    if name=='':
        print('empty value detected!')
        continue
    print(name)


























































































