list_1=[]
for i in range(10,55,5):
    list_1.append(i)


def fun_list(list_1):
    max_no=max(list_1)
    min_no=min(list_1)
    sum_no=sum(list_1)
    return (max_no,min_no,sum_no)

max_no,min_no,sum_no=fun_list(list_1)
print(max_no,min_no,sum_no)