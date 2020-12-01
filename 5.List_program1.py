# Program1
num=[25,24,64,12,78,51,94,1];

max=num[0];

for i in range(1,len(num)):
    if (num[i]>max):

        max=num[i];
print(max)



'''
# Program 2

num=[25,24,64,12,78,51,94,1];

min=num[0];

for i in range(1,len(num)):
    if (num[i]<min):

        min=num[i];
print(min)

'''

"""
# Program 3

shop=["oil","bread","milk","salt","sugar"]

bag=[]
buy=input("which product")
for i in range(len(shop)):
        if(buy==shop[i]):
                print("product is available")
                bag.append(buy)
                
print(bag)

"""

'''
# Program 4
shop=["oil","bread","milk","salt","sugar"]
bag=[]


buy=input("which product")
for i in range(len(shop)):

    if(buy==shop[i]):
        print("product is available");
        bag.append(buy)
print(bag)

rem=input("Remove ?")

for i in range(len(bag)):
    if(rem==bag[i]):
        bag.remove(rem)
        break
print(bag)

'''
