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

max=0
for j in range(len(t)):
    if(t[i][1][0]>max):
        max=t[i][1][0]
print("Topper of the mathematics is:",t[i][0],"with marks: ",max)

max=0
for k in range(len(t)):
    if(t[k][1][1]>max):
        max=t[k][1][1]
print("Topper of the Physics:",t[k][0],"with marks:",max)

max=0
for l in range(len(t)):
    if(t[l][1][2]>max):
        max=t[l][1][2]
print("Topper of the Chemistry:",t[l][0],"with marks",max)

print(d)
