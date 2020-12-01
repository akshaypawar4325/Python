d={}

n=int(input("How many times you want to repeat:"))
for i in range(n):
      roll=int(input("Enter the roll no:"))
      name=input("Enter the name:")
      math=int(input("Mathematics marks: "))
      physics=int(input("Physics mark:"))
      chemistry=int(input("Chemistry marks:"))
      l=[math,physics,chemistry]
      d[roll]=[name,l]

t=list(d.values())
print(t)
option=0
while(option!=5):
    
    print("1.Math topper")
    print("2.Physics topper")
    print("3.Chemistry topper")
    option=int(input("Enter no for subject topper:"))
    
    if(option==1):
        max=0
        name=""
        for i in range(len(t)):
            if(max<t[i][1][0]):
                max=t[i][1][0]
                name=t[i][0]
        print("math topper is",name,"with marks:",max)
    elif(option==2):
        max=0
        name=''
        for j in range(len(t)):
            if(max<t[j][1][1]):
                max=t[j][1][1]
                name=t[j][0]
        print("math topper is",name,"with marks:",max)
    elif(option==3):
        max=0
        name=''
        for k in range(len(t)):
            if(max<t[k][1][2]):
                max=t[k][1][2]
                name=t[k][0]
        print("math topper is",name,"with marks:",max)
    elif(option==4):
        print(d)
    elif(option==5):
         print("exit")
