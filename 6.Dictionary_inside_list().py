d={1:["akshay",{"math":25,"phy":65,"che":58}],
2:["ajay",{"math":45,"phy":54,"che":68}],
3:["rahul",{"math":54,"phy":54,"che":65}]}

n=input("enter subject: ")
max=0
for val in d.values():
    if(max<val[1][n]):
        max=val[1][n]
print(max)
