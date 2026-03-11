
 # string  is the most fundamental data type in python bc in companies 80% of data are texts
 # so, we have to proccess analyse transform those datas. understanding string bhnd the sign is 
 # not an option.  that is why i am covering the video word by word.
      
# 3 transformation
    #   replace()

s_price="123,34"   
print(s_price.replace(",","."))    # so in the out put we will see the comma changed by dot.

Date="2026/03/07"
print(Date.replace("/","-"))     # slash will changed by minus.


s_price="123,34"   
print(s_price.replace(",",""))    # the out put will show us the comma changed by nothing.

s_price="123,34"   
print(s_price.replace(","," "))    # so in the out put we will see the comma changed by space.

s_price="123,34$"   
print(s_price.replace(",",".").replace("$",""))   # this is how  we can replace more than one value once.

   # challenge in replace
phone_number="+49 (234) 345-834"
print(phone_number.replace("+","").replace(" ","").replace("(","").replace(")","").replace("-",""))


# join to merge diferent strings   and we usually use it to open file bc the folder and the file puts distinctly.
f_Name="kerim" 
l_name="reshid"
last_name=f_Name + " " + l_name    #we can simplly add the srtings like this.
print(last_name)

# real challenge for join
#  merge the folder and file and make it copy paste freindly to open the file.
folder="c:user/kerim/Desktop/date_function_practice2"
file="data.csv"  
print(folder + "/" + file)



    #   f string  modern and super easy way of format and build string
age=23
dep="SWE"
year="3rd"
# print("i am" + age + "i am studing" + dep)   this will return an error bc we caan't add int and str
# print("i am" + str(age) + "i am studing" + dep)   now problem solved  but it's some thing boaring that is why we need to use f string.

print(f"i am kerim reshid and i am {age} years old i am learnig at haramaya university {dep} field i am {year} year student.")
# using f (stands for format)  we can print any values regardless of data type.

print(f"2+3={2+3} any time bc mathimatics will never lie.") # so we can also do oprations usinf f string.
# print(f"{this is the future of BI analyst}")  this code will return error bc when ever we have to put values in side curly brace({}) . if we want there is another method
print(f"{{this is the future of BI analyst}}")  # using double curly brace we can print text.



# split method  this method is used to separate values by defining where we want to separate(crtical point).
# return as a list.

stamp='2026-03-07'
full_name='kerim reshid '

print(stamp.split("-"))       # we are spliting by telling exactly where we want to split.("-")
print(full_name.split(" "))   # we are spliting by telling exactly where we want to split.(" ")



# string repetition (*)

print("ha"*4)
print("#"*17)
print('_'*12)  # this is used to make such signs or any values stable.

print('ha'*7)

 
 
#  4 extraction

# indexing and slicing
# indexing to get single value from string value.
f_Name="kerim"
print(f_Name[0])    # since +ve indexing start from zero so this will give as only k
print(f_Name[3])    # this will give us exactly  i.
print(f_Name[-2])   # this will give us exactly  i again because -ve indexing start from -1.

#  slicing to get more than one value value from string value.

print(f_Name[0:3]) # starting from 0 (bc start will include) up to exactly 2 (bc end won't include) 
print(f_Name[:3])  # this is similar to the above we can ignor 0 if we start from the first.

print(f_Name[-4:-1]) # will give us eri   e=-4 and i=-2   bc -1(end) won't included.

# slicing with open end
print(f_Name[2:])   # exactly equal to (rim) since we don't define the ending point python gonna understand that we want up to end.
print(f_Name[-5:])   # exactly equal to (kerim )    sometimes this will make confusion bc it's looks like normal indexing but the difference is here we have (:).

# slicing with step
print(f_Name[-4:-1:2])   # new thing here we are commanding to jump 1 value. so it's = (ei)
numbers = [0,1,2,3,4,5,6,7,8,9]
print(numbers[::2])    # we didn't define starting and ending point here so python gonna understand we want 0-9(including 9) with step 2

