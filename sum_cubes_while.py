n=int(input("enter number:"))
i=1
sum_cubes=0
while(i<=n):
    cubes=i*i*i
    sum_cubes=sum_cubes+cubes
    i=i+1
print("sum of cubes is",sum_cubes)