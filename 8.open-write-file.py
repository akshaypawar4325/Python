#Write() in python
f=open("grocery.txt","w")
f.write("Python is the general purpose high level programming language\n")
l=["hi\n","hello","123\n"]
f.writelines(l)
f.close()

#===================
'''
#Read menu list from grocery file and write it into the second one basket file
f=open("grocery.txt","r")
g=open("basket.txt","w")
basket=[]
shop=f.readlines()
n=input("which element")
n=n+"\n"
if n in shop:
    basket.append(n)
g.writelines(basket)
f.close()
g.close()
'''
#============================
'''
f=open("grocery.txt","r")
g=open("basket.txt","w")

grocery=f.readlines()
basket=[]
print(grocery)
buy=input("Buy product name:")
buy=buy+"\n"
if buy in grocery:
        basket.append(buy)
print(basket)


g.writelines(basket)

g.close()
f.close()
'''
'''
==============================
readlines() used for creating a list in file like txt,..
read() used to read and write the string
============================================
'''
