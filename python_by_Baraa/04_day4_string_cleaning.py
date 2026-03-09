
# string cleaning
# since 80% of company datasets are string which means texts and they have bad data quality 
# before we stsrt do something on them we have to clean it to get effective result from the datas

# space cleaning: this  is common task in real data sets the task is simple removing uncessary space 

name='  $ kerim'.lstrip().lstrip('$')    # it's some boring and biggner method. won't give the exact what we want.
print(name)      # this is how can clean left side of the value.

name='  $ kerim#'      # but this is advanced and easy way to remove every extra speces and Spe Char  s. with regardless of order when we pass parameter  like this ('$ ') or (' $') . but this function will accept only one argument
print(name.strip('# $')) 
name='  $ kerim#'.strip('# $')    
print(name)                     #the same result so this is another way print final result

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
print(user_srch==act_data)        # since i applied the concept strip from left and righ side(every uncessary values removed once). so we'll get true.

# advanced challenge
# clean this messy data 
# expected output: Kerim Reshid,Addis Ababa,Ethiopia

user_srch='% ###3Kerim Reshid,@ddis @baba,Ethiopia   -'.strip('#-% 3').replace('@','A')
print(user_srch)    # in the out put i will get kerim Reshid,Addis Ababa,Ethiopia 



# search functions  now we are gonna see checking string value using search.
text = "Data analysis with python".startswith('data')  
print(text)    # (false bc of case) this searching is used to check whether our string values starts as we want or not and in the out we will see True or False

stu_info='Kerim reshid,3rd year,SWE'
print(stu_info.endswith("SWE"))          # True  since, no matter to use it in print function and also to use single and double qouts interchangeably.

file='sample datas.csv'         
print(file.endswith('.csv'))      # True agian and it's important to check file type. 

stu_info='Kerim reshid,3rd year,SWE'
print('3rd' in stu_info)                 # true bc python searchs in the string value it gets then return True.     

city = "Addis Ababa is the capital of Ethiopia"
print(city.find('Ababa'))     # now here we won't see bool values bc it's related with indexing so it counts starting from zero then return index no.
 # and it's not about single letter it find the word Ababa when it get it return the first index no of this word.

# challenge to find exactly the removeal part index no  and slice(extract phone no with out country code)
phone='+241-979-73658'
print(phone.find('-'))    # we got 4 it means - is in the 4 index(5th position since indexing starts from 0)  the let me apply slicing then.

print(phone[5:])       # simply we can solve the problem like this.
print(phone[phone.find('-')+1:])  # same result but it's alittle more professional and advanced.

# validation  methods

text = "Kerim"
print(text.isalpha())
print(phone.isdecimal())
print(city.isnumeric())     # we can check like this  we will get True or False.




















































