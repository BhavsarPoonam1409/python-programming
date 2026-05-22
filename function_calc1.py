def add(x,y):
    return x + y
def sub(x,y):
    return x - y
def multi(x,y):
    return x *y
def divide(x,y):
    return x / y
def modulo(x,y):
    return x % y

no1=float(input("Enter a first number: "))
no2=float(input("Enter a second number: "))
while(True):
    print("1)addition")
    print("2)substraction")
    print("3)multiplication")
    print("4)divide")
    print("5)modulos")
    print("6)exite")
    choice=int(input("enter a choice: "))
    if(choice==1):
        addition=add(no1,no2)
        print("addition in function:",addition)
    elif(choice==2):
        substraction=sub(no1,no2)
        print("substraction in function:",substraction)
    elif(choice==3):
        multiplication=multi(no1,no2)
        print("multiplication in function:",multiplication)
    elif(choice==4):
        divide=divide(no1,no2)
        print("divition in function:",divide) 
    elif(choice==5):
        modulos=modulo(no1,no2)
        print("modulo in function:",modulos)
    elif(choice==6):
        break
    else:
        print("Invalid value")
        