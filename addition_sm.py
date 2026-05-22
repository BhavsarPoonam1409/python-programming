no1=int(input("Enter num1:"))
no2=int(input("Enter num2:"))
no3=int(input("Enter num3:"))
no4=int(input("Enter num4:"))
no5=int(input("Enter num5:"))
total=no1+no2+no3+no4+no5
print("total:",total)
if(total>100):
    print("substraction",total-100)
elif(total>75 and total<=100):
    print("multipication",total*5)
else:
    print("addition",total+25)