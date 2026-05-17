base=int(input("enter base:"))
exp=int(input("enter exp:"))
power=1
for i in range(1,exp+1):
    power=power*base
print("the answer is :",power)