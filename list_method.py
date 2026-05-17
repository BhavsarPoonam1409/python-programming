n=int(input("enter n:"))
even_list=[]
odd_list=[]
for i in range(1,n+1):
    if(i%2==0):
        even_list.append(i)
    else:
        odd_list.append(i)

print(even_list)
print(odd_list)