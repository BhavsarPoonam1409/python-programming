n1=int(input("enter n1:"))
n2=int(input("enter n2:"))
n3=int(input("enter n3:"))
total=n1+n2+n3
per=total/3
if(per>80):
    print("distiction")
elif(per>70 and per<=80):
    print("first class")
elif(per>60 and per<=70):
    print("second class")
elif(per>50 and per<=60):
    print("third class")
elif(per>40 and per<=50):
    print("pass class")
else:
    print("fail class")