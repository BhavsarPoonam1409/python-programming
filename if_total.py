n1=int(input("enter n1:"))
n2=int(input("enter n2:"))
n3=int(input("enter n3:"))
n4=int(input("enter n4:"))
n5=int(input("enter n5:"))
total=n1+n2+n3+n4+n5
if(total>100):
    print("substraction:",total-100)
elif(total>75 and total<=100):
    print("multiplication:",total*5)
else:
    print("addition:",total+25)