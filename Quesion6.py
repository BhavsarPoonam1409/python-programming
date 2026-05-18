n1=int(input("enter number 1: "))
n2=int(input("enter number 2: "))
def swap_no(n1,n2):
    temp=n1
    n1=n2
    n2=temp
    print("after swepping value:",n1,n2)
    return n1,n2
swap_no(n1,n2)
print("before swapping value: ",n1,n2)
