gend=input("gender:")
age=int(input("age"))

if(gend=='M' and age>21):
    print("you are valid for marrige")
elif (gend=='F' and age>18):
    print("you are valid for marriage")
else:
    print("Invalid age")
