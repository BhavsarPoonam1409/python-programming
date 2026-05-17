n=int(input("enter number:"))
t1=0
t2=1
t3=t1+t2
print(t1)
print(t2)
for i in range(2,n):
    print(t3)
    t1=t2
    t2=t3
    t3=t1+t2

t1=0
t2=1
t3=t1+t2   
sum=0    
for i in range(2,n+2):
    sum=sum+t1
    t1=t2
    t2=t3
    t3=t1+t2
print("sum",sum)
    
    