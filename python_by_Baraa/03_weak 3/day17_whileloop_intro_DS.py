
# hello how are you today i am gonna cover while loop and introduction to data structure
# while loop is used to repeate a block of code as long as a condition is true

# lets see it with example like counter.
# counter=1                   #  this is initialization
# while counter<=5:            # this is condition.   if it is true go and do some thing if is false exit from loop.
#     print("no",counter)
#     counter+=1         #  this is called update.    what if we don't give this increment? the loop never stop bc 1<5 is always true.

# print()


answer=""
# print('customer questionary')
# while answer!='yes':
#     answer=input('do you agree? (yes/no)')
#     print("why? cause we offer you a lot of benefits")
#     if answer=='yes':
#         break
# print("thank you!")   

# print()

# # while True: it is some slightly different from normal while
# # it is more power full but its risky.
# print('special customers questionary')
# while True:
#     answer=input('do you agree? (yes/no)')
#     if answer=='yes':
#        break
# print("thank you!")   

# print()

# the differnce here is our condition is always true so there is no need to check the con but the risk is it'll be infinite unless we put break with if statment so if thee statment we put is true the loop will end(exit).

# so while looo is finite                       but  while True is infinite and its risky
#  we know when the loop will exit                while Trueis more power full.
#    more readeble                                  more felxible
#    it's counter ,limited retries                  open ended waiting for d= DB,api and stream.  


# challenge 1      ask the user while it get yes    but restrict the attempts by 3
# print("questionary with limit 3")

print("questionary with limit 3")
answer=""
attempt=1
while answer!="yes":
    answer=input("do you agree? (yes/no)")
    if answer!="yes" and attempt==3:
        print("you are out of the chance")
        break
    elif answer=="yes":
        print("thank you! we are in the same page")
        break
    else:
        print("why? because we offer you a lot of things")
    attempt+=1


































































