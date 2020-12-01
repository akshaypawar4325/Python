#Program8
grocery=[["rice",10],["wheat",20],["oil",30],["bread",40]]

basket=[]

buy=input("enter the product name:")

for i in range(len(grocery)):
    
    if(buy==grocery[i][0]):
        print("Product is available")
        basket.append(grocery[i])
            
print(basket)
