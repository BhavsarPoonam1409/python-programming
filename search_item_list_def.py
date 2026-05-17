list_1=[12,34,56,78,11.23]
item=int(input("enter item:"))


def search(item):
    for i in range(len(list_1)):
        flage=0
        if(item==list_1[i]):
            flage=1
        return flage
    
result=search(item)
if(result==1):
    print("present")
else:
    print("not present")
