d={1:"hello",2:"world",3:"hi",4:"moon"}
a=d.keys()
c=d.values()
print("keys: ",a)
print("values: ",c)
#syntax:dictionary[key]=value
#==========================
'''
#Add the key and values in the dictionary
d={}
d[1]="python"
print(d)
'''
#==================================
'''
#Remove the element from dictionary
d={1:"Python",2:"data"}
a=d.pop(1)
print(a)
print(d)
'''
#=================================
'''
#Example
d={}
n=int(input("Enter how many number add"))
for i in range(n):
    a=int(input("Enter the key:"))
    b=input("Enter the value:")

    d[a]=b
print(d)
'''
