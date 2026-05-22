list_1=[12,45,67]
sum_tuple=()
average_tuple=()
sum=0
for i in list_1:
    sum=sum+i
    sum_tuple=sum_tuple+(sum,)
average=sum/3
average_tuple=average_tuple+(average,)
print(sum_tuple)
print(average_tuple)