n1=int(input("enter n1:"))
n2=int(input("enter n2:"))
n3=int(input("enter n3:"))
if(n1>n2):
    if(n1>n3):
        print("n1 is a large")
    else:
        print("n3 is a large")
else:
    if(n2>n3):
        print("n2 is a large")
    else:
        print("n3 is a large")