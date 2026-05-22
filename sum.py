n=int(input("enter n:"))
cubes=0
sum=0
for i in range(1,n+1):
    cubes=i*i*i
    sum=sum+cubes
print(i,cubes,sum)