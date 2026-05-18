list_int=[12,56,78,89,78,99,90,85,34,44]
while(True):
    print("----menu----")
    print("1)add a nem element at the end")
    print("2)insert an element at index 3")
    print("3)remove the last element")
    print("4)sort the list")
    print("5)revers the list")
    print("6)exit")
    choice=int(input("enter choice"))
    if(choice==1):
        list_int.append(23)
        print(list_int)
    elif(choice==2):
        list_int.insert(3,77)
        print(list_int)
    elif(choice==3):
        list_int.pop()
        print(list_int)
    elif(choice==4):
        list_int.sort()
        print(list_int)
    elif(choice==5):
        list_int.reverse()
        print(list_int)
    elif(choice==6):
        break
    else:
        print("invalid choice")