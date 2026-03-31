# hello, how are you today, so today i will continue coparision,membership,identity and logical oprators  
# 1 comparision oprators(<,>,==,!=,<=,>=)
print(24*3+34-4/4+54-63 == 4/4+54-63-24*3+34)      #it's obvious its false bc they are not equal.
print('a'<'b')     # we can compaire str(alaphabets) like this a is 1st and b is 2nd  python copare the string alphabeticaly any time the privious letter is less(like 1 < 2) so our result is true.
print('A'<'b')     # again true even if one capital and other small letter python compare them alphabetically 
print('a'>'A')     # in python capital letters less than small one(which means they come first)  when we compare to  their small one like 'a'>'A'  or 'A'<'a' true
print("a"=="A")    # false the are absolutly differnt in python python is very case sensetive.
print('kerim'>'')  #  true bc of the length of the string
print('kerim' != "kerim")  # it's false bc we say they are not equal while they are equal we can realize that there is priority bn '' and "" .
print("Kerim"<='kerim')     # true bc capital less than small in python wc means capital letters comes first in python alphabet orders 
print(4<23<45)       # true bc everything here is true
print(1>4<6<7)      #  false bc to be true everyhting must be true
#  any time the default result we expect is true i see this most studies and in python also similar

#  simple challenge
# check whether the students age is between 18 and 25
a_age=50
b_age=25 
print(18<=a_age<=25)      # it will false 
print(18<=b_age<=25)       # it will true


# logical oprators (and,or,not) used to combine boolians to build logic or rules.

print(1>4<6<7 and 4<23<45)    # false bc to be true all conditions must be true here we  have one false condition
print("Kerim"<='kerim' or 'kerim'<'' or 3!=4)  #true bc in 'or' logic if we have one true value the that satisfys the condition to be true.

#are the two students get permission to enter (the criteria is they must be bn 18 and 30)  
print(18<=a_age<=25 and 18<=b_age<=25)    # we got false that means i's not allowed to enter both of them

# one of the two students get permission to enter (the criteria is they must be bn 18 and 30)
print(18<=a_age<=25 or 18<=b_age<=25)      # we got true so one the two can enter.

# lets check the system is under pressure or not(the criteria is atleast one part is above 90 to say under pressure)
cpu_usage=75
memory_usage=95
battery_usage=90

# print("is the system is under pressure?",cpu_usage>90 or memory_usage>90 or battery_usage>90)
# # we got true so, we can explore that the system is under pressure right noe bc of memory_usage is above 90.

print(not 3!=5)       # not is negation used to change the result to it's opposite.
print(not cpu_usage>90 or battery_usage>90)  # we got true bc not changed the actual value(false)
print(not not cpu_usage>90 or battery_usage>90) # false

print(not False)
print(not bool())
print(not bool(0))    # these three are will get true bc of not  while they ware false.

print(not True)
print(not bool(123))
print(not bool("2y346"))  # these three are will get false bc of not  while they ware true.

# control excution order
print(cpu_usage>90 or battery_usage>90 and memory_usage>90)
# false 'and' oprator has higher priority than or oprator so python will excute battery_usage>90 and memory_usage>90 1st got false  then cpu_usage>90 or false(got bc of and ) finally we got false bc false or false is false.
print((cpu_usage>90 or battery_usage>90) and memory_usage>90)
# false again but the difference is now the 'parentesis' has higher priority than 'and'
# priority step : comarision < > >= <= == !=
# not then and then or 

# allow to access oonly the user is logged in or guest 
# must not be baneded. 
is_logged_in=True
is_guest=False
is_banned=True 
print((is_logged_in or is_guest) and not is_banned)
#we  false so the customer is not allowe to acces our services bc of he bannded even though he satisfy is_logged_in and is_guest.
# to chooese the order we got to see the question proprly.
# what if we do it with out parentesis guess what will gonna happen
print(is_logged_in or is_guest and not is_banned)
# true bc of the default priority is given to 'and'  so it change the result so we should take care of picing the logic especcialy the order. 
# we got incorrect result bc of priority usage.



# membership(in,not in)  to check something is inside list,single str value and array and so on 
s_list=['kerim','ebrahim','abduselam','sydo','ayub','sami']
print('ebrahim' in s_list)       #true 
print('ayub' not in s_list)       #false bc ayub is there in the list but, we said not in
print('k' in s_list)               # false why? bc,  In the list to be member must put in quots we have k but we have no 'k' 
stu_name='kerim'
print("k" in stu_name)       #true  this is differnt out of list(multiple value data type)

#identity oprator
a=5
b=5
print(a==b)               # True bc we are comparing the values here not the variable id
print(a is b)             # true ohhh why? we are comparing the variable(id) not the value so how they are simillar
                           # bc python will make one id for simple similar values

s_list=['kerim','ebrahim','abduselam','sydo','ayub','sami']
t_list=['kerim','ebrahim','abduselam','sydo','ayub','sami']
print(s_list==t_list)         # true when comparing the value the have same values
print(s_list is t_list)       # false bc the have different variable id yaah python treate this as compex data so created differnt is then when we compare the id using is we will get false.
 

# challenge make sure the email exist and not empty.

s_email=''
print(s_email is not None and s_email!= '')      # we will get false so  we can  easily reailize something wrong in user email. 


# revision challenges
# 1. Identity check (same object vs same value)
a = [1,2]
b = [1,2]
print(a == b)   # True   we are comparing the values
print(a is b)   # False   we are comparing the variable it self or the ID of the variable.

# 2. Check if ID is numeric
id = 3476
print("Valid ID" if id.isdigit() else "Invalid ID")

#3 check membership
region = input("Region: ").lower()
print("Addis" if "addis" in region else "Other")

# 4. Profit calculation
r = float(input("Revenue: "))
c = float(input("Cost: "))
print("Profit:", r - c) 

# 5. Validate age range
age = int(input("Age: "))
print("Valid" if 0 <= age <= 120 else "Invalid")

# 6. Membership check
city = input("City: ").lower()
print(city in ["addis", "adama"])


















