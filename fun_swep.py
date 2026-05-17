a=int(input("enter a:"))
b=int(input("enter b:"))
def swep_no(a,b):
    temp=a
    a=b
    b=temp
    print("After swepping :",a,b)
    return 

print("Befor swepping:",a,b)
swep_no(a,b)