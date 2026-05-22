n1=int(input("Enter number 1:"))
n2=int(input("Enter number 2:"))
while(True):
    print("----Menu----")
    print("1) Addition")
    print("2) Subtraction")
    print("3) Exit")
    choice=int(input("Enter choice:"))
    if(choice==1):
        ans=n1+n2
        print("Addition:" ,ans)
    elif(choice==2):
        print("Subtraction:" ,n1-n2)
    elif(choice==3):
        break
    else:
        print("Enter valid choice")

