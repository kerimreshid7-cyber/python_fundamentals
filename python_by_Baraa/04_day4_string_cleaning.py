
# string cleaning
# since 80% of company datas are string which means texts and they have bad data quality 
# before we doing something on them we have to clean it to get effective result fro the datas

# space cleaning: this  is common task in real data sets the task is simple removing uncessary space 

name='  $ kerim'.lstrip().strip('$')    # it's some boring and biggner method. won't give the exact what we want.
print(name)      # this is how can clean left side of the value.
name='  $ kerim#'.strip('# $')      # but this is advanced and easy way to remove every extra speces and Spe Char  s. with regardless of order when we pass argument(in 1 argument) like this ('$ ') or (' $') . but this function will accept only one argument
print(name)  
skill='front end,sql and data anlysis $####   '.rstrip('$# ')  # this is fantastic way to remove uncessary spaces and special characters 
print(skill)




dep='  # software engineering  '.strip().strip('#')     #(won't remove one extra space where before # ) this is how we can remove extra spaces and uncessary special characters.
print(dep)
dep='  # software engineering  '.strip().replace('#','')  # the out put is same code 1 python gonna do first change # by empty then remove right and left spces and it's easy we usually use this.
print(dep)
cle_dep='  # software engineering  '.strip(' #')      # this will clean every thing and it's the modern way to clean. 
dep='  # software engineering  '

is_clean=cle_dep==dep
print(f'no of extra characters={len(dep)-len(cle_dep)}')
print('is my data is clean?',is_clean)

print(f'{{ohh cleaning is simple and very intersting with python}}')



# case cleaning  lowwer and upper methods 
#  we use these most of the time in searching tasks bc when 
# users search some thing mostly with typo from the original value so to fix such type of probles use
course='python'.upper()
name='KERIM reshid'.upper()    # THESE two code will made the latters capital and if it's already capital it will ignore and displlay it self.
user_srch='Kerim'


act_data='keriM'   
print(user_srch==act_data)     # we will get false since pyhton is case sensetive we won't get what we looking for.

user_srch='% Kerim  '.lower()
act_data='#$$ keriM %'.lower()
print(user_srch==act_data)      #  stil it's false bc of extra space 


user_srch='% 3Kerim  '.lower().strip('% 3')
act_data='#$$ (keriM %'.lower().strip('(%#$ ')
print(user_srch==act_data)        # since i applied the concept strip from left and righ side(evry uncessary values removed once). so we'll get true.

# advanced challenge
# clean this messy data 
# expected output: Kerim Reshid,Addis Ababa,ethiopia

user_srch='% ###3Kerim Reshid,@ddis @baba,Ethiopia   -'.lower().strip('#-% 3').replace('@','A')
print(user_srch)    # in the out put i will get kerim reshid,Addis Ababa,ethiopia but still ethiopia is not match to the expected output  I think to fix this i need to learn more.































































