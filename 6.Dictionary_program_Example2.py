student={}
n=int(input("Enter the no of student in list: "))
for i in range(n):
    roll=int(input("Enter the roll no:"))
    name=input("Name of the student")
    mark=int(input("Enter the subject mark:"))
    student[roll]=[name,mark]

    l=list(student.values())
    
    max=0
for i in range(len(l)):
    if(l[i][1]>max):
        max=l[i][1]
print(max)

print(student)
