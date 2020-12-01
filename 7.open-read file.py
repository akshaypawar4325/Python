#read()
f=open("app.txt","r")
s=f.read()
print(s)
f.seek(0)
a=f.read()
print(a)
#===============================
'''
#readline()
f=open("app.txt","r")
s=f.readline()
print(s)
'''

'''
f=open("app.txt","r")
s=f.readline(5)
a=f.readline()
print(s)
print(a)
'''

#===============================
'''
#readlines()
f=open("app.txt","r")
s=f.readlines()
print(s)

'''
