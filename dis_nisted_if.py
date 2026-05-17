age=int(input("enter age:"))
mem_ship=input("enter member ship:")
if(age>25):
    if(mem_ship=='true'):
        print("50% discount")
    else:
        print("40% discount")
else:
    if(age<=25):
        if(mem_ship=='true'):
            print("30% discount")
        else:
            print("20% discount")