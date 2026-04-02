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


# 1 break statment  is used to stop the loop(itration) when the condition is true if the condition is false then print and again return to the first step so the logic is like that.
for name in names:
    if name=="":
        print('empty value detected!')
        break  # we told python to stop the loop using break.
    print(name)
print()



# 2 continue is used to skip one step(thathe condition become true) but continue the loop.(skip this but continue the loop.)
for name in names:
    if name=='':
        print('empty value detected!')
        continue  # which mean if name=='' then print empty value detected! and then skip this step(empty str) and continue the loop. so we won't get the blank line bc of continue.
    print(name)

print()
# we use continue to skip bad or empty data but to continue the loop.



# 3 pass used to command python "do nothing for now" 
tasks = ["Clean room", "Do homework", "Call friend"]
for task in tasks:
    if task=="Do homework":
        pass   # we are instracting pyhton to do nothing if task=Do homework so it'll gonna jump this task.  pass with else may make you confused with continue so take care of that.
    else:
        print(task)
  
print()

# another ex.
sales=[234,324,63433,"",7363,837]
for sale in sales:
    if sales=="":
        print("didn't find sale here")
        pass    # i realized when we should use pass with out else. to create space holder then may be when we get convinient time we will fix it so using pass.
    print(sale)

print()

# challenge 1
# print only working days (skip weakends) out of days
working_days=['mon','tue','sun','wed','fri','sat','thu']
weakend=['sat','sun']

for day in working_days:
    if day in weakend:
        print("there was no work on that day")
        continue
    print(day)

print()


# challenge 2
# scan email to block un safe data from entering your system.
emails = [
    "samir21@gmail.com",
    "hana.kebede@yahoo.com",
    "abel.tech2024@outlook.com",
    "drop table users;"      # one way the hacker may use to distroy our data base or access and steal important info. which is called sql injection.
    "selamwork12@gmail.com"
]

# for email in emails:
#     if ";" in email:
#         print('here there is sql injection')
#         break
#     print(email)



# for else
for email in emails:
    if ";" in email:
        print("here there is sql injection")
        
else:
    print("end")





































































