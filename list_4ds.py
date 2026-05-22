list_4=[1,2,3,4,5,6,7]
search_value=int(input("Enter a search item: "))

def search(search_value):
    flag=0
    for i in range(len(list_4)):
        if(list_4[i]==search_value):
            flag=1
    return flag

result=search(search_value)
if(result==1):
    print("Element is present")
else:
    print("Element is not present")


