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
print()


# so lets continue todays new ideas or topics.
# loop control statments  we will see three of them
# break,continue,and pass        so we are about to see the advancd for loop.

names=['ker','ebr','abd','syd',"",'ayub','sam']

for name in names:
    if name=="":
        print('empty value detected!')
    print(name)   # we didn't tell python what it should do next so by default it'll continue the loop and it'll print the empty space also(blank line)and then the remaining two names.

print()


# break statment  is used to stop the itration when the condition is true if the condition is false then print and again return to the first step so the logic is like that.
for name in names:
    if name=="":
        print('empty value detected!')
        break  # we told python to stop the loop using break.
    print(name)
print()



# continue is used to continue the loop  after even the 2nd condition is true it's opposite to even 
for name in names:
    if name=='':
        print('empty value detected!')
        continue  # which mean if name=='' then print empty value detected! and then skip this step(empty str) and continue the loop. so we won't get the blank line bc of continue.
    print(name)

print()


# pass used to command python "do nothing for now" 
tasks = ["Clean room", "Do homework", "Call friend"]
for task in tasks:
    if task=="Do homework":
        pass   # we are instracting pyhton to do nothing if task=Do homework so it'll gonna jump this task. 
    else:
        print(task)






















































































