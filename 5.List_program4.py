#Program4
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

