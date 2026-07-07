# after long time i just back with new concepts inline if and case match. so lets pick up the journey. 
# inline IF(ternary) is writing if statments in one line there is some dfnce out normal if statment. it has different rules the way to type
# let me list the rules   1, if comes first as usuall then give condition
#                         2, there is no elif here (not permible)
#                         3, else is not an option rather it's mandatory.
#                         4,  merge the code with print
# we use it for simple tasks that needed simple logic.

# Challenge 1 — Even or Odd
# Write one line that prints "Even" if 17 is even, otherwise "Odd".
no=17
print("even" if no%2==0 else "Odd")
# it's super easy now lets try what if the callenge need to use elif as we know in not allowed to use elif in ternary. lets go together.

# Challenge 2 — Even,odd or nither
# Write one line that prints "Even" if 17 is even, "odd" if a number is odd otherwise "nither".

print("invalid" if not isinstance(no,int)else "even" if no%2==1 else "odd" if no%2==1 else "nither")

# match case: in python it works as if statment but it's simple and easy some times it's treate as simpler form of if statment.
# challenge 3  change the contry names into abbrivation
country="ethiopia"

if country=="ethiopia":
    print("eth")
elif country=='united areb emariate':
    print("UAE")
else:
    print("unknown country")

# lets do it with simpler form using match case
 
m_country=str(input("enter country name"))
match m_country:
    case "ethiopia":
        print('eth')
    case "united areb emariates":
        print("uae")
    case _:
        print("unknown country")
    


