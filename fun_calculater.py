n1=int(input("enter number"))
n2=int(input("enter number 2:"))
n3=int(input("enter number 3:"))
def add_no(n1,n2):
    return n1+n2

def sub_no(n1,n3):
    return n1-n3

def multi_no(n1,n2):
    return n1*n2

def divide_no(n1,n3):
    return n1/n3

def modulo_no(n2,n3):
    return n2%n3

while(True):
    print("---menu---")
    print("1)addition")
    print("2)substraction")
    print("3)multiplication")
    print("4)division")
    print("5)modulo")
    print("6)exit")

    choice=int(input("enter choice:"))
    if(choice==1):
        print("addition:",add_no(n1,n2))
    elif(choice==2):
        print("substraction:",sub_no(n1,n3))
    elif(choice==3):
        print("multiplication:",multi_no(n1,n2))
    elif(choice==4):
        print("division:",divide_no(n1,n3))
    elif(choice==5):
        print("modulo:",modulo_no(n2,n3))
    elif(choice==6):
        break
    else:
        print("invalid choice")

        