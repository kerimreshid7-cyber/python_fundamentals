# today let me revise and do practical exercise 
# challenge to revise membership , logical oprators and identity oprators.
# 1 check if the user name is unkown and email is not empty and also the age is greater than or equal to 18


print("it's just for revision.")
user_name='@abd_kerim7'
email='ke@gmail.com'
age=18
print((email is not '' and email != '') and age >=18) 
#if we get true every thing is fine if it's false we should check what whappend and why   as we are data analyst.

# 2 check if the password is at least 8 characters long and does not contain space.
password=' 8745njf'        # it's look like full fill the condition but we got to emphise about space.
print(len(password)>=8 and ' 'not in password) 
# the out put show us false python is not lying us we trust it and find the problem when we use it in real life

# 3 check if a user's email is not empty. contains'@', and ends with '.com'
print(email != '' and '@' in email and email.endswith('.com'))
# exactly true we can prove it wow python

# 4 check if a user name is a string ,is not None and is longer than 5 characters.
user_name='kerim reshid'
print(isinstance(user_name,str) and user_name is not None and len(user_name) > 5)
# obviously true 

# 5 check if the user is either an admin or a moderator,and either they are not banned or they verfied their email.
user="kerim"
is_admin=False
is_moderator=True
is_banned=False
is_verified=True 


print((is_admin or is_moderator) and (is_banned or is_verified) )
# as I think it's better to do it by conditional statment (if)  bc it doesn't give me sence the true false here so, lets learn conditional statment. 


# introduction to conditional statment 
# now  we just enter to the cocepts in control flow code we will practice more from now on
# indentation in python is not option  it's syntax. 

# if condition it's easy to understand if the condition is true then go and excute unlesss skip it(or if we give another option using else or elif then python gonna jump to that)
#  rules: 1 if is necessary not optional like else and elif
#         2 in one conditional statment allowed   only one if
#         3 if always come first
#         4 it can stand alone.


# simple if statment : if the condition is True  then go and excute if nnot just skip it.

