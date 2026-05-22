n=int(input("Enter value of n: "))
sum_cubes=0
cubes_list=[]
sum_cubes_list=[]
for i in range(1,n+1):
    cubes=i*i*i
    sum_cubes=sum_cubes+cubes
    cubes_list.append(cubes)
    sum_cubes_list.append(sum_cubes)

print(cubes_list)
print(sum_cubes_list)


