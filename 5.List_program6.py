
product=[]
cost=[]
option=0

while(option!=6):
    print("1.Add product")
    print("2.remove product")
    print("3.insert product")
    print("4.print list")
    print("5.Generate bill")
    print("6.exit")

    option=int(input("enter the value"))

    if(option==1):
        n=int(input("How many items to add:"))
        for i in range(n):
            a=input("enter product name:")
            b=int(input("enter the product cost:"))
            product.append(a)
            cost.append(b)
    elif(option==2):
        n=int(input("How many items to remove"))
        for i in range(n):
            a=input("enter product name:")
            if(a in product):
                index=product.index(a)
                product.remove(a)
                cost.remove(cost[index])
            else:
                print(a,"not in list")

    elif(option==3):
            a=int(input("Index position"))
            b=input("enter product name:")
            c=int(input("enter the cost"))
        product.insert(a,b)
        cost.insert(a,c)
    elif(option==4):

        print(product,cost)

    elif(option==5):
       c=0
       for i in range(len(cost)):
           c=c+cost[i]
       print("Your total bill is",c)
    elif(option==6):
        
        print("exit")
