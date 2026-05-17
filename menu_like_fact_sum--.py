n=int(input("enter number:"))
sum=0
fact=1

while(True):
    print("---menu----")
    print("1)sum")
    print("2)factorial")
    print("3)power value")
    choice=int(input("enter choice:"))
    if(choice==1):
        i=1
        while(i<=n):
            sum=sum+i
            i=i+1
        print("sum of i:",sum)
    elif(choice==2):
        i=1
        while(i<=n):
            fact=fact*i
            i=i+1
        print("factorial of n:",fact)
    elif(choice==3):
        base=int(input("enter base:"))
        exp=int(input("enter exponant:"))
        i=1
        power=1
        while(i<=exp):
            power=power*base
            i=i+1
        print("power value:",power)
    elif(choice==4):
        break
    else:
        print("invalide choice")