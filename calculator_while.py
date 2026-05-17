no1=int(input("enter number 1:"))
no2=int(input("enter number 2:"))
no3=int(input("enter number 3:"))
while(True):
    print("----menu----")
    print("1)addition")
    print("2)substraction")
    print("3)multiplication")
    print("4)integer division")
    print("5)floating division")
    print("6)modulo")
    print("7)exit")
    choice=int(input("enter choice:"))
    if(choice==1):
        print("addition:",no1+no2)
    elif(choice==2):
        print("substraction:",no2-no1)
    elif(choice==3):
        print("multiplication:",no2*no3)
    elif(choice==4):
        print("integer division:",no1//no2)
    elif(choice==5):
        print("floating division:",no1/no2)
    elif(choice==6):
        print("modulo:",no1%no3)
    elif(choice==7):
        break
    else:
        print("invalid choice")