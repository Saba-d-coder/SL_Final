list=[]

def ctok(c):
    k=c+273.15
    list.append({'from:'+str(c)+'deg C','to:'+str(k)+'K'})
    print("Converted to Kelvin:",k)

def ktoc(k):
    c=k-273.15
    list.append({'from:'+str(k)+'K','to:'+str(c)+'deg C'})
    print("Converted to Celsius :",c)

def ctof(c):
    f=(9/5)*c+32
    list.append({'from:'+str(c)+'deg C','to:'+str(f)+'deg F'})
    print("Converted to Farenheit:",f)

def ftoc(f):
    c=(f-32)*5/9
    list.append({'from:'+str(f)+'deg C','to:'+str(c)+'deg C'})
    print("Converted to Celsius:",c)

def ftok(f):
    k=((f-32)*5/9)+273.15
    list.append({'from:'+str(f)+'deg F','to:'+str(k)+'K'})
    print("Converted to Kelvin:",k)

def ktof(k):
    f=((9/5)*(k-273.15))+32
    list.append({'from:'+str(k)+'K','to:'+str(f)+'deg F'})
    print("Converted to Farenheit :",f)

while(1):
    print("\nEnter 1- For conversion \n any other key to stop")
    n=int(input())

    if(n==1):

        ch=int(input("\nEnter 1- for ctok\n2-ktoc\n3-ctof\n4-ftoc\n5-ftok\n6-ktof\n7-to see history"))
        if ch==1:
            t=float(input("Enter tmp in celsius"))
            ctok(t)
        elif ch==2:
            t=float(input("Enter tmp in kelvin"))
            ktoc(t)
            
        elif ch==3:
            t=float(input("Enter tmp in celsius"))
            ctof(t)
        
        elif ch==4:
            t=float(input("Enter tmp in farenheit"))
            ftoc(t)

        elif ch==5:
            t=float(input("Enter tmp in farenheit "))
            ftok(t)

        elif ch==6:
            t=float(input("Enter tmp in kelvin"))
            ktof(t)

        elif ch==7:
            print(list)

        else:
            print("\ninvalid input")
            
    else:
        break


