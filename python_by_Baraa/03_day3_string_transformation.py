
 # string  is the most fundamental data type in python bc in companies 80% of data are texts
 # so, we have to proccess analyse transform those datas. understanding string bhnd the sign is 
 # not an option.  that is why i am covering the video word by word.
   
# 3 transformation
    #   replace()

s_price="123,34"   
print(price.replace(",","."))    # so in the out put we will see the comma changed by dot.

Date="2026/03/07"
print(Date.replace("/","-"))     # slash will changed by minus.


s_price="123,34"   
print(price.replace(",",""))    # the out put will show us the comma changed by nothing.

s_price="123,34"   
print(price.replace(","," "))    # so in the out put we will see the comma changed by space.

s_price="123,34$"   
print(price.replace(",",".").replace("$",""))   # this is how  we can replace more than one value once.

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


















