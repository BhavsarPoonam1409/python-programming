n=int(input("enter number:"))
dict_sq_cubes={}
for i in range(1,n+1):
    sq=i*i
    cubes=i*i*i
    dict_sq_cubes[i]=[sq,cubes]
print(dict_sq_cubes)
