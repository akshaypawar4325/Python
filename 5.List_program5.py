#Program5
product=["oil","bread","rice","sugar"]
option=0

while(option!=5):
    print("1.Add product")
    print("2.remove product")
    print("3.insert product")
    print("4.print list")
    print("5.exit")

    option=int(input("enter the value"))

    if(option==1):
        a=input("enter product name: ")
        product.append(a)
    elif(option==2):
        a=input("enter product name: ")
        product.remove(a)

    elif(option==3):
        
        a=input("enter product name: ")
        b=int(input("Index position"))
        product.insert(b,a)
    elif(option==4):

        print(product)
    elif(option==5):
        
        print("exit")
