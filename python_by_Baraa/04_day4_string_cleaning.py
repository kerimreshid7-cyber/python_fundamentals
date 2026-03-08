
# string cleaning
# since 80% of company datas are string which means texts and they have bad data quality 
# before we doing something on them we have to clean it to get effective result fro the datas

# space cleaning: this  is common task in real data sets the task is simple removing uncessary space 

name='  $ kerim'.lstrip().strip('$')    # it's some boring and biggner method
print(name)      # this is how can clean left side of the value.
name='  $ kerim'.lstrip(' $')      # but this is advanced and easy way to remove every extra speces and Spe Char  s. with regardless of order when we pass argument(in 1 argument) like this ('$ ') or (' $') . but this function will accept only one argument
print(name)  
skill='front end,sql and data anlysis $####   '.rstrip('$# ')  # this is fantastic way to remove uncessary spaces and special characters 
print(skill)

dep='  # software engineering  '.strip().strip('#')     #(won't remove one extra space where before # ) this is how we can remove extra spaces and uncessary special characters.
print(dep)
dep='  # software engineering  '.strip().replace('#','')  # the out put is same code 1 python gonna do first change # by empty then remove right and left spces and it's easy we usually use this.
print(dep)
dep='  # software engineering  '.strip(' #')      # this will clean every thing and it's the modern way to clean. 
print(dep)

print(f'{{ohh cleaning is simple and very intersting with python}}')


# Challenge 1 — Clean messy usernames
# You receive usernames from a file. Many have spaces or unwanted symbols at the start or end.

usernames = [
"   Bilal   ",
"###Ahmed",
"Fatima###",
"   ##Yusuf##   "
]

# Task
# Create a new list where:
# All leading and trailing spaces are removed.
# All  characters from the left and right are removed.

new_usernames=[]
































































































