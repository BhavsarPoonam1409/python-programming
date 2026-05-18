n=int(input("enter number:"))
list_1=[]
even_list=[]
odd_list=[]
for i in range(1,n+1):
    list_1.append(i)
    if(i%2==0):
        even_list.append(i)
    else:
        odd_list.append(i)
print("list of integer number:",list_1)
print("even number of list:",even_list)
print("odd number of list:",odd_list)