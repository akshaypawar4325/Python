D1={1:['MANDAR',{'HINDI':56,'ENG':70}]}
print(D1)
d2=D1[1][1]
print(d2)
marks=[]
for key in d2:
    marks.append(d2[key])

print(marks)
highest=max(marks)
print(highest)
