list_1=[12,56,78]
sum_list=[]
average_list=[]
sum=0
for i in list_1:
    sum=sum+i
    sum_list.append(sum)
average=sum/3
average_list.append(average)
print(sum_list)
print(average_list)