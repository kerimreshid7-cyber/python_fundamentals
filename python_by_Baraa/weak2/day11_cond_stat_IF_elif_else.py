
# today again i am commited to practice conditional (if) statments by doing some practical challenges.

# lets try to change the students grading system from manual into digital.
# challenge 1 take the grade from the user and tell grade he get

score=float(input("enter your score"))   #since we have defined to take float, if we input string or bool or complex pyhton will return error.
if score<= 100  and score>=90 :
    print('congra you got A')
elif score>=80 and score<90: 
    print('congra you got B')
elif score>=70 and score<80 : 
    print('you got B-')
elif score>=60 and score<70:
    print('you got C')
elif score<=50 and score>=40:
    print("sorry not for today. you got F")
elif score<=40 and score>=1:
    print('ohh sorry you got NG')
else:
    print("invalid input")  # about numbering only.

# i think this is boring. for sure i will modified it, when i got some practical experiance on coding.

# i have understand one thing new in if statment ti's nice the logic be the highest to lowest we call it clean logic.
# so now let me do this proble again.
stu_score=float(input('enter your score here'))
if score<0 or score>100:
    print('invalid input')
elif score>=90:
    print('congrates you got A')
else:
    print('invalid input')    #by the way i know about error handling from my back ground experiance but i just to follow the road map of the video.

# these two out codes will excute one after another by order.first come first served.



# if is mandatory,only one,must come first, and condition must be appeared. 
# elif optional, multiple times,come after if, and condition must be appeared.
# else optional only one,come at the end, and condition optional.















































































