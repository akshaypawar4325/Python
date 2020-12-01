f=open("app.txt","r")

s=f.readlines()
line=len(s)
f.seek(0)
char=0
words=0

s=f.read()
for i in s:
    char=char+1
    if(i==" " or i=="\n"):
        words=words+1
print("line: ",line)
print("char: ",char)
print("words: ",words)
