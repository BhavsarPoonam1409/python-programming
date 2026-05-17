n1=int(input("enter n1:"))
n2=int(input("enter n2:"))
n3=int(input("enter n3:"))
n4=int(input("enter n4:"))
if(n1<n2):
    if(n1<n3):
        if(n1<n4):
            print("n1 is a small")
        else:
            print("n4 is a small")
    else:
        if(n3<n4):
            print("n3 is a small")
        else:
            print("n4 is a small")
else:
    if(n2<n3):
        if(n2<n4):
            print("n2 is a small")
        else:
            print("n4 is a small")
    else:
        if(n3<n4):
            print("n3 is a small")
        else:
            print("n4 is a small")