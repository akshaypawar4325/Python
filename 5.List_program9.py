#Program9
grocery=[["rice",10],["wheat",20],["oil",30],["bread",40]]

basket=[]

select=0

while(select<4):
    print("1.append")
    print("2.bill")
    print("3.basket list")
    select=int(input("Select the option"))
    if(select==1):
        
        buy=input("Enter the product name:")
        for i in range(len(grocery)):
            if(buy==grocery[i][0]):
                print("product found")
                basket.append(grocery[i])
    elif(select==2):
        
        b=0
        for i in range(len(basket)):
            
            b=b+basket[i][1]
        print("Your total bill is",b)
    elif(select==3):
        print(basket)
